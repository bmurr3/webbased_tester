# users/local_user_db.py
import hashlib
import psycopg2

from users.authentication_base import AuthenticationBase


class LocalUserDB(AuthenticationBase):
    @classmethod
    def hash_username(cls, username: str) -> str:
        # Implement a simple hashing mechanism for the username
        hashed_user = hashlib.sha256(username.encode()).hexdigest()

        if len(hashed_user) > 50:
            hashed_user = hashed_user[:50]
        return hashed_user

    @classmethod
    def hash_password(cls, password: str) -> str:
        # Implement a simple hashing mechanism for the password
        return hashlib.sha256(password.encode()).hexdigest()

    def __init__(self):
        self.__db_conn = psycopg2.connect(
            database="webtesterdb",
            user="vscode"
        )
        self.__db_cursor = self.__db_conn.cursor()

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
