# users/local_user_db.py
import bcrypt
import psycopg2

from users.authentication_base import AuthenticationBase


class LocalUserDB(AuthenticationBase):
    @classmethod
    def hash_username(cls, username: str) -> str:
        # Implement a simple hashing mechanism for the username
        salt = bcrypt.gensalt()
        hashed_user = bcrypt.hashpw(username.encode('utf-8'), salt)

        if len(hashed_user) > 50:
            hashed_user = hashed_user[:50]
        return hashed_user

    @classmethod
    def hash_password(cls, password: str) -> str:
        # Implement a simple hashing mechanism for the password
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode('utf-8'), salt)

    def __init__(self):
        self.__db_conn = psycopg2.connect(
            database="webtesterdb",
            user="vscode"
        )
        self.__db_cursor = self.__db_conn.cursor()

    def close(self):
        if hasattr(self, "__db_cursor") and self.__db_cursor:
            self.__db_cursor.close()
            self.__db_cursor = None
        if hasattr(self, "__db_conn") and self.__db_conn:
            self.__db_conn.close()
            self.__db_conn = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def authenticate(self, username: str, password: str) -> bool:
        username_hash = self.hash_username(username)
        password_hash = self.hash_password(password)

        self.__db_cursor.execute(
            "SELECT * FROM users WHERE username_hash = %s AND password_hash = %s",
            (username_hash, password_hash)
        )
        user = self.__db_cursor.fetchone()
        return user is not None

    def add_user(self, username: str, password: str) -> None:
        username_hash = self.hash_username(username)
        password_hash = self.hash_password(password)

        self.__db_cursor.execute(
            "INSERT INTO users (username_hash, password_hash) VALUES (%s, %s)",
            (username_hash, password_hash)
        )
        self.__db_conn.commit()

    def delete_user(self, username: str) -> None:
        username_hash = self.hash_username(username)

        self.__db_cursor.execute(
            "DELETE FROM users WHERE username_hash = %s",
            (username_hash,)
        )
        self.__db_conn.commit()
