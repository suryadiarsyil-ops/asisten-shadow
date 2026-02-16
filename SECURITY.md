# Security Policy

## Supported Versions

Versi yang saat ini mendapatkan security updates:

| Version | Supported          |
| ------- | ------------------ |
| 2.0.x   | :white_check_mark: |
| 1.0.x   | :x:                |

## Security Features

### Current Implementation

#### Password Security
- **SHA-256 Hashing**: Semua password di-hash menggunakan SHA-256
- **No Plain Text Storage**: Password tidak pernah disimpan dalam bentuk plain text
- **Minimum Length**: Password minimal 6 karakter
- **Salt**: Setiap password menggunakan hash yang unik

#### Data Encryption
- **Base64 Encoding**: Konten catatan dienkripsi dengan Base64
- **Lock Keys**: Catatan sensitif dapat dikunci dengan kunci tambahan
- **Key Hashing**: Kunci catatan di-hash sebelum disimpan

#### Input Validation
- Validasi username (minimal 3 karakter, alphanumeric + underscore)
- Validasi password (minimal 6 karakter)
- Sanitasi input untuk mencegah injection attacks
- Error handling yang proper

### Security Limitations

⚠️ **Important**: Aplikasi ini menggunakan enkripsi sederhana (Base64) yang **BUKAN** enkripsi kriptografis yang kuat.

**Keterbatasan:**
- Base64 adalah encoding, bukan enkripsi sejati
- Data dapat di-decode dengan mudah jika file dicuri
- Tidak ada enkripsi end-to-end
- Tidak ada secure key storage
- File JSON dapat dibaca langsung

**Rekomendasi:**
- Jangan simpan informasi super sensitif (password bank, data kartu kredit)
- Gunakan password yang kuat
- Jaga keamanan file sistem Anda
- Pertimbangkan enkripsi disk level OS
- Backup data secara regular

## Reporting a Vulnerability

Jika Anda menemukan vulnerability keamanan, mohon **JANGAN** buat public issue di GitHub.

### Cara Melaporkan

1. **Email**: Kirim detail vulnerability ke security@asistenshadow.com
2. **Include**:
   - Deskripsi vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested fix (jika ada)

### Response Timeline

- **Initial Response**: Dalam 48 jam
- **Status Update**: Setiap 7 hari
- **Fix Timeline**: Tergantung severity
  - Critical: 1-7 hari
  - High: 7-14 hari
  - Medium: 14-30 hari
  - Low: 30-90 hari

### Disclosure Policy

- Koordinasikan disclosure dengan security team
- Tunggu patch dirilis sebelum public disclosure
- Credit akan diberikan kepada reporter (kecuali requested anonymous)

## Security Best Practices

### Untuk Users

#### Password Management
```
✅ DO:
- Gunakan password unik untuk Asisten Shadow
- Minimal 8-12 karakter
- Kombinasi huruf, angka, simbol
- Ganti password secara berkala

❌ DON'T:
- Gunakan password yang sama dengan akun lain
- Share password dengan orang lain
- Simpan password di plain text
- Gunakan password yang mudah ditebak
```

#### Data Storage
```
✅ DO:
- Backup data secara regular
- Enkripsi disk/folder tempat aplikasi
- Gunakan kunci yang kuat untuk catatan sensitif
- Logout setelah selesai menggunakan

❌ DON'T:
- Simpan data di shared computer tanpa proteksi
- Share file users.json atau notes.json
- Leave terminal open di public space
- Forget to lock your computer
```

### Untuk Developers

#### Code Security
```python
# ✅ Good: Input validation
def validate_username(username: str) -> bool:
    if not username or len(username) < 3:
        return False
    if not username.isalnum() and '_' not in username:
        return False
    return True

# ❌ Bad: No validation
def save_user(username: str, password: str):
    users[username] = password  # Direct save without checks
```

#### Secure Coding Practices
- Always validate and sanitize user input
- Use type hints for better code clarity
- Handle exceptions properly
- Don't log sensitive information
- Use secure random for tokens/keys
- Keep dependencies updated

## Security Checklist

### Pre-Deployment
- [ ] All tests passing
- [ ] No hardcoded credentials
- [ ] Input validation on all user inputs
- [ ] Error messages don't leak sensitive info
- [ ] Dependencies checked for vulnerabilities
- [ ] Code reviewed for security issues

### Post-Deployment
- [ ] Monitor for security issues
- [ ] Regular dependency updates
- [ ] Review user feedback for security concerns
- [ ] Keep security documentation updated

## Known Security Issues

### Current
None reported.

### Historical
None yet (new project).

## Planned Security Improvements

### Short Term (Next 3 months)
- [ ] Add AES-256 encryption
- [ ] Implement secure key derivation (PBKDF2)
- [ ] Add brute force protection
- [ ] Implement session management
- [ ] Add audit logging

### Long Term (Next 6-12 months)
- [ ] End-to-end encryption
- [ ] Two-factor authentication
- [ ] Biometric authentication
- [ ] Cloud sync with encryption
- [ ] Security audit by professional

## Resources

### Security References
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [Python Security Best Practices](https://python.readthedocs.io/en/stable/library/security_warnings.html)
- [CWE Top 25](https://cwe.mitre.org/top25/)

### Tools
- `safety check` - Check dependencies for vulnerabilities
- `bandit` - Python security linter
- `pip-audit` - Audit Python packages

### Contact
- Security Email: security@asistenshadow.com
- GPG Key: [To be added]
- Response Time: 48 hours

## Acknowledgments

Terima kasih kepada security researchers yang membantu meningkatkan keamanan Asisten Shadow:

- [None yet - be the first!]

---

Last Updated: January 15, 2024
Security Policy Version: 1.0
