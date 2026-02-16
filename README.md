# 🕵️ Asisten Shadow

<div align="center">

![Version](https://img.shields.io/badge/version-2.0.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.7+-green.svg)
![License](https://img.shields.io/badge/license-MIT-orange.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

**Aplikasi catatan pribadi terenkripsi dengan keamanan tingkat tinggi**

[Fitur](#-fitur) • [Instalasi](#-instalasi) • [Penggunaan](#-penggunaan) • [Dokumentasi](#-dokumentasi) • [Kontribusi](#-kontribusi)

</div>

---

## 📋 Deskripsi

**Asisten Shadow** adalah aplikasi catatan pribadi berbasis terminal dengan sistem enkripsi yang membantu Anda menyimpan catatan dengan aman. Aplikasi ini dilengkapi dengan fitur kunci pribadi untuk catatan sensitif, pencarian cerdas, dan sistem manajemen pengguna yang robust.

## ✨ Fitur

### 🔐 Keamanan
- ✅ **Password Hashing** menggunakan SHA-256
- ✅ **Enkripsi Catatan** dengan Base64
- ✅ **Kunci Pribadi** untuk catatan sensitif
- ✅ **Validasi Input** yang ketat

### 📝 Manajemen Catatan
- ✅ Tambah, Edit, Hapus catatan
- ✅ Kunci/Unlock catatan
- ✅ Pencarian catatan dengan keyword
- ✅ Export catatan ke JSON
- ✅ Timestamp otomatis (created & updated)

### 📊 Analytics
- ✅ Statistik catatan (total, terkunci, terbuka)
- ✅ Riwayat login
- ✅ Info akun lengkap

### 🎨 User Experience
- ✅ Interface terminal yang clean
- ✅ Navigasi menu yang intuitif
- ✅ Pesan error yang jelas
- ✅ Konfirmasi untuk aksi penting

## 🚀 Instalasi

### Persyaratan
- Python 3.7 atau lebih baru
- pip (Python package manager)

### Langkah Instalasi

1. **Clone repository**
```bash
git clone https://github.com/suryadiarsyil-ops/asisten-shadow.git
cd asisten-shadow
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Jalankan aplikasi**
```bash
python src/main.py
```

### Instalasi dari Source

```bash
# Clone repository
git clone https://github.com/suryadiarsyil-ops/asisten-shadow.git
cd asisten-shadow

# Setup virtual environment (opsional tapi direkomendasikan)
python -m venv venv
source venv/bin/activate  # Linux/Mac
# atau
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Jalankan aplikasi
python src/main.py
```

## 💻 Penggunaan

### Quick Start

```bash
python src/main.py
```

### Menu Utama
```
==================================================
              ASISTEN SHADOW v2.0
==================================================
--------------------------------------------------
  1. Register
  2. Login
  3. Tentang Aplikasi
  4. Keluar
--------------------------------------------------
```

### Registrasi Pengguna
1. Pilih menu **Register**
2. Masukkan username (minimal 3 karakter)
3. Masukkan password (minimal 6 karakter)
4. Konfirmasi password

### Login & Dashboard
Setelah login, Anda akan melihat dashboard dengan menu:
- **Tambah Catatan** - Buat catatan baru
- **Lihat Semua Catatan** - Tampilkan daftar catatan
- **Buka Catatan** - Lihat isi catatan
- **Edit Catatan** - Ubah catatan yang ada
- **Hapus Catatan** - Hapus catatan
- **Cari Catatan** - Cari dengan keyword
- **Export Catatan** - Export ke JSON
- **Info Akun** - Lihat info akun & statistik

### Contoh Penggunaan

#### Membuat Catatan Terkunci
```
1. Pilih "Tambah Catatan"
2. Tulis catatan Anda
3. Masukkan kunci pribadi
4. Catatan akan tersimpan terenkripsi
```

#### Mencari Catatan
```
1. Pilih "Cari Catatan"
2. Masukkan keyword
3. Sistem akan menampilkan hasil pencarian
```

## 📁 Struktur Proyek

```
asisten-shadow/
│
├── src/
│   ├── main.py              # Entry point aplikasi
│   ├── user_manager.py      # Manajemen user
│   ├── notes_manager.py     # Manajemen catatan
│   ├── utils.py             # Helper functions
│   └── config.py            # Konfigurasi
│
├── tests/
│   ├── test_user.py         # Unit test user
│   ├── test_notes.py        # Unit test notes
│   └── test_utils.py        # Unit test utils
│
├── docs/
│   ├── API.md               # API Documentation
│   ├── SECURITY.md          # Security Guide
│   └── CONTRIBUTING.md      # Contribution Guide
│
├── data/
│   ├── users.json           # Database users (auto-generated)
│   └── notes.json           # Database notes (auto-generated)
│
├── .github/
│   └── workflows/
│       └── tests.yml        # GitHub Actions CI/CD
│
├── .gitignore               # Git ignore file
├── requirements.txt         # Python dependencies
├── setup.py                 # Package setup
├── LICENSE                  # MIT License
└── README.md               # This file
```

## 🔒 Keamanan

### Password Security
- Password di-hash menggunakan **SHA-256**
- Tidak ada plain text password yang disimpan
- Validasi strength password

### Data Encryption
- Catatan dienkripsi dengan **Base64**
- Kunci pribadi di-hash untuk keamanan ekstra
- Data sensitif tidak pernah di-log

### Best Practices
- ✅ Gunakan password yang kuat
- ✅ Jangan share kunci pribadi
- ✅ Backup data secara berkala
- ✅ Update aplikasi secara rutin

## 🧪 Testing

Jalankan unit tests:

```bash
# Jalankan semua tests
python -m pytest tests/

# Test dengan coverage
python -m pytest tests/ --cov=src

# Test spesifik
python -m pytest tests/test_user.py
```

## 📖 Dokumentasi

Dokumentasi lengkap tersedia di folder `docs/`:
- [API Documentation](docs/API.md)
- [Security Guide](docs/SECURITY.md)
- [Contributing Guide](docs/CONTRIBUTING.md)

## 🤝 Kontribusi

Kontribusi sangat diterima! Silakan baca [CONTRIBUTING.md](docs/CONTRIBUTING.md) untuk detail.

### Cara Berkontribusi
1. Fork repository
2. Buat branch fitur (`git checkout -b feature/AmazingFeature`)
3. Commit perubahan (`git commit -m 'Add some AmazingFeature'`)
4. Push ke branch (`git push origin feature/AmazingFeature`)
5. Buat Pull Request

## 🐛 Bug Report & Feature Request

Gunakan [GitHub Issues](https://github.com/suryadiarsyil-ops/asisten-shadow/issues) untuk:
- Melaporkan bug
- Mengajukan fitur baru
- Diskusi pengembangan

## 📝 Changelog

### Version 2.0.0 (Current)
- ✨ Refactoring struktur kode dengan OOP
- 🔒 Improved security dengan SHA-256
- 📊 Fitur statistik dan analytics
- 🔍 Pencarian catatan
- 💾 Export catatan
- 📱 UI/UX improvements

### Version 1.0.0
- 🎉 Initial release
- ✅ Basic CRUD operations
- 🔐 Basic encryption

## 📜 License

Proyek ini dilisensikan di bawah MIT License - lihat file [LICENSE](LICENSE) untuk detail.

## 👨‍💻 Author

**Asisten Shadow Team**
- GitHub: [@username](https://github.com/username)
- Email: contact@asistenshadow.com

## 🙏 Acknowledgments

- Terima kasih kepada semua kontributor
- Inspired by secure note-taking apps
- Built with ❤️ using Python

## 📞 Support

Butuh bantuan? Hubungi kami:
- 📧 Email: support@asistenshadow.com
- 💬 Discord: [Join our server](https://discord.gg/asistenshadow)
- 📖 Wiki: [Documentation](https://github.com/suryadiarsyil-ops/asisten-shadow/wiki)

---

<div align="center">

**⭐ Jika proyek ini membantu, berikan star ya! ⭐**

Made with ❤️ by Asisten Shadow Team

</div>
# asisten-shadow
# asisten-shadow
