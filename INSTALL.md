# Installation Guide

Panduan lengkap untuk menginstal dan menjalankan Asisten Shadow di berbagai platform.

## Table of Contents
- [Requirements](#requirements)
- [Quick Start](#quick-start)
- [Installation Methods](#installation-methods)
- [Platform-Specific Instructions](#platform-specific-instructions)
- [Troubleshooting](#troubleshooting)

## Requirements

### System Requirements
- **Operating System**: Windows 10+, macOS 10.14+, atau Linux
- **RAM**: Minimal 512 MB
- **Storage**: Minimal 50 MB free space
- **Internet**: Untuk download dependencies (one-time)

### Software Requirements
- **Python**: Version 3.7 atau lebih baru
- **pip**: Python package manager (biasanya sudah include dengan Python)
- **git**: (Opsional) Untuk clone repository

## Quick Start

### Option 1: Using Launcher Scripts (Recommended)

#### Linux/macOS
```bash
# Clone repository
git clone https://github.com/suryadiarsyil-ops/asisten-shadow.git
cd asisten-shadow

# Run launcher (will auto-setup everything)
./run.sh
```

#### Windows
```batch
# Clone repository
git clone https://github.com/suryadiarsyil-ops/asisten-shadow.git
cd asisten-shadow

# Run launcher (will auto-setup everything)
run.bat
```

### Option 2: Manual Setup

```bash
# 1. Clone repository
git clone https://github.com/suryadiarsyil-ops/asisten-shadow.git
cd asisten-shadow

# 2. Create virtual environment
python -m venv venv

# 3. Activate virtual environment
# Linux/macOS:
source venv/bin/activate
# Windows:
venv\Scripts\activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run application
python src/main.py
```

## Installation Methods

### Method 1: From GitHub (Development)

Untuk development atau ingin versi terbaru:

```bash
git clone https://github.com/suryadiarsyil-ops/asisten-shadow.git
cd asisten-shadow
pip install -e .
```

### Method 2: From PyPI (Stable)

⚠️ Coming soon!

```bash
pip install asisten-shadow
asisten-shadow
```

### Method 3: From ZIP/Tarball

1. Download release dari [GitHub Releases](https://github.com/suryadiarsyil-ops/asisten-shadow/releases)
2. Extract archive
3. Follow Manual Setup instructions

## Platform-Specific Instructions

### Windows

#### Prerequisites
1. **Install Python**
   - Download dari [python.org](https://www.python.org/downloads/)
   - ✅ Check "Add Python to PATH" saat instalasi
   - Verify: `python --version`

2. **Install Git** (Opsional)
   - Download dari [git-scm.com](https://git-scm.com/)

#### Installation Steps
```batch
# Open Command Prompt atau PowerShell

# Navigate to desired directory
cd C:\Users\YourName\Documents

# Clone repository
git clone https://github.com/suryadiarsyil-ops/asisten-shadow.git
cd asisten-shadow

# Run launcher
run.bat
```

#### Troubleshooting Windows
- **"Python not found"**: Pastikan Python sudah di PATH
- **"pip not found"**: Jalankan `python -m ensurepip`
- **Permission error**: Run Command Prompt as Administrator

### macOS

#### Prerequisites
1. **Install Homebrew** (Recommended)
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. **Install Python**
   ```bash
   brew install python3
   ```

3. **Install Git**
   ```bash
   brew install git
   ```

#### Installation Steps
```bash
# Open Terminal

# Navigate to desired directory
cd ~/Documents

# Clone repository
git clone https://github.com/suryadiarsyil-ops/asisten-shadow.git
cd asisten-shadow

# Make script executable (if not already)
chmod +x run.sh

# Run launcher
./run.sh
```

#### Troubleshooting macOS
- **"Permission denied"**: Run `chmod +x run.sh`
- **"Command not found"**: Check if Python is in PATH
- **SSL Certificate error**: Install certificates: `/Applications/Python 3.x/Install Certificates.command`

### Linux (Ubuntu/Debian)

#### Prerequisites
```bash
# Update package list
sudo apt update

# Install Python and pip
sudo apt install python3 python3-pip python3-venv

# Install Git
sudo apt install git
```

#### Installation Steps
```bash
# Navigate to desired directory
cd ~/Documents

# Clone repository
git clone https://github.com/suryadiarsyil-ops/asisten-shadow.git
cd asisten-shadow

# Make script executable
chmod +x run.sh

# Run launcher
./run.sh
```

#### Troubleshooting Linux
- **"python3-venv not found"**: `sudo apt install python3-venv`
- **"pip not found"**: `sudo apt install python3-pip`
- **Permission issues**: Don't use `sudo` with pip in venv

### Linux (Fedora/RHEL/CentOS)

#### Prerequisites
```bash
# Install Python and pip
sudo dnf install python3 python3-pip

# Install Git
sudo dnf install git
```

### Linux (Arch)

#### Prerequisites
```bash
# Install Python and pip
sudo pacman -S python python-pip

# Install Git
sudo pacman -S git
```

## Virtual Environment Setup

### Why Use Virtual Environment?
- Isolasi dependencies
- Tidak ada konflik dengan package system
- Mudah manage multiple Python projects

### Manual Virtual Environment

```bash
# Create venv
python -m venv venv

# Activate
# Linux/macOS:
source venv/bin/activate

# Windows CMD:
venv\Scripts\activate.bat

# Windows PowerShell:
venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Deactivate (when done)
deactivate
```

## Docker Installation (Advanced)

⚠️ Coming soon!

```bash
# Build image
docker build -t asisten-shadow .

# Run container
docker run -it -v $(pwd)/data:/app/data asisten-shadow
```

## Post-Installation

### First Run
1. Launch application: `./run.sh` or `run.bat`
2. Choose "Register" from menu
3. Create username and password
4. Start using!

### Configuration
- Data stored in: `data/` directory
- Config file: `src/config.py`
- Logs: (To be implemented)

### Updates

#### Automatic (Recommended)
```bash
cd asisten-shadow
git pull origin main
pip install -r requirements.txt --upgrade
```

#### Manual
1. Download latest release
2. Replace files (keep `data/` directory)
3. Run `pip install -r requirements.txt`

## Uninstallation

### Complete Removal
```bash
# 1. Backup your data (optional)
cp -r data ~/asisten-shadow-backup

# 2. Remove directory
cd ..
rm -rf asisten-shadow

# 3. Remove virtual environment (if created manually)
rm -rf venv
```

### Keep Data
```bash
# 1. Backup data
cp -r data ~/asisten-shadow-backup

# 2. Remove app but keep data
cd ..
rm -rf asisten-shadow
# (data backup is safe)
```

## Troubleshooting

### Common Issues

#### Issue: "Module not found"
**Solution:**
```bash
pip install -r requirements.txt
```

#### Issue: "Permission denied"
**Linux/macOS:**
```bash
chmod +x run.sh
```

**Windows:** Run as Administrator

#### Issue: "Python version too old"
**Solution:** Install Python 3.7+
```bash
# Check version
python --version

# Upgrade (varies by OS)
```

#### Issue: "pip not found"
**Solution:**
```bash
python -m ensurepip --upgrade
```

#### Issue: Virtual environment activation fails
**Windows PowerShell:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Getting Help

If you encounter issues:

1. **Check Documentation**: Read [README.md](README.md) and [FAQ](#)
2. **Search Issues**: [GitHub Issues](https://github.com/suryadiarsyil-ops/asisten-shadow/issues)
3. **Ask Community**: [Discord](#) or [Discussions](#)
4. **Report Bug**: Create new issue with:
   - OS and Python version
   - Error message
   - Steps to reproduce

## Development Setup

For contributors:

```bash
# Clone repository
git clone https://github.com/suryadiarsyil-ops/asisten-shadow.git
cd asisten-shadow

# Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dev dependencies
pip install -r requirements.txt
pip install pytest pytest-cov black flake8 pylint

# Run tests
pytest tests/

# Run linters
make lint

# Format code
make format
```

## Additional Resources

- [Official Documentation](https://github.com/suryadiarsyil-ops/asisten-shadow/wiki)
- [Video Tutorial](#) (Coming soon)
- [FAQ](https://github.com/suryadiarsyil-ops/asisten-shadow/wiki/FAQ)
- [Contributing Guide](CONTRIBUTING.md)

---

**Need more help?** Contact us at support@asistenshadow.com
