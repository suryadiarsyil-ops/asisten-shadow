# Contributing to Asisten Shadow

Terima kasih atas minat Anda untuk berkontribusi pada Asisten Shadow! 🎉

## Code of Conduct

Dengan berpartisipasi dalam proyek ini, Anda diharapkan untuk menjunjung tinggi kode etik kami:
- Bersikap sopan dan menghormati semua kontributor
- Memberikan kritik yang konstruktif
- Fokus pada apa yang terbaik untuk komunitas

## Cara Berkontribusi

### Melaporkan Bug

Jika Anda menemukan bug, silakan buat issue dengan informasi berikut:
- Deskripsi bug yang jelas
- Langkah-langkah untuk mereproduksi bug
- Hasil yang diharapkan vs hasil aktual
- Screenshot (jika memungkinkan)
- Versi Python dan sistem operasi Anda

### Mengajukan Fitur Baru

Untuk mengajukan fitur baru:
1. Cek apakah fitur sudah pernah diajukan di Issues
2. Buat issue baru dengan label "enhancement"
3. Jelaskan fitur dengan detail
4. Berikan use case dan contoh

### Pull Request Process

1. **Fork Repository**
   ```bash
   git clone https://github.com/suryadiarsyil-ops/asisten-shadow.git
   cd asisten-shadow
   ```

2. **Buat Branch Baru**
   ```bash
   git checkout -b feature/nama-fitur
   # atau
   git checkout -b fix/nama-bug
   ```

3. **Buat Perubahan**
   - Tulis kode yang clean dan terdokumentasi
   - Ikuti style guide Python (PEP 8)
   - Tambahkan docstrings untuk fungsi/class baru
   - Update README.md jika diperlukan

4. **Testing**
   ```bash
   # Jalankan tests
   pytest tests/
   
   # Check coverage
   pytest tests/ --cov=src
   
   # Linting
   flake8 src/
   pylint src/
   ```

5. **Commit Changes**
   ```bash
   git add .
   git commit -m "feat: menambahkan fitur X"
   # atau
   git commit -m "fix: memperbaiki bug Y"
   ```

   Gunakan konvensi commit:
   - `feat:` untuk fitur baru
   - `fix:` untuk bug fix
   - `docs:` untuk perubahan dokumentasi
   - `style:` untuk perubahan formatting
   - `refactor:` untuk refactoring kode
   - `test:` untuk menambah tests
   - `chore:` untuk maintenance

6. **Push ke GitHub**
   ```bash
   git push origin feature/nama-fitur
   ```

7. **Buat Pull Request**
   - Buka repository di GitHub
   - Klik "New Pull Request"
   - Pilih branch Anda
   - Isi deskripsi PR dengan detail
   - Link ke issue terkait (jika ada)

## Style Guide

### Python Code Style

Ikuti PEP 8 dengan beberapa tambahan:

```python
# Good
def calculate_statistics(notes: List[Dict]) -> Dict:
    """
    Calculate statistics from notes.
    
    Args:
        notes: List of note dictionaries
        
    Returns:
        Dictionary containing statistics
    """
    total = len(notes)
    locked = sum(1 for note in notes if note["is_locked"])
    
    return {
        "total": total,
        "locked": locked
    }


# Bad
def calc_stats(n):
    t = len(n)
    l = sum(1 for x in n if x["is_locked"])
    return {"total": t, "locked": l}
```

### Dokumentasi

- Semua fungsi publik harus memiliki docstring
- Gunakan type hints
- Tambahkan komentar untuk logika yang kompleks

```python
def process_note(note: Dict, key: Optional[str] = None) -> Tuple[bool, str]:
    """
    Process a note with optional key verification.
    
    Args:
        note: Dictionary containing note data
        key: Optional key for locked notes
        
    Returns:
        Tuple of (success: bool, message: str)
        
    Raises:
        ValueError: If note format is invalid
    """
    # Implementation here
    pass
```

### Testing

Setiap fitur baru harus disertai dengan unit test:

```python
def test_add_note():
    """Test adding a new note"""
    manager = NotesManager()
    success, msg = manager.add_note("testuser", "Test content")
    
    assert success is True
    assert "berhasil" in msg.lower()
```

## Project Structure

```
asisten-shadow/
├── src/               # Source code
│   ├── main.py       # Entry point
│   ├── config.py     # Configuration
│   ├── utils.py      # Utilities
│   ├── user_manager.py
│   └── notes_manager.py
├── tests/            # Unit tests
├── docs/             # Documentation
├── data/             # Data storage
└── .github/          # GitHub configs
```

## Prioritas Kontribusi

Kami sangat menghargai kontribusi pada area berikut:

### High Priority
- 🐛 Bug fixes
- 🔒 Security improvements
- 📝 Documentation
- ✅ Unit tests

### Medium Priority
- ✨ New features
- 🎨 UI/UX improvements
- ⚡ Performance optimization

### Low Priority
- 🧹 Code refactoring
- 📊 Analytics features

## Development Setup

1. Install Python 3.7+
2. Setup virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt  # Dev dependencies
   ```

4. Run tests:
   ```bash
   pytest tests/ -v
   ```

## Questions?

Jika Anda memiliki pertanyaan:
- Buka issue dengan label "question"
- Email ke: contribute@asistenshadow.com
- Join Discord server kami

## Recognition

Kontributor akan disebutkan di:
- README.md (Contributors section)
- CHANGELOG.md
- Release notes

Terima kasih atas kontribusi Anda! 🙏
