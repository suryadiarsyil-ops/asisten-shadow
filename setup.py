"""
Setup file for Asisten Shadow
"""

from setuptools import setup, find_packages
import os

# Read README for long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read requirements
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="asisten-shadow",
    version="2.0.0",
    author="Asisten Shadow Team",
    author_email="contact@asistenshadow.com",
    description="Aplikasi catatan pribadi terenkripsi dengan keamanan tingkat tinggi",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/suryadiarsyil-ops/asisten-shadow",
    project_urls={
        "Bug Tracker": "https://github.com/suryadiarsyil-ops/asisten-shadow/issues",
        "Documentation": "https://github.com/suryadiarsyil-ops/asisten-shadow/wiki",
        "Source Code": "https://github.com/suryadiarsyil-ops/asisten-shadow",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Office/Business",
        "Topic :: Security :: Cryptography",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "Natural Language :: Indonesian",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "asisten-shadow=src.main:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["README.md", "LICENSE", "requirements.txt"],
    },
    keywords="notes encryption security privacy terminal cli",
    zip_safe=False,
)
