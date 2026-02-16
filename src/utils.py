"""
Utility functions for Asisten Shadow
"""

import os
import json
import base64
import hashlib
import datetime
import shutil
from typing import Dict, Optional, Tuple, List
from config import HASH_ALGORITHM, SCREEN_WIDTH, HEADER_CHAR, SEPARATOR_CHAR


def load_data(filename: str) -> Dict:
    if not os.path.exists(filename):
        return {}

    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, dict) else {}
    except (json.JSONDecodeError, IOError):
        return {}


def save_data(filename: str, data: Dict) -> bool:
    try:
        directory = os.path.dirname(filename)
        if directory:
            os.makedirs(directory, exist_ok=True)

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        return True
    except IOError:
        return False


def hash_password(password: str, algorithm: str = HASH_ALGORITHM) -> str:
    if algorithm == "md5":
        return hashlib.md5(password.encode()).hexdigest()
    return hashlib.sha256(password.encode()).hexdigest()


def encode_text(text: str) -> str:
    try:
        return base64.b64encode(text.encode()).decode()
    except Exception:
        return ""


def decode_text(text_b64: str) -> str:
    try:
        return base64.b64decode(text_b64.encode()).decode()
    except Exception:
        return "[ERROR: Data rusak]"


def get_timestamp(fmt: str = "%Y-%m-%d %H:%M:%S") -> str:
    return datetime.datetime.now().strftime(fmt)


def validate_username(username: str, min_length: int = 3) -> Tuple[bool, str]:
    if not username:
        return False, "Username tidak boleh kosong!"

    if len(username) < min_length:
        return False, f"Username minimal {min_length} karakter!"

    if not username.replace("_", "").isalnum():
        return False, "Username hanya boleh huruf, angka, underscore!"

    return True, "Valid"


def validate_password(password: str, min_length: int = 6) -> Tuple[bool, str]:
    if not password:
        return False, "Password tidak boleh kosong!"

    if len(password) < min_length:
        return False, f"Password minimal {min_length} karakter!"

    return True, "Valid"
