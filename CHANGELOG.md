# Changelog

All notable changes to Asisten Shadow will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned
- Cloud sync functionality
- Mobile app version
- End-to-end encryption
- Multi-language support
- Dark mode for terminal

## [2.0.0] - 2024-01-15

### Added
- 🏗️ Complete code refactoring with OOP design
- 🔒 Enhanced security with SHA-256 password hashing
- 📊 Statistics and analytics dashboard
- 🔍 Advanced search functionality with keyword and tags
- 💾 Export notes to JSON format
- ⭐ Favorite notes feature
- 🏷️ Tags support for better organization
- 📝 Detailed note metadata (created_at, updated_at)
- 👤 User profile management
- 🔑 Change password functionality
- 🗑️ Delete account feature
- ✅ Comprehensive unit tests
- 📚 Complete documentation (README, CONTRIBUTING, etc)
- 🔄 GitHub Actions CI/CD pipeline
- 📦 Package setup for pip installation

### Changed
- Improved UI/UX with better formatting
- Better error handling and validation
- More descriptive status messages
- Enhanced code documentation with type hints
- Modular code structure (user_manager, notes_manager, utils)

### Fixed
- Data corruption issues
- Password validation bugs
- File handling errors
- Edge cases in note operations

### Security
- Upgraded password storage from Base64 to SHA-256
- Added input validation and sanitization
- Implemented secure key verification
- Added protection against common attacks

## [1.0.0] - 2023-12-01

### Added
- 🎉 Initial release
- Basic user registration and login
- Create, read, update, delete notes
- Lock notes with password
- Base64 encryption for note content
- Simple terminal interface
- JSON file storage

### Known Issues
- Limited security (Base64 encoding only)
- No search functionality
- Basic error handling
- Minimal code documentation

## Version History

| Version | Release Date | Major Changes |
|---------|-------------|---------------|
| 2.0.0   | 2024-01-15  | Complete rewrite with OOP, enhanced security |
| 1.0.0   | 2023-12-01  | Initial release with basic features |

## Migration Guide

### From 1.0.0 to 2.0.0

**Important:** Version 2.0.0 uses different password hashing. Existing users need to:

1. **Backup your data:**
   ```bash
   cp data/users.json data/users.json.backup
   cp data/notes.json data/notes.json.backup
   ```

2. **Clear old data and re-register:**
   ```bash
   rm data/users.json
   rm data/notes.json
   ```

3. **Run new version and register again**

**Note:** Direct migration script will be provided in future updates.

## Credits

### Contributors
- Main Developer: Asisten Shadow Team
- Security Audit: [Pending]
- Documentation: Community Contributors

### Special Thanks
- All beta testers
- Issue reporters
- Feature requesters
- Community supporters

## Links

- [GitHub Repository](https://github.com/suryadiarsyil-ops/asisten-shadow)
- [Issue Tracker](https://github.com/suryadiarsyil-ops/asisten-shadow/issues)
- [Documentation](https://github.com/suryadiarsyil-ops/asisten-shadow/wiki)
- [Release Notes](https://github.com/suryadiarsyil-ops/asisten-shadow/releases)

---

**Legend:**
- 🎉 New Feature
- 🔒 Security
- 🐛 Bug Fix
- 📝 Documentation
- ⚡ Performance
- 🔄 Refactoring
- 🗑️ Deprecated
- ❌ Removed
