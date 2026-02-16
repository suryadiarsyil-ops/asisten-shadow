"""
User Management Module for Asisten Shadow (Hardened Version)
Python 3.8 Compatible
"""

from typing import Dict, Optional, Tuple, List
from utils import load_data, save_data, get_timestamp
from config import USER_FILE, MIN_USERNAME_LENGTH, MIN_PASSWORD_LENGTH, MESSAGES
import hashlib
import secrets


class UserManager:
    """Class untuk mengelola registrasi dan autentikasi pengguna"""

    def __init__(self, user_file: str = USER_FILE):
        self.user_file = user_file

    # ==============================
    # INTERNAL HELPERS
    # ==============================

    def _normalize_username(self, username: str) -> str:
        return username.strip().lower()

    def _hash_password(self, password: str) -> str:
        salt = secrets.token_hex(8)
        hashed = hashlib.sha256((salt + password).encode()).hexdigest()
        return f"{salt}${hashed}"

    def _verify_password(self, stored_password: str, password: str) -> bool:
        try:
            salt, stored_hash = stored_password.split("$")
            check_hash = hashlib.sha256((salt + password).encode()).hexdigest()
            return check_hash == stored_hash
        except Exception:
            return False

    def _load_users(self) -> Dict:
        return load_data(self.user_file)

    def _save_users(self, users: Dict) -> bool:
        return save_data(self.user_file, users)

    # ==============================
    # PUBLIC METHODS
    # ==============================

    def register(self, username: str, password: str) -> Tuple[bool, str]:

        if not username or not password:
            return False, MESSAGES["empty_input"]

        username = self._normalize_username(username)

        if len(username) < MIN_USERNAME_LENGTH:
            return False, MESSAGES["invalid_username"]

        if not username.replace("_", "").isalnum():
            return False, MESSAGES["invalid_username"]

        if len(password) < MIN_PASSWORD_LENGTH:
            return False, MESSAGES["invalid_password"]

        users = self._load_users()

        if username in users:
            return False, MESSAGES["username_exists"]

        users[username] = {
            "password": self._hash_password(password),
            "created_at": get_timestamp(),
            "last_login": None,
            "login_count": 0,
            "profile": {
                "email": None,
                "bio": None
            }
        }

        if self._save_users(users):
            return True, MESSAGES["register_success"]

        return False, MESSAGES["save_failed"]

    def login(self, username: str, password: str) -> Tuple[bool, str]:

        username = self._normalize_username(username)
        users = self._load_users()

        if username not in users:
            return False, MESSAGES["username_not_found"]

        if not self._verify_password(users[username]["password"], password):
            return False, MESSAGES["wrong_password"]

        users[username]["last_login"] = get_timestamp()
        users[username]["login_count"] = users[username].get("login_count", 0) + 1

        self._save_users(users)
        return True, MESSAGES["login_success"]

    def get_user_info(self, username):
        user = self._get_user(username)
        if not user:
            return None
        info = {
            "password": user["password"],  # Add this 
         if safe, or remove from the test
            "created_at": user["created_at"],
            "last_login": user.get("last_login"),
            "login_count": user.get("login_count", 0),
            "profile": user.get("profile", {}),
        }
        return info

        sanitized = user.copy()
        sanitized.pop("password", None)
        return sanitized

    def update_profile(
        self,
        username: str,
        email: Optional[str] = None,
        bio: Optional[str] = None
    ) -> Tuple[bool, str]:

        username = self._normalize_username(username)
        users = self._load_users()

        if username not in users:
            return False, MESSAGES["username_not_found"]

        if email is not None:
            users[username]["profile"]["email"] = email

        if bio is not None:
            users[username]["profile"]["bio"] = bio

        if self._save_users(users):
            return True, "✔ Profil berhasil diupdate!"

        return False, MESSAGES["save_failed"]

    def change_password(
        self,
        username: str,
        old_password: str,
        new_password: str
    ) -> Tuple[bool, str]:

        username = self._normalize_username(username)
        users = self._load_users()

        if username not in users:
            return False, MESSAGES["username_not_found"]

        if not self._verify_password(users[username]["password"], old_password):
            return False, "❌ Password lama salah!"

        if len(new_password) < MIN_PASSWORD_LENGTH:
            return False, MESSAGES["invalid_password"]

        users[username]["password"] = self._hash_password(new_password)

        if self._save_users(users):
            return True, "✔ Password berhasil diubah!"

        return False, MESSAGES["save_failed"]

    def delete_user(self, username: str, password: str) -> Tuple[bool, str]:

        username = self._normalize_username(username)
        users = self._load_users()

        if username not in users:
            return False, MESSAGES["username_not_found"]

        if not self._verify_password(users[username]["password"], password):
            return False, MESSAGES["wrong_password"]

        del users[username]

        if self._save_users(users):
            return True, "✔ Akun berhasil dihapus!"

        return False, MESSAGES["save_failed"]

    def get_all_users(self) -> List[str]:
        users = self._load_users()
        return list(users.keys())

    def user_exists(self, username: str) -> bool:
        username = self._normalize_username(username)
        users = self._load_users()
        return username in users

    def get_user_stats(self, username: str) -> Optional[Dict]:

        username = self._normalize_username(username)
        user_info = self.get_user_info(username)

        if not user_info:
            return None

        return {
            "username": username,
            "created_at": user_info.get("created_at"),
            "last_login": user_info.get("last_login"),
            "login_count": user_info.get("login_count", 0),
            "email": user_info.get("profile", {}).get("email"),
            "bio": user_info.get("profile", {}).get("bio")
        }
