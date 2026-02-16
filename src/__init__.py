"""
Asisten Shadow - Aplikasi Catatan Terenkripsi
Version 2.0.0
"""

__version__ = "2.0.0"
__author__ = "Asisten Shadow Team"
__email__ = "contact@asistenshadow.com"
__description__ = "Aplikasi catatan pribadi terenkripsi dengan keamanan tingkat tinggi"

from .user_manager import UserManager
from .notes_manager import NotesManager
from .utils import *
from .config import *

__all__ = [
    "UserManager",
    "NotesManager",
]
