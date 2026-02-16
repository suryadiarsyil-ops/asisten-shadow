"""
Unit tests for UserManager
"""

import os
import sys
import pytest
import tempfile
import json

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from user_manager import UserManager


@pytest.fixture
def temp_user_file():
    """Create temporary user file for testing"""
    fd, path = tempfile.mkstemp(suffix='.json')
    os.close(fd)
    yield path
    if os.path.exists(path):
        os.unlink(path)


@pytest.fixture
def user_manager(temp_user_file):
    """Create UserManager instance with temp file"""
    return UserManager(temp_user_file)


class TestUserRegistration:
    """Test user registration functionality"""
    
    def test_register_valid_user(self, user_manager):
        """Test registering a valid user"""
        success, message = user_manager.register("testuser", "password123")
        assert success is True
        assert "berhasil" in message.lower()
    
    def test_register_duplicate_username(self, user_manager):
        """Test registering with duplicate username"""
        user_manager.register("testuser", "password123")
        success, message = user_manager.register("testuser", "newpassword")
        assert success is False
        assert "sudah" in message.lower()
    
    def test_register_short_username(self, user_manager):
        """Test registering with short username"""
        success, message = user_manager.register("ab", "password123")
        assert success is False
        assert "minimal" in message.lower()
    
    def test_register_short_password(self, user_manager):
        """Test registering with short password"""
        success, message = user_manager.register("testuser", "12345")
        assert success is False
        assert "minimal" in message.lower()
    
    def test_register_empty_credentials(self, user_manager):
        """Test registering with empty credentials"""
        success, message = user_manager.register("", "")
        assert success is False


class TestUserLogin:
    """Test user login functionality"""
    
    def test_login_valid_credentials(self, user_manager):
        """Test login with valid credentials"""
        user_manager.register("testuser", "password123")
        success, message = user_manager.login("testuser", "password123")
        assert success is True
        assert "berhasil" in message.lower()
    
    def test_login_invalid_username(self, user_manager):
        """Test login with invalid username"""
        success, message = user_manager.login("nonexistent", "password123")
        assert success is False
        assert "tidak ditemukan" in message.lower()
    
    def test_login_invalid_password(self, user_manager):
        """Test login with invalid password"""
        user_manager.register("testuser", "password123")
        success, message = user_manager.login("testuser", "wrongpassword")
        assert success is False
        assert "salah" in message.lower()
    
    def test_login_updates_last_login(self, user_manager):
        """Test that login updates last_login timestamp"""
        user_manager.register("testuser", "password123")
        user_manager.login("testuser", "password123")
        user_info = user_manager.get_user_info("testuser")
        assert user_info["last_login"] is not None


class TestUserInfo:
    """Test user information retrieval"""
    
    def test_get_existing_user_info(self, user_manager):
        """Test getting info for existing user"""
        user_manager.register("testuser", "password123")
        user_info = user_manager.get_user_info("testuser")
        assert user_info is not None
        assert "password" in user_info
        assert "created_at" in user_info
    
    def test_get_nonexistent_user_info(self, user_manager):
        """Test getting info for nonexistent user"""
        user_info = user_manager.get_user_info("nonexistent")
        assert user_info is None
    
    def test_user_exists(self, user_manager):
        """Test user_exists method"""
        user_manager.register("testuser", "password123")
        assert user_manager.user_exists("testuser") is True
        assert user_manager.user_exists("nonexistent") is False


class TestPasswordManagement:
    """Test password management functionality"""
    
    def test_change_password_success(self, user_manager):
        """Test successful password change"""
        user_manager.register("testuser", "oldpassword")
        success, message = user_manager.change_password(
            "testuser", "oldpassword", "newpassword123"
        )
        assert success is True
        
        # Verify new password works
        success, _ = user_manager.login("testuser", "newpassword123")
        assert success is True
    
    def test_change_password_wrong_old_password(self, user_manager):
        """Test password change with wrong old password"""
        user_manager.register("testuser", "oldpassword")
        success, message = user_manager.change_password(
            "testuser", "wrongpassword", "newpassword123"
        )
        assert success is False
    
    def test_change_password_short_new_password(self, user_manager):
        """Test password change with short new password"""
        user_manager.register("testuser", "oldpassword")
        success, message = user_manager.change_password(
            "testuser", "oldpassword", "123"
        )
        assert success is False


class TestUserDeletion:
    """Test user deletion functionality"""
    
    def test_delete_user_success(self, user_manager):
        """Test successful user deletion"""
        user_manager.register("testuser", "password123")
        success, message = user_manager.delete_user("testuser", "password123")
        assert success is True
        assert user_manager.user_exists("testuser") is False
    
    def test_delete_user_wrong_password(self, user_manager):
        """Test user deletion with wrong password"""
        user_manager.register("testuser", "password123")
        success, message = user_manager.delete_user("testuser", "wrongpassword")
        assert success is False
        assert user_manager.user_exists("testuser") is True


class TestUserStats:
    """Test user statistics functionality"""
    
    def test_get_user_stats(self, user_manager):
        """Test getting user statistics"""
        user_manager.register("testuser", "password123")
        user_manager.login("testuser", "password123")
        
        stats = user_manager.get_user_stats("testuser")
        assert stats is not None
        assert stats["username"] == "testuser"
        assert stats["login_count"] >= 1
        assert "created_at" in stats


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
