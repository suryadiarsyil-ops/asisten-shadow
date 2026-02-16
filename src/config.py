"""
Configuration file for Asisten Shadow
"""

import os

# Application Information
APP_NAME = "Asisten Shadow"
VERSION = "2.0.0"
AUTHOR = "Asisten Shadow Team"
DESCRIPTION = "Aplikasi catatan pribadi terenkripsi dengan keamanan tingkat tinggi"

# Directory Configuration
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(os.path.dirname(BASE_DIR), "data")

# Ensure data directory exists
os.makedirs(DATA_DIR, exist_ok=True)

# File Paths
USER_FILE = os.path.join(DATA_DIR, "users.json")
NOTES_FILE = os.path.join(DATA_DIR, "notes.json")

# Security Settings
MIN_USERNAME_LENGTH = 3
MIN_PASSWORD_LENGTH = 6
HASH_ALGORITHM = "sha256"

# UI Settings
SCREEN_WIDTH = 50
HEADER_CHAR = "="
SEPARATOR_CHAR = "-"

# Note Settings
MAX_PREVIEW_LENGTH = 30
MAX_SEARCH_RESULTS = 20

# Export Settings
EXPORT_FORMAT = "json"
EXPORT_INDENT = 4

# Validation Messages
MESSAGES = {
    "empty_input": "❌ Input tidak boleh kosong!",
    "invalid_username": f"❌ Username minimal {MIN_USERNAME_LENGTH} karakter!",
    "invalid_password": f"❌ Password minimal {MIN_PASSWORD_LENGTH} karakter!",
    "username_exists": "❌ Username sudah digunakan!",
    "username_not_found": "❌ Username tidak ditemukan!",
    "wrong_password": "❌ Password salah!",
    "wrong_key": "❌ Kunci salah!",
    "password_mismatch": "❌ Password tidak cocok!",
    "register_success": "✔ Registrasi berhasil! Silakan login.",
    "login_success": "✔ Login berhasil!",
    "logout_success": "✔ Logout berhasil!",
    "note_added": "✔ Catatan berhasil ditambahkan!",
    "note_edited": "✔ Catatan berhasil diedit!",
    "note_deleted": "✔ Catatan berhasil dihapus!",
    "no_notes": "⚠ Belum ada catatan.",
    "invalid_note_number": "❌ Nomor catatan tidak valid!",
    "export_success": "✔ Catatan berhasil diekspor!",
    "export_failed": "❌ Gagal mengekspor catatan!",
    "no_search_results": "⚠ Tidak ada catatan yang cocok.",
    "save_failed": "❌ Gagal menyimpan data!",
}

# Feature Flags
ENABLE_EXPORT = True
ENABLE_SEARCH = True
ENABLE_STATISTICS = True
ENABLE_BACKUP = True

# Debug Mode
DEBUG = False
