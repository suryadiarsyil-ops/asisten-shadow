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

🔧 Konfigurasi Lanjutan
Ubah Port Server (jika 5000 dipakai)
# Edit server.py, baris terakhir:
> app.run(debug=True, port=8080)  # Ganti dengan port lain

Enable HTTPS (Opsional)
# Tambahkan ssl_context
> app.run(debug=True, port=5000, ssl_context='adhoc')

🛠️ Troubleshooting Termux

1. Port 5000 sudah digunakan:
#Cari proses yang pakai port 5000
> netstat -tulpn | grep :5000

#Atau kill semua proses Python
> pkill -f python

#Coba port lain
> python server.py --port 8080

2. Module tidak ditemukan:
#Update pip
> pip install --upgrade pip

#Install ulang dependensi
> pip uninstall flask flask-cors pyjwt -y
> pip install flask flask-cors pyjwt

3. Permission denied:
# Beri permission
chmod +x server.py
chmod 644 *.json

4. Database corrupt:
# Backup database
cp users.json users.json.backup
cp notes.json notes.json.backup

# Reset database
echo "{}" > users.json
echo "{}" > notes.json

📱 Tips Termux Pro
Jalankan di Background:

# Gunakan nohup
nohup python server.py &

# Cek log
tail -f nohup.out

#Stop server
pkill -f "python server.py"

Auto-start saat boot (root):

# Install termux-boot
pkg install termux-boot

# Buat script startup
mkdir -p ~/.termux/boot
echo 'cd ~/asisten-shadow && python server.py' > ~/.termux/boot/start-asisten
chmod +x ~/.termux/boot/start-asisten

Backup data ke Google Drive:

# Install rclone
pkg install rclone

# Konfigurasi rclone
rclone config

# Backup
rclone copy users.json drive:asisten-shadow-backup/
rclone copy notes.json drive:asisten-shadow-backup/

# Reset & Update:
cd ~
rm -rf asisten-shadow
git clone git@github.com:suryadiarsyil-ops/asisten-shadow.git
cd asisten-shadow
pip install flask flask-cors pyjwt
python server.py

