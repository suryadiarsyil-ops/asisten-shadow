#!/bin/bash

# Asisten Shadow - Launcher Script for Linux/Mac
# Version 2.0.0

echo "========================================="
echo "   Starting Asisten Shadow v2.0.0"
echo "========================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 is not installed!"
    echo "Please install Python 3.7 or higher."
    exit 1
fi

# Check Python version
PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
REQUIRED_VERSION="3.7"

if [ "$(printf '%s\n' "$REQUIRED_VERSION" "$PYTHON_VERSION" | sort -V | head -n1)" != "$REQUIRED_VERSION" ]; then
    echo "❌ Error: Python version $PYTHON_VERSION is too old!"
    echo "Please upgrade to Python 3.7 or higher."
    exit 1
fi

echo "✅ Python version: $PYTHON_VERSION"

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo ""
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
    
    if [ $? -ne 0 ]; then
        echo "❌ Failed to create virtual environment!"
        exit 1
    fi
    
    echo "✅ Virtual environment created"
fi

# Activate virtual environment
echo "🔄 Activating virtual environment..."
source venv/bin/activate

# Install/Update dependencies
if [ ! -f "venv/.dependencies_installed" ]; then
    echo ""
    echo "📥 Installing dependencies..."
    pip install -q --upgrade pip
    pip install -q -r requirements.txt
    
    if [ $? -eq 0 ]; then
        touch venv/.dependencies_installed
        echo "✅ Dependencies installed"
    else
        echo "❌ Failed to install dependencies!"
        exit 1
    fi
else
    echo "✅ Dependencies already installed"
fi

# Create data directory if it doesn't exist
mkdir -p data

# Run the application
echo ""
echo "🚀 Launching Asisten Shadow..."
echo "========================================="
echo ""

cd src
python main.py

# Deactivate virtual environment on exit
deactivate

echo ""
echo "========================================="
echo "   Thank you for using Asisten Shadow!"
echo "========================================="
