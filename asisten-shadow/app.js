class AsistenShadow {
    constructor() {
        this.currentUser = null;
        this.notes = [];
        this.apiUrl = 'http://localhost:5000/api';
        
        this.initializeElements();
        this.attachEventListeners();
        this.checkAuthStatus();
    }

    initializeElements() {
        // Authentication elements
        this.authSection = document.getElementById('authSection');
        this.appSection = document.getElementById('appSection');
        this.userInfo = document.getElementById('userInfo');
        this.usernameDisplay = document.getElementById('usernameDisplay');
        this.logoutBtn = document.getElementById('logoutBtn');
        
        // Forms
        this.loginForm = document.getElementById('loginForm');
        this.registerForm = document.getElementById('registerForm');
        this.loginTab = document.getElementById('loginTab');
        this.registerTab = document.getElementById('registerTab');
        this.loginBtn = document.getElementById('loginBtn');
        this.registerBtn = document.getElementById('registerBtn');
        
        // App elements
        this.sidebarUsername = document.getElementById('sidebarUsername');
        this.noteCount = document.getElementById('noteCount');
        this.notesGrid = document.getElementById('notesGrid');
        this.searchNotes = document.getElementById('searchNotes');
        
        // Modal
        this.modal = document.getElementById('noteModal');
        this.modalTitle = document.getElementById('modalTitle');
        this.modalContent = document.getElementById('noteModalContent');
        this.modalActions = document.getElementById('modalActions');
        
        // Loading
        this.loadingOverlay = document.getElementById('loadingOverlay');
    }

    attachEventListeners() {
        // Tab switching
        this.loginTab.addEventListener('click', () => this.switchTab('login'));
        this.registerTab.addEventListener('click', () => this.switchTab('register'));
        
        // Authentication
        this.loginBtn.addEventListener('click', () => this.login());
        this.registerBtn.addEventListener('click', () => this.register());
        this.logoutBtn.addEventListener('click', () => this.logout());
        
        // Modal
        document.querySelector('.close-modal').addEventListener('click', () => this.closeModal());
        this.modal.addEventListener('click', (e) => {
            if (e.target === this.modal) this.closeModal();
        });
        
        // Password visibility toggle
        document.querySelectorAll('.toggle-password').forEach(btn => {
            btn.addEventListener('click', (e) => {
                const input = e.target.closest('.form-group').querySelector('input');
                const icon = e.target.querySelector('i');
                if (input.type === 'password') {
                    input.type = 'text';
                    icon.classList.remove('fa-eye');
                    icon.classList.add('fa-eye-slash');
                } else {
                    input.type = 'password';
                    icon.classList.remove('fa-eye-slash');
                    icon.classList.add('fa-eye');
                }
            });
        });
        
        // Menu navigation
        document.querySelectorAll('.menu-btn').forEach(btn => {
            btn.addEventListener('click', (e) => {
                const section = e.target.dataset.section;
                this.switchSection(section);
            });
        });
        
        // Quick actions
        document.getElementById('quickAdd').addEventListener('click', () => {
            this.switchSection('add');
        });
        
        document.getElementById('viewAll').addEventListener('click', () => {
            this.switchSection('notes');
            this.loadNotes();
        });
        
        // Search
        this.searchNotes.addEventListener('input', (e) => this.searchNotesHandler(e.target.value));
    }

    async checkAuthStatus() {
        const token = localStorage.getItem('token');
        if (token) {
            try {
                const response = await fetch(`${this.apiUrl}/verify`, {
                    headers: { 'Authorization': `Bearer ${token}` }
                });
                
                if (response.ok) {
                    const data = await response.json();
                    this.currentUser = data.user;
                    this.showApp();
                    this.loadNotes();
                } else {
                    localStorage.removeItem('token');
                }
            } catch (error) {
                console.error('Auth check failed:', error);
            }
        }
    }

    switchTab(tab) {
        document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
        document.querySelectorAll('.form-container').forEach(form => form.classList.remove('active'));
        
        if (tab === 'login') {
            this.loginTab.classList.add('active');
            this.loginForm.classList.add('active');
        } else {
            this.registerTab.classList.add('active');
            this.registerForm.classList.add('active');
        }
    }

    async login() {
        const username = document.getElementById('loginUsername').value;
        const password = document.getElementById('loginPassword').value;
        
        if (!username || !password) {
            this.showMessage('loginMessage', 'Username dan password harus diisi!', 'error');
            return;
        }
        
        this.showLoading();
        
        try {
            const response = await fetch(`${this.apiUrl}/login`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ username, password })
            });
            
            const data = await response.json();
            
            if (response.ok) {
                localStorage.setItem('token', data.token);
                this.currentUser = username;
                this.showApp();
                this.loadNotes();
                this.showMessage('loginMessage', 'Login berhasil!', 'success');
            } else {
                this.showMessage('loginMessage', data.error || 'Login gagal!', 'error');
            }
        } catch (error) {
            this.showMessage('loginMessage', 'Terjadi kesalahan!', 'error');
        } finally {
            this.hideLoading();
        }
    }

    async register() {
        const username = document.getElementById('registerUsername').value;
        const password = document.getElementById('registerPassword').value;
        const confirmPassword = document.getElementById('confirmPassword').value;
        
        if (!username || !password || !confirmPassword) {
            this.showMessage('registerMessage', 'Semua field harus diisi!', 'error');
            return;
        }
        
        if (password !== confirmPassword) {
            this.showMessage('registerMessage', 'Password tidak cocok!', 'error');
            return;
        }
        
        if (password.length < 6) {
            this.showMessage('registerMessage', 'Password minimal 6 karakter!', 'error');
            return;
        }
        
        this.showLoading();
        
        try {
            const response = await fetch(`${this.apiUrl}/register`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ username, password })
            });
            
            const data = await response.json();
            
            if (response.ok) {
                this.showMessage('registerMessage', 'Registrasi berhasil! Silakan login.', 'success');
                this.switchTab('login');
                document.getElementById('loginUsername').value = username;
                document.getElementById('registerUsername').value = '';
                document.getElementById('registerPassword').value = '';
                document.getElementById('confirmPassword').value = '';
            } else {
                this.showMessage('registerMessage', data.error || 'Registrasi gagal!', 'error');
            }
        } catch (error) {
            this.showMessage('registerMessage', 'Terjadi kesalahan!', 'error');
        } finally {
            this.hideLoading();
        }
    }

    logout() {
        localStorage.removeItem('token');
        this.currentUser = null;
        this.showAuth();
    }

    showAuth() {
        this.authSection.style.display = 'block';
        this.appSection.style.display = 'none';
        this.userInfo.style.display = 'none';
    }

    showApp() {
        this.authSection.style.display = 'none';
        this.appSection.style.display = 'flex';
        this.userInfo.style.display = 'flex';
        this.usernameDisplay.textContent = this.currentUser;
        this.sidebarUsername.textContent = this.currentUser;
    }

    switchSection(section) {
        document.querySelectorAll('.content-section').forEach(sec => sec.classList.remove('active'));
        document.querySelectorAll('.menu-btn').forEach(btn => btn.classList.remove('active'));
        
        document.getElementById(`${section}Section`).classList.add('active');
        document.querySelector(`[data-section="${section}"]`).classList.add('active');
        
        if (section === 'notes') {
            this.loadNotes();
        } else if (section === 'stats') {
            this.loadStats();
        } else if (section === 'locked') {
            this.loadLockedNotes();
        }
    }

    async loadNotes() {
        if (!this.currentUser) return;
        
        this.showLoading();
        
        try {
            const token = localStorage.getItem('token');
            const response = await fetch(`${this.apiUrl}/notes`, {
                headers: { 'Authorization': `Bearer ${token}` }
            });
            
            if (response.ok) {
                this.notes = await response.json();
                this.renderNotes();
                this.updateNoteCount();
            }
        } catch (error) {
            console.error('Failed to load notes:', error);
        } finally {
            this.hideLoading();
        }
    }

    renderNotes(filteredNotes = null) {
        const notesToRender = filteredNotes || this.notes;
        
        if (notesToRender.length === 0) {
            this.notesGrid.innerHTML = `
                <div class="empty-state">
                    <i class="fas fa-clipboard"></i>
                    <h3>Belum ada catatan</h3>
                    <p>Mulai dengan menambahkan catatan pertama Anda</p>
                </div>
            `;
            return;
        }
        
        this.notesGrid.innerHTML = notesToRender.map((note, index) => `
            <div class="note-card ${note.lock ? 'locked' : ''}">
                <div class="note-header">
                    <div class="note-title">${note.title || 'Catatan Tanpa Judul'}</div>
                    <div class="note-actions">
                        <button class="note-action-btn" onclick="app.viewNote(${index})">
                            <i class="fas fa-eye"></i>
                        </button>
                        ${note.lock ? `
                            <button class="note-action-btn" onclick="app.unlockNote(${index})">
                                <i class="fas fa-unlock"></i>
                            </button>
                        ` : `
                            <button class="note-action-btn" onclick="app.editNote(${index})">
                                <i class="fas fa-edit"></i>
                            </button>
                            <button class="note-action-btn" onclick="app.deleteNote(${index})">
                                <i class="fas fa-trash"></i>
                            </button>
                        `}
                    </div>
                </div>
                <div class="note-content">
                    ${note.content.length > 150 ? note.content.substring(0, 150) + '...' : note.content}
                </div>
                <div class="note-footer">
                    <div class="note-time">
                        <i class="far fa-clock"></i>
                        ${new Date(note.time).toLocaleString('id-ID')}
                    </div>
                    ${note.lock ? '<i class="fas fa-lock"></i>' : '<i class="fas fa-unlock"></i>'}
                </div>
            </div>
        `).join('');
    }

    searchNotesHandler(query) {
        if (!query) {
            this.renderNotes();
            return;
        }
        
        const filtered = this.notes.filter(note => 
            note.content.toLowerCase().includes(query.toLowerCase()) ||
            (note.title && note.title.toLowerCase().includes(query.toLowerCase()))
        );
        
        this.renderNotes(filtered);
    }

    updateNoteCount() {
        const total = this.notes.length;
        const locked = this.notes.filter(n => n.lock).length;
        const unlocked = total - locked;
        
        this.noteCount.textContent = `${total} catatan`;
        
        if (document.getElementById('totalNotes')) {
            document.getElementById('totalNotes').textContent = total;
            document.getElementById('lockedNotes').textContent = locked;
            document.getElementById('unlockedNotes').textContent = unlocked;
        }
    }

    async addNote(title, content, password = '') {
        this.showLoading();
        
        try {
            const token = localStorage.getItem('token');
            const response = await fetch(`${this.apiUrl}/notes`, {
                method: 'POST',
                headers: {
                    'Authorization': `Bearer ${token}`,
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    title,
                    content,
                    password
                })
            });
            
            if (response.ok) {
                await this.loadNotes();
                this.switchSection('notes');
                this.showMessage('global', 'Catatan berhasil ditambahkan!', 'success');
            }
        } catch (error) {
            console.error('Failed to add note:', error);
        } finally {
            this.hideLoading();
        }
    }

    viewNote(index) {
        const note = this.notes[index];
        
        if (note.lock) {
            this.promptUnlock(note, index);
            return;
        }
        
        this.modalTitle.textContent = note.title || 'Catatan';
        this.modalContent.innerHTML = `
            <div class="note-view">
                <p>${note.content.replace(/\n/g, '<br>')}</p>
                <div class="note-meta">
                    <small><i class="far fa-clock"></i> ${new Date(note.time).toLocaleString('id-ID')}</small>
                </div>
            </div>
        `;
        
        this.modalActions.innerHTML = `
            <button class="btn-secondary" onclick="app.closeModal()">
                <i class="fas fa-times"></i> Tutup
            </button>
            <button class="btn-primary" onclick="app.editNote(${index})">
                <i class="fas fa-edit"></i> Edit
            </button>
        `;
        
        this.modal.classList.add('active');
    }

    promptUnlock(note, index) {
        this.modalTitle.textContent = '🔒 Catatan Terkunci';
        this.modalContent.innerHTML = `
            <p>Catatan ini dilindungi dengan password.</p>
            <div class="unlock-form">
                <input type="password" id="unlockPasswordInput" placeholder="Masukkan password">
            </div>
        `;
        
        this.modalActions.innerHTML = `
            <button class="btn-secondary" onclick="app.closeModal()">
                <i class="fas fa-times"></i> Batal
            </button>
            <button class="btn-primary" onclick="app.attemptUnlock(${index})">
                <i class="fas fa-unlock"></i> Buka
            </button>
        `;
        
        this.modal.classList.add('active');
    }

    async attemptUnlock(index) {
        const password = document.getElementById('unlockPasswordInput').value;
        const note = this.notes[index];
        
        this.showLoading();
        
        try {
            const token = localStorage.getItem('token');
            const response = await fetch(`${this.apiUrl}/notes/${index}/unlock`, {
                method: 'POST',
                headers: {
                    'Authorization': `Bearer ${token}`,
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ password })
            });
            
            if (response.ok) {
                const unlockedNote = await response.json();
                this.notes[index] = unlockedNote;
                this.closeModal();
                this.viewNote(index);
            } else {
                this.showMessage('modal', 'Password salah!', 'error');
            }
        } catch (error) {
            console.error('Failed to unlock note:', error);
        } finally {
            this.hideLoading();
        }
    }

    editNote(index) {
        const note = this.notes[index];
        
        this.modalTitle.textContent = 'Edit Catatan';
        this.modalContent.innerHTML = `
            <div class="edit-form">
                <div class="form-group">
                    <label>Judul</label>
                    <input type="text" id="editTitle" value="${note.title || ''}">
                </div>
                <div class="form-group">
                    <label>Isi Catatan</label>
                    <textarea id="editContent" rows="8">${note.content}</textarea>
                </div>
                <div class="form-group">
                    <label class="checkbox-label">
                        <input type="checkbox" id="editLock" ${note.lock ? 'checked' : ''}>
                        <i class="fas fa-lock"></i> Kunci Catatan
                    </label>
                    <div id="editLockOptions" style="display: ${note.lock ? 'block' : 'none'}">
                        <input type="password" id="editPassword" placeholder="Password baru">
                        <input type="password" id="editConfirmPassword" placeholder="Konfirmasi password">
                    </div>
                </div>
            </div>
        `;
        
        this.modalActions.innerHTML = `
            <button class="btn-secondary" onclick="app.closeModal()">
                <i class="fas fa-times"></i> Batal
            </button>
            <button class="btn-primary" onclick="app.saveEdit(${index})">
                <i class="fas fa-save"></i> Simpan
            </button>
        `;
        
        this.modal.classList.add('active');
        
        // Show/hide lock options
        document.getElementById('editLock').addEventListener('change', (e) => {
            document.getElementById('editLockOptions').style.display = 
                e.target.checked ? 'block' : 'none';
        });
    }

    async saveEdit(index) {
        const title = document.getElementById('editTitle').value;
        const content = document.getElementById('editContent').value;
        const lock = document.getElementById('editLock').checked;
        const password = lock ? document.getElementById('editPassword').value : '';
        
        if (!content.trim()) {
            this.showMessage('modal', 'Isi catatan tidak boleh kosong!', 'error');
            return;
        }
        
        if (lock && password.length < 4) {
            this.showMessage('modal', 'Password minimal 4 karakter!', 'error');
            return;
        }
        
        this.showLoading();
        
        try {
            const token = localStorage.getItem('token');
            const response = await fetch(`${this.apiUrl}/notes/${index}`, {
                method: 'PUT',
                headers: {
                    'Authorization': `Bearer ${token}`,
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    title,
                    content,
                    password: lock ? password : ''
                })
            });
            
            if (response.ok) {
                await this.loadNotes();
                this.closeModal();
                this.showMessage('global', 'Catatan berhasil diedit!', 'success');
            }
        } catch (error) {
            console.error('Failed to edit note:', error);
        } finally {
            this.hideLoading();
        }
    }

    async deleteNote(index) {
        if (!confirm('Yakin ingin menghapus catatan ini?')) return;
        
        this.showLoading();
        
        try {
            const token = localStorage.getItem('token');
            const response = await fetch(`${this.apiUrl}/notes/${index}`, {
                method: 'DELETE',
                headers: { 'Authorization': `Bearer ${token}` }
            });
            
            if (response.ok) {
                await this.loadNotes();
                this.showMessage('global', 'Catatan berhasil dihapus!', 'success');
            }
        } catch (error) {
            console.error('Failed to delete note:', error);
        } finally {
            this.hideLoading();
        }
    }

    closeModal() {
        this.modal.classList.remove('active');
    }

    showMessage(elementId, message, type) {
        const element = document.getElementById(elementId);
        if (element) {
            element.textContent = message;
            element.className = `auth-message ${type}`;
            element.style.display = 'block';
            
            setTimeout(() => {
                element.style.display = 'none';
            }, 3000);
        }
    }

    showLoading() {
        this.loadingOverlay.classList.add('active');
    }

    hideLoading() {
        this.loadingOverlay.classList.remove('active');
    }

    async loadStats() {
        const total = this.notes.length;
        const locked = this.notes.filter(n => n.lock).length;
        const unlocked = total - locked;
        
        document.getElementById('totalNotes').textContent = total;
        document.getElementById('lockedNotes').textContent = locked;
        document.getElementById('unlockedNotes').textContent = unlocked;
        
        const now = new Date();
        const options = { 
            weekday: 'long', 
            year: 'numeric', 
            month: 'long', 
            day: 'numeric',
            hour: '2-digit',
            minute: '2-digit'
        };
        document.getElementById('lastActivity').textContent = 
            now.toLocaleDateString('id-ID', options);
        
        // Load recent activity
        const activityList = document.getElementById('activityList');
        const activities = this.notes
            .sort((a, b) => new Date(b.time) - new Date(a.time))
            .slice(0, 5)
            .map(note => ({
                type: note.lock ? 'lock' : 'create',
                time: note.time,
                content: note.title || note.content.substring(0, 50) + '...'
            }));
        
        activityList.innerHTML = activities.map(act => `
            <div class="activity-item">
                <div class="activity-icon">
                    <i class="fas fa-${act.type === 'lock' ? 'lock' : 'sticky-note'}"></i>
                </div>
                <div class="activity-details">
                    <p>${act.type === 'lock' ? 'Mengunci catatan' : 'Membuat catatan'}: ${act.content}</p>
                    <div class="activity-time">
                        ${new Date(act.time).toLocaleString('id-ID')}
                    </div>
                </div>
            </div>
        `).join('');
    }

    async loadLockedNotes() {
        const lockedNotes = this.notes.filter(note => note.lock);
        const lockedList = document.getElementById('lockedNotesList');
        
        if (lockedNotes.length === 0) {
            lockedList.innerHTML = `
                <div class="empty-state">
                    <i class="fas fa-lock-open"></i>
                    <h3>Tidak ada catatan terkunci</h3>
                    <p>Semua catatan Anda terbuka</p>
                </div>
            `;
            return;
        }
        
        lockedList.innerHTML = lockedNotes.map((note, index) => `
            <div class="note-card locked">
                <div class="note-header">
                    <div class="note-title">${note.title || 'Catatan Terkunci'}</div>
                    <button class="note-action-btn" onclick="app.promptUnlock(app.notes.findIndex(n => n.time === '${note.time}'))">
                        <i class="fas fa-unlock"></i> Buka
                    </button>
                </div>
                <div class="note-content">
                    🔒 Konten dilindungi password
                </div>
                <div class="note-footer">
                    <div class="note-time">
                        <i class="far fa-clock"></i>
                        ${new Date(note.time).toLocaleDateString('id-ID')}
                    </div>
                    <i class="fas fa-lock"></i>
                </div>
            </div>
        `).join('');
    }
}

// Initialize the app when page loads
window.addEventListener('DOMContentLoaded', () => {
    window.app = new AsistenShadow();
});
