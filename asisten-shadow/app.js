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
        document.querySelectorAll('.menu
