# users/authentication.py

import os
from typing import Final

AUTH_VAR: Final[str] = os.environ.get("AUTH_VAR", "local_user_db")

if AUTH_VAR == "ldap":
    from users.ldap import LDAPAuth as Authentication
else:
    from users.local_user_db import LocalUserDB as Authentication


if __name__ == "__main__":
    auth = Authentication()
    print(Authentication.hash_username("example_user"))
    print(Authentication.hash_password("example_password"))

    auth.add_user("jsmith1", "securepassword123")
    assert auth.authenticate("jsmith1", "securepassword123") is True
    assert auth.authenticate("jsmith1", "wrongpassword") is False
    assert auth.authenticate("unknown", "securepassword123") is False

    if hasattr(auth, "delete_user"):
        auth.delete_user("jsmith1")
        assert auth.authenticate("jsmith1", "securepassword123") is False
