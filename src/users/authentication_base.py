# users/authentication_base.py

from abc import ABC, abstractmethod


class AuthenticationBase(ABC):
    @classmethod
    @abstractmethod
    def hash_username(cls, username: str) -> str:
        pass

    @classmethod
    @abstractmethod
    def hash_password(cls, password: str) -> str:
        pass

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def authenticate(self, username: str, password: str) -> bool:
        pass

    @abstractmethod
    def add_user(self, username: str, password: str) -> None:
        pass
