@echo off
REM Asisten Shadow - Launcher Script for Windows
REM Version 2.0.0

echo =========================================
echo    Starting Asisten Shadow v2.0.0
echo =========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed!
    echo Please install Python 3.7 or higher from python.org
    pause
    exit /b 1
)

echo Python is installed
echo.

REM Check if virtual environment exists
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
    if errorlevel 1 (
        echo Failed to create virtual environment!
        pause
        exit /b 1
    )
    echo Virtual environment created
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Install/Update dependencies
if not exist "venv\.dependencies_installed" (
    echo.
    echo Installing dependencies...
    python -m pip install --upgrade pip --quiet
    pip install -r requirements.txt --quiet
    if errorlevel 1 (
        echo Failed to install dependencies!
        pause
        exit /b 1
    )
    type nul > venv\.dependencies_installed
    echo Dependencies installed successfully
) else (
    echo Dependencies already installed
)

REM Create data directory if it doesn't exist
if not exist "data" mkdir data

REM Run the application
echo.
echo Launching Asisten Shadow...
echo =========================================
echo.

cd src
python main.py

REM Deactivate virtual environment
cd ..
call venv\Scripts\deactivate.bat

echo.
echo =========================================
echo    Thank you for using Asisten Shadow!
echo =========================================
pause
