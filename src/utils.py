"""
Utility functions for Asisten Shadow
"""

import os
import json
import base64
import hashlib
import datetime
from typing import Dict, Any, Optional
from config import HASH_ALGORITHM, SCREEN_WIDTH, HEADER_CHAR, SEPARATOR_CHAR


def load_data(filename: str) -> Dict:
    """
    Memuat data dari file JSON
    
    Args:
        filename: Path ke file JSON
        
    Returns:
        Dictionary berisi data atau empty dict jika file tidak ada
    """
    if not os.path.exists(filename):
        return {}
    
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, dict) else {}
    except (json.JSONDecodeError, IOError) as e:
        print(f"Warning: Error loading {filename}: {e}")
        return {}


def save_data(filename: str, data: Dict) -> bool:
    """
    Menyimpan data ke file JSON
    
    Args:
        filename: Path ke file JSON
        data: Dictionary data yang akan disimpan
        
    Returns:
        True jika berhasil, False jika gagal
    """
    try:
        # Ensure directory exists
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        return True
    except IOError as e:
        print(f"Error: Gagal menyimpan data ke {filename}: {e}")
        return False


def hash_password(password: str, algorithm: str = HASH_ALGORITHM) -> str:
    """
    Hash password menggunakan algoritma yang ditentukan
    
    Args:
        password: Password yang akan di-hash
        algorithm: Algoritma hash (default: sha256)
        
    Returns:
        String hasil hash
    """
    if algorithm == "sha256":
        return hashlib.sha256(password.encode()).hexdigest()
    elif algorithm == "md5":
        return hashlib.md5(password.encode()).hexdigest()
    else:
        return hashlib.sha256(password.encode()).hexdigest()


def encode_text(text: str) -> str:
    """
    Encode teks dengan Base64
    
    Args:
        text: Teks yang akan di-encode
        
    Returns:
        String hasil encode
    """
    try:
        return base64.b64encode(text.encode()).decode()
    except Exception as e:
        print(f"Error encoding text: {e}")
        return ""


def decode_text(text_b64: str) -> str:
    """
    Decode teks dari Base64
    
    Args:
        text_b64: Teks Base64 yang akan di-decode
        
    Returns:
        String hasil decode atau error message
    """
    try:
        return base64.b64decode(text_b64.encode()).decode()
    except Exception:
        return "[ERROR: Data rusak]"


def get_timestamp(format: str = "%Y-%m-%d %H:%M:%S") -> str:
    """
    Mendapatkan timestamp saat ini
    
    Args:
        format: Format timestamp (default: YYYY-MM-DD HH:MM:SS)
        
    Returns:
        String timestamp
    """
    return datetime.datetime.now().strftime(format)


def clear_screen():
    """Membersihkan layar konsol"""
    os.system('cls' if os.name == 'nt' else 'clear')


def print_header(title: str, width: int = SCREEN_WIDTH, char: str = HEADER_CHAR):
    """
    Mencetak header dengan format yang rapi
    
    Args:
        title: Judul header
        width: Lebar header
        char: Karakter pembatas
    """
    print("\n" + char * width)
    print(f"{title:^{width}}")
    print(char * width)


def print_separator(width: int = SCREEN_WIDTH, char: str = SEPARATOR_CHAR):
    """
    Mencetak separator
    
    Args:
        width: Lebar separator
        char: Karakter separator
    """
    print(char * width)


def print_menu(options: list, width: int = SCREEN_WIDTH):
    """
    Mencetak menu dengan format yang rapi
    
    Args:
        options: List opsi menu
        width: Lebar menu
    """
    print_separator(width)
    for i, option in enumerate(options, 1):
        print(f"  {i}. {option}")
    print_separator(width)


def get_input(prompt: str, required: bool = True, strip: bool = True) -> str:
    """
    Mendapatkan input dengan validasi
    
    Args:
        prompt: Pesan prompt
        required: Apakah input wajib diisi
        strip: Apakah whitespace dihapus
        
    Returns:
        String input dari user
    """
    while True:
        value = input(prompt)
        if strip:
            value = value.strip()
        
        if not required or value:
            return value
        print("❌ Input tidak boleh kosong!")


def confirm_action(message: str) -> bool:
    """
    Konfirmasi aksi dari pengguna
    
    Args:
        message: Pesan konfirmasi
        
    Returns:
        True jika user konfirmasi (y), False jika tidak (n)
    """
    while True:
        response = input(f"{message} (y/n): ").lower().strip()
        if response in ['y', 'n']:
            return response == 'y'
        print("❌ Input tidak valid! Masukkan 'y' atau 'n'")


def validate_username(username: str, min_length: int = 3) -> tuple[bool, str]:
    """
    Validasi username
    
    Args:
        username: Username yang akan divalidasi
        min_length: Panjang minimal username
        
    Returns:
        Tuple (valid: bool, message: str)
    """
    if not username:
        return False, "Username tidak boleh kosong!"
    
    if len(username) < min_length:
        return False, f"Username minimal {min_length} karakter!"
    
    if not username.isalnum() and '_' not in username:
        return False, "Username hanya boleh mengandung huruf, angka, dan underscore!"
    
    return True, "Valid"


def validate_password(password: str, min_length: int = 6) -> tuple[bool, str]:
    """
    Validasi password
    
    Args:
        password: Password yang akan divalidasi
        min_length: Panjang minimal password
        
    Returns:
        Tuple (valid: bool, message: str)
    """
    if not password:
        return False, "Password tidak boleh kosong!"
    
    if len(password) < min_length:
        return False, f"Password minimal {min_length} karakter!"
    
    return True, "Valid"


def truncate_text(text: str, max_length: int = 30) -> str:
    """
    Memotong teks jika terlalu panjang
    
    Args:
        text: Teks yang akan dipotong
        max_length: Panjang maksimal
        
    Returns:
        Teks yang sudah dipotong dengan "..." di akhir
    """
    if len(text) <= max_length:
        return text
    return text[:max_length - 3] + "..."


def format_size(size_bytes: int) -> str:
    """
    Format ukuran file ke format yang mudah dibaca
    
    Args:
        size_bytes: Ukuran dalam bytes
        
    Returns:
        String ukuran yang terformat (e.g., "1.5 KB")
    """
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.1f} TB"


def create_backup(source_file: str, backup_dir: str = None) -> Optional[str]:
    """
    Membuat backup dari file
    
    Args:
        source_file: File yang akan di-backup
        backup_dir: Direktori tujuan backup (opsional)
        
    Returns:
        Path file backup atau None jika gagal
    """
    try:
        if not os.path.exists(source_file):
            return None
        
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = os.path.basename(source_file)
        name, ext = os.path.splitext(filename)
        
        if backup_dir:
            os.makedirs(backup_dir, exist_ok=True)
            backup_file = os.path.join(backup_dir, f"{name}_backup_{timestamp}{ext}")
        else:
            backup_file = f"{source_file}.backup_{timestamp}"
        
        import shutil
        shutil.copy2(source_file, backup_file)
        return backup_file
    except Exception as e:
        print(f"Error creating backup: {e}")
        return None


def sanitize_filename(filename: str) -> str:
    """
    Membersihkan nama file dari karakter tidak valid
    
    Args:
        filename: Nama file yang akan dibersihkan
        
    Returns:
        Nama file yang sudah dibersihkan
    """
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        filename = filename.replace(char, '_')
    return filename


def parse_date(date_string: str) -> Optional[datetime.datetime]:
    """
    Parse string tanggal ke datetime object
    
    Args:
        date_string: String tanggal
        
    Returns:
        Datetime object atau None jika gagal
    """
    formats = [
        "%Y-%m-%d %H:%M:%S",
        "%Y-%m-%d",
        "%d/%m/%Y",
        "%d-%m-%Y"
    ]
    
    for fmt in formats:
        try:
            return datetime.datetime.strptime(date_string, fmt)
        except ValueError:
            continue
    return None


def pretty_print_dict(data: Dict, indent: int = 0):
    """
    Print dictionary dengan format yang rapi
    
    Args:
        data: Dictionary yang akan di-print
        indent: Level indentasi
    """
    for key, value in data.items():
        if isinstance(value, dict):
            print("  " * indent + f"{key}:")
            pretty_print_dict(value, indent + 1)
        else:
            print("  " * indent + f"{key}: {value}")
