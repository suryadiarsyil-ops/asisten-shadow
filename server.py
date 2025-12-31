from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os
import base64
import datetime
import jwt
import secrets
from functools import wraps

app = Flask(__name__)
CORS(app)

# Konfigurasi
app.config['SECRET_KEY'] = secrets.token_hex(32)
USER_FILE = "users.json"
NOTES_FILE = "notes.json"

# Helper functions
def load_data(filename):
    if not os.path.exists(filename):
        return {}
    with open(filename, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
            if isinstance(data, list):
                return {}
            return data
        except json.JSONDecodeError:
            return {}

def save_data(filename, data):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def encode_text(text):
    return base64.b64encode(text.encode()).decode()

def decode_text(text_b64):
    try:
        return base64.b64decode(text_b64.encode()).decode()
    except:
        return "[ERROR: data rusak]"

# Decorator untuk autentikasi
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        
        if 'Authorization' in request.headers:
            auth_header = request.headers['Authorization']
            if auth_header.startswith('Bearer '):
                token = auth_header.split(' ')[1]
        
        if not token:
            return jsonify({'error': 'Token tidak ditemukan!'}), 401
        
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = data['username']
        except:
            return jsonify({'error': 'Token tidak valid!'}), 401
        
        return f(current_user, *args, **kwargs)
    
    return decorated

# Routes
@app.route('/api/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        username = data.get('username', '').strip()
        password = data.get('password', '').strip()
        
        if not username or not password:
            return jsonify({'error': 'Username dan password harus diisi!'}), 400
        
        if len(password) < 6:
            return jsonify({'error': 'Password minimal 6 karakter!'}), 400
        
        users = load_data(USER_FILE)
        
        if username in users:
            return jsonify({'error': 'Username sudah terdaftar!'}), 400
        
        # Enkripsi password sebelum disimpan
        users[username] = encode_text(password)
        save_data(USER_FILE, users)
        
        # Buat folder notes untuk user
        notes = load_data(NOTES_FILE)
        if username not in notes:
            notes[username] = []
            save_data(NOTES_FILE, notes)
        
        return jsonify({'message': 'Registrasi berhasil!'}), 201
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        username = data.get('username', '').strip()
        password = data.get('password', '').strip()
        
        if not username or not password:
            return jsonify({'error': 'Username dan password harus diisi!'}), 400
        
        users = load_data(USER_FILE)
        
        if username not in users:
            return jsonify({'error': 'Username tidak ditemukan!'}), 401
        
        if users[username] != encode_text(password):
            return jsonify({'error': 'Password salah!'}), 401
        
        # Buat token JWT
        token = jwt.encode({
            'username': username,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
        }, app.config['SECRET_KEY'])
        
        return jsonify({
            'message': 'Login berhasil!',
            'token': token,
            'user': username
        }), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/verify', methods=['GET'])
@token_required
def verify(current_user):
    return jsonify({'user': current_user}), 200

@app.route('/api/notes', methods=['GET'])
@token_required
def get_notes(current_user):
    try:
        notes_data = load_data(NOTES_FILE)
        user_notes = notes_data.get(current_user, [])
        
        # Decode notes untuk frontend
        decoded_notes = []
        for note in user_notes:
            decoded_note = {
                'title': decode_text(note.get('title', '')) if note.get('title') else '',
                'content': decode_text(note.get('note', '')),
                'time': note.get('time', ''),
                'lock': bool(note.get('lock'))
            }
            decoded_notes.append(decoded_note)
        
        return jsonify(decoded_notes), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/notes', methods=['POST'])
@token_required
def add_note(current_user):
    try:
        data = request.get_json()
        title = data.get('title', '').strip()
        content = data.get('content', '').strip()
        password = data.get('password', '').strip()
        
        if not content:
            return jsonify({'error': 'Isi catatan tidak boleh kosong!'}), 400
        
        notes_data = load_data(NOTES_FILE)
        
        if current_user not in notes_data:
            notes_data[current_user] = []
        
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        new_note = {
            'title': encode_text(title) if title else '',
            'note': encode_text(content),
            'lock': encode_text(password) if password else '',
            'time': timestamp
        }
        
        notes_data[current_user].append(new_note)
        save_data(NOTES_FILE, notes_data)
        
        return jsonify({'message': 'Catatan berhasil ditambahkan!'}), 201
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/notes/<int:index>', methods=['PUT'])
@token_required
def update_note(current_user, index):
    try:
        data = request.get_json()
        title = data.get('title', '').strip()
        content = data.get('content', '').strip()
        password = data.get('password', '').strip()
        
        if not content:
            return jsonify({'error': 'Isi catatan tidak boleh kosong!'}), 400
        
        notes_data = load_data(NOTES_FILE)
        user_notes = notes_data.get(current_user, [])
        
        if index < 0 or index >= len(user_notes):
            return jsonify({'error': 'Catatan tidak ditemukan!'}), 404
        
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        user_notes[index]['title'] = encode_text(title) if title else ''
        user_notes[index]['note'] = encode_text(content)
        user_notes[index]['lock'] = encode_text(password) if password else ''
        user_notes[index]['time'] = timestamp
        
        save_data(NOTES_FILE, notes_data)
        
        return jsonify({'message': 'Catatan berhasil diupdate!'}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/notes/<int:index>/unlock', methods=['POST'])
@token_required
def unlock_note(current_user, index):
    try:
        data = request.get_json()
        password = data.get('password', '').strip()
        
        notes_data = load_data(NOTES_FILE)
        user_notes = notes_data.get(current_user, [])
        
        if index < 0 or index >= len(user_notes):
            return jsonify({'error': 'Catatan tidak ditemukan!'}), 404
        
        note = user_notes[index]
        
        if not note.get('lock'):
            return jsonify({'error': 'Catatan tidak terkunci!'}), 400
        
        if encode_text(password) != note['lock']:
            return jsonify({'error': 'Password salah!'}), 401
        
        # Return decrypted note
        decoded_note = {
            'title': decode_text(note.get('title', '')) if note.get('title') else '',
            'content': decode_text(note['note']),
            'time': note.get('time', ''),
            'lock': False  # Temporarily unlocked for viewing
        }
        
        return jsonify(decoded_note), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/notes/<int:index>', methods=['DELETE'])
@token_required
def delete_note(current_user, index):
    try:
        notes_data = load_data(NOTES_FILE)
        user_notes = notes_data.get(current_user, [])
        
        if index < 0 or index >= len(user_notes):
            return jsonify({'error': 'Catatan tidak ditemukan!'}), 404
        
        user_notes.pop(index)
        save_data(NOTES_FILE, notes_data)
        
        return jsonify({'message': 'Catatan berhasil dihapus!'}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Buat file JSON jika belum ada
    if not os.path.exists(USER_FILE):
        save_data(USER_FILE, {})
    
    if not os.path.exists(NOTES_FILE):
        save_data(NOTES_FILE, {})
    
    print("Server Asisten Shadow berjalan di http://localhost:5000")
    print("Buka http://localhost:5000 di browser")
    app.run(debug=True, port=5000)
