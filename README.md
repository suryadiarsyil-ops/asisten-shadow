# 📝 Asisten Shadow - Aplikasi Catatan Pribadi Terenkripsi
https://img.shields.io/github/repo-size/suryadiarsyil-ops/asisten-shadow
https://img.shields.io/github/license/suryadiarsyil-ops/asisten-shadow
https://img.shields.io/github/last-commit/suryadiarsyil-ops/asisten-shadow

Repository URL: git@github.com:suryadiarsyil-ops/asisten-shadow.git

📱 CARA MENJALANKAN DI TERMUX (ANDROID)
# Langkah 1: Persiapan Termux
bash
> pkg update && pkg upgrade -y
pkg install python python-pip git -y

# Langkah 2: Clone Repository
bash
> git clone git@github.com:suryadiarsyil-ops/asisten-shadow.git
cd asisten-shadow

# Langkah 3: Install Dependensi
bash
> pip install flask flask-cors pyjwt

# Langkah 4: Jalankan Server
bash
> python server.py

# Langkah 5: Akses Aplikasi
1. Di browser Termux:
   * Buka browser: termux-open-url http://localhost:5000

2. Di browser smartphone lain:
   * Cek IP Termux: ifconfig | grep inet
   * Buka: http://[IP_TERMUX]:5000

# Langkah 6: Untuk Akses Eksternal (Opsional)
Install ngrok
> pkg install wget -y
wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip
unzip ngrok-stable-linux-arm.zip

Daftar di ngrok.com untuk token gratis
> ./ngrok authtoken YOUR_TOKEN_HERE

Jalankan ngrok di terminal baru
> ./ngrok http 5000

# 💻 CARA MENJALANKAN DI KOMPUTER/LAPTOP
Windows:
Clone repository
> git clone git@github.com:suryadiarsyil-ops/asisten-shadow.git
cd asisten-shadow

* Install Python (jika belum)
* Download dari python.org
Install dependensi
> pip install flask flask-cors pyjwt

# Jalankan server
> python server.py
Buka browser: http://localhost:5000

# Linux/Mac:

#Clone repository
> git clone git@github.com:suryadiarsyil-ops/asisten-shadow.git
cd asisten-shadow

#Install Python3 dan pip
> sudo apt update
sudo apt install python3 python3-pip  #Ubuntu/Debian

#atau
> brew install python  #Mac

#Install dependensi
> pip3 install flask flask-cors pyjwt

#Jalankan server
> python3 server.py

#Buka browser: http://localhost:5000

