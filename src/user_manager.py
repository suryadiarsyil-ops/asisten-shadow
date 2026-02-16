"""
User Management Module for Asisten Shadow
"""

from typing import Dict, Optional
from utils import load_data, save_data, hash_password, get_timestamp
from config import USER_FILE, MIN_USERNAME_LENGTH, MIN_PASSWORD_LENGTH, MESSAGES


class UserManager:
    """Class untuk mengelola registrasi dan autentikasi pengguna"""
    
    def __init__(self, user_file: str = USER_FILE):
        """
        Inisialisasi UserManager
        
        Args:
            user_file: Path ke file database user
        """
        self.user_file = user_file
    
    def register(self, username: str, password: str) -> tuple[bool, str]:
        """
        Registrasi pengguna baru
        
        Args:
            username: Username pengguna
            password: Password pengguna
            
        Returns:
            Tuple (success: bool, message: str)
        """
        # Validasi input
        if not username or not password:
            return False, MESSAGES["empty_input"]
        
        if len(username) < MIN_USERNAME_LENGTH:
            return False, MESSAGES["invalid_username"]
        
        if len(password) < MIN_PASSWORD_LENGTH:
            return False, MESSAGES["invalid_password"]
        
        # Load existing users
        users = load_data(self.user_file)
        
        # Check if username already exists
        if username in users:
            return False, MESSAGES["username_exists"]
        
        # Create new user
        users[username] = {
            "password": hash_password(password),
            "created_at": get_timestamp(),
            "last_login": None,
            "login_count": 0,
            "profile": {
                "email": None,
                "bio": None
            }
        }
        
        # Save to file
        if save_data(self.user_file, users):
            return True, MESSAGES["register_success"]
        
        return False, MESSAGES["save_failed"]
    
    def login(self, username: str, password: str) -> tuple[bool, str]:
        """
        Login pengguna
        
        Args:
            username: Username pengguna
            password: Password pengguna
            
        Returns:
            Tuple (success: bool, message: str)
        """
        users = load_data(self.user_file)
        
        # Check if username exists
        if username not in users:
            return False, MESSAGES["username_not_found"]
        
        # Verify password
        if users[username]["password"] != hash_password(password):
            return False, MESSAGES["wrong_password"]
        
        # Update last login
        users[username]["last_login"] = get_timestamp()
        users[username]["login_count"] = users[username].get("login_count", 0) + 1
        save_data(self.user_file, users)
        
        return True, MESSAGES["login_success"]
    
    def get_user_info(self, username: str) -> Optional[Dict]:
        """
        Mendapatkan informasi pengguna
        
        Args:
            username: Username pengguna
            
        Returns:
            Dictionary info user atau None jika tidak ditemukan
        """
        users = load_data(self.user_file)
        return users.get(username)
    
    def update_profile(self, username: str, email: str = None, bio: str = None) -> tuple[bool, str]:
        """
        Update profil pengguna
        
        Args:
            username: Username pengguna
            email: Email baru (opsional)
            bio: Bio baru (opsional)
            
        Returns:
            Tuple (success: bool, message: str)
        """
        users = load_data(self.user_file)
        
        if username not in users:
            return False, MESSAGES["username_not_found"]
        
        if email is not None:
            users[username]["profile"]["email"] = email
        
        if bio is not None:
            users[username]["profile"]["bio"] = bio
        
        if save_data(self.user_file, users):
            return True, "✔ Profil berhasil diupdate!"
        
        return False, MESSAGES["save_failed"]
    
    def change_password(self, username: str, old_password: str, new_password: str) -> tuple[bool, str]:
        """
        Ganti password pengguna
        
        Args:
            username: Username pengguna
            old_password: Password lama
            new_password: Password baru
            
        Returns:
            Tuple (success: bool, message: str)
        """
        users = load_data(self.user_file)
        
        if username not in users:
            return False, MESSAGES["username_not_found"]
        
        # Verify old password
        if users[username]["password"] != hash_password(old_password):
            return False, "❌ Password lama salah!"
        
        # Validate new password
        if len(new_password) < MIN_PASSWORD_LENGTH:
            return False, MESSAGES["invalid_password"]
        
        # Update password
        users[username]["password"] = hash_password(new_password)
        
        if save_data(self.user_file, users):
            return True, "✔ Password berhasil diubah!"
        
        return False, MESSAGES["save_failed"]
    
    def delete_user(self, username: str, password: str) -> tuple[bool, str]:
        """
        Hapus akun pengguna
        
        Args:
            username: Username pengguna
            password: Password untuk konfirmasi
            
        Returns:
            Tuple (success: bool, message: str)
        """
        users = load_data(self.user_file)
        
        if username not in users:
            return False, MESSAGES["username_not_found"]
        
        # Verify password
        if users[username]["password"] != hash_password(password):
            return False, MESSAGES["wrong_password"]
        
        # Delete user
        del users[username]
        
        if save_data(self.user_file, users):
            return True, "✔ Akun berhasil dihapus!"
        
        return False, MESSAGES["save_failed"]
    
    def get_all_users(self) -> list:
        """
        Mendapatkan daftar semua username (untuk admin)
        
        Returns:
            List username
        """
        users = load_data(self.user_file)
        return list(users.keys())
    
    def user_exists(self, username: str) -> bool:
        """
        Cek apakah username sudah ada
        
        Args:
            username: Username yang akan dicek
            
        Returns:
            True jika username ada, False jika tidak
        """
        users = load_data(self.user_file)
        return username in users
    
    def get_user_stats(self, username: str) -> Optional[Dict]:
        """
        Mendapatkan statistik pengguna
        
        Args:
            username: Username pengguna
            
        Returns:
            Dictionary statistik atau None
        """
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
