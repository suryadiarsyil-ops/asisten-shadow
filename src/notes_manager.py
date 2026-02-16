"""
Notes Management Module for Asisten Shadow
"""
from src.utils import truncate_text
from typing import Dict, List, Optional, Tuple
from utils import (
    load_data, save_data, hash_password, encode_text, 
    decode_text, get_timestamp, truncate_text
)
from config import NOTES_FILE, MAX_PREVIEW_LENGTH, MESSAGES


class NotesManager:
    """Class untuk mengelola catatan pengguna"""
    
    def __init__(self, notes_file: str = NOTES_FILE):
        """
        Inisialisasi NotesManager
        
        Args:
            notes_file: Path ke file database notes
        """
        self.notes_file = notes_file
    
    def add_note(self, username: str, content: str, lock_key: str = "", 
                 tags: List[str] = None) -> tuple[bool, str]:
        """
        Menambahkan catatan baru
        
        Args:
            username: Username pemilik catatan
            content: Isi catatan
            lock_key: Kunci untuk mengunci catatan (opsional)
            tags: List tag untuk catatan (opsional)
            
        Returns:
            Tuple (success: bool, message: str)
        """
        if not content:
            return False, "❌ Catatan tidak boleh kosong!"
        
        notes = load_data(self.notes_file)
        
        if username not in notes:
            notes[username] = []
        
        note_data = {
            "id": len(notes[username]) + 1,
            "content": encode_text(content),
            "lock": hash_password(lock_key) if lock_key else "",
            "is_locked": bool(lock_key),
            "created_at": get_timestamp(),
            "updated_at": get_timestamp(),
            "tags": tags or [],
            "favorite": False
        }
        
        notes[username].append(note_data)
        
        if save_data(self.notes_file, notes):
            return True, MESSAGES["note_added"]
        
        return False, MESSAGES["save_failed"]
    
    def get_notes(self, username: str, include_locked: bool = True) -> List[Dict]:
        """
        Mendapatkan semua catatan pengguna
        
        Args:
            username: Username pemilik catatan
            include_locked: Apakah catatan terkunci disertakan
            
        Returns:
            List catatan
        """
        notes = load_data(self.notes_file)
        user_notes = notes.get(username, [])
        
        if not include_locked:
            return [note for note in user_notes if not note["is_locked"]]
        
        return user_notes
    
    def get_note_by_index(self, username: str, index: int) -> Optional[Dict]:
        """
        Mendapatkan catatan berdasarkan index
        
        Args:
            username: Username pemilik catatan
            index: Index catatan (0-based)
            
        Returns:
            Dictionary catatan atau None
        """
        notes = self.get_notes(username)
        
        if 0 <= index < len(notes):
            return notes[index]
        
        return None
    
    def display_notes_list(self, username: str, show_locked: bool = True) -> List[Dict]:
        """
        Menampilkan daftar catatan dengan format tabel
        
        Args:
            username: Username pemilik catatan
            show_locked: Apakah menampilkan catatan terkunci
            
        Returns:
            List catatan
        """
        notes = self.get_notes(username, include_locked=show_locked)
        
        if not notes:
            print(f"\n{MESSAGES['no_notes']}")
            return []
        
        print("\n" + "="*80)
        print(f"{'No':<5} {'Status':<10} {'Preview':<35} {'Tags':<15} {'Updated':<15}")
        print("-"*80)
        
        for i, note in enumerate(notes, 1):
            status = "🔒 Locked" if note["is_locked"] else "🔓 Open"
            favorite = "⭐" if note.get("favorite", False) else ""
            
            content = decode_text(note["content"])
            preview = truncate_text(content, MAX_PREVIEW_LENGTH)
            
            if note["is_locked"]:
                preview = "[Catatan Terkunci]"
            
            tags_str = ", ".join(note.get("tags", [])[:2])
            if len(note.get("tags", [])) > 2:
                tags_str += "..."
            
            updated = note["updated_at"][:16]  # YYYY-MM-DD HH:MM
            
            print(f"{i:<5} {status:<10} {preview:<35} {tags_str:<15} {updated:<15} {favorite}")
        
        print("-"*80)
        print(f"Total: {len(notes)} catatan\n")
        return notes
    
    def view_note(self, username: str, index: int, key: str = None) -> tuple[bool, Optional[str]]:
        """
        Melihat isi catatan
        
        Args:
            username: Username pemilik catatan
            index: Index catatan
            key: Kunci untuk membuka catatan terkunci
            
        Returns:
            Tuple (success: bool, content: str atau None)
        """
        note = self.get_note_by_index(username, index)
        
        if not note:
            return False, MESSAGES["invalid_note_number"]
        
        # Check if note is locked
        if note["is_locked"]:
            if key is None:
                return False, "🔑 Catatan terkunci! Masukkan kunci."
            
            if hash_password(key) != note["lock"]:
                return False, MESSAGES["wrong_key"]
        
        content = decode_text(note["content"])
        return True, content
    
    def edit_note(self, username: str, index: int, new_content: str = None, 
                  new_lock: Optional[str] = None, tags: List[str] = None,
                  key: str = None) -> tuple[bool, str]:
        """
        Mengedit catatan
        
        Args:
            username: Username pemilik catatan
            index: Index catatan
            new_content: Isi catatan baru (opsional)
            new_lock: Kunci baru (opsional)
            tags: Tag baru (opsional)
            key: Kunci untuk membuka catatan terkunci
            
        Returns:
            Tuple (success: bool, message: str)
        """
        notes = load_data(self.notes_file)
        user_notes = notes.get(username, [])
        
        if not 0 <= index < len(user_notes):
            return False, MESSAGES["invalid_note_number"]
        
        note = user_notes[index]
        
        # Verify key if note is locked
        if note["is_locked"]:
            if key is None:
                return False, "🔑 Masukkan kunci untuk mengedit catatan!"
            
            if hash_password(key) != note["lock"]:
                return False, MESSAGES["wrong_key"]
        
        # Update content
        if new_content is not None:
            note["content"] = encode_text(new_content)
            note["updated_at"] = get_timestamp()
        
        # Update lock
        if new_lock is not None:
            if new_lock == "":
                note["lock"] = ""
                note["is_locked"] = False
            else:
                note["lock"] = hash_password(new_lock)
                note["is_locked"] = True
        
        # Update tags
        if tags is not None:
            note["tags"] = tags
        
        if save_data(self.notes_file, notes):
            return True, MESSAGES["note_edited"]
        
        return False, MESSAGES["save_failed"]
    
    def delete_note(self, username: str, index: int, key: str = None) -> tuple[bool, str]:
        """
        Menghapus catatan
        
        Args:
            username: Username pemilik catatan
            index: Index catatan
            key: Kunci untuk menghapus catatan terkunci
            
        Returns:
            Tuple (success: bool, message: str)
        """
        notes = load_data(self.notes_file)
        user_notes = notes.get(username, [])
        
        if not 0 <= index < len(user_notes):
            return False, MESSAGES["invalid_note_number"]
        
        note = user_notes[index]
        
        # Verify key if locked
        if note["is_locked"]:
            if key is None:
                return False, "🔑 Masukkan kunci untuk menghapus catatan!"
            
            if hash_password(key) != note["lock"]:
                return False, MESSAGES["wrong_key"]
        
        # Delete note
        del user_notes[index]
        
        if save_data(self.notes_file, notes):
            return True, MESSAGES["note_deleted"]
        
        return False, MESSAGES["save_failed"]
    
    def search_notes(self, username: str, keyword: str, 
                     search_tags: bool = False) -> List[Tuple[int, Dict]]:
        """
        Mencari catatan berdasarkan keyword
        
        Args:
            username: Username pemilik catatan
            keyword: Kata kunci pencarian
            search_tags: Apakah mencari di tags juga
            
        Returns:
            List tuple (index, note)
        """
        notes = self.get_notes(username)
        results = []
        
        keyword_lower = keyword.lower()
        
        for i, note in enumerate(notes):
            # Skip locked notes
            if note["is_locked"]:
                continue
            
            # Search in content
            content = decode_text(note["content"]).lower()
            if keyword_lower in content:
                results.append((i, note))
                continue
            
            # Search in tags if enabled
            if search_tags:
                tags = [tag.lower() for tag in note.get("tags", [])]
                if any(keyword_lower in tag for tag in tags):
                    results.append((i, note))
        
        return results
    
    def get_notes_by_tag(self, username: str, tag: str) -> List[Tuple[int, Dict]]:
        """
        Mendapatkan catatan berdasarkan tag
        
        Args:
            username: Username pemilik catatan
            tag: Tag yang dicari
            
        Returns:
            List tuple (index, note)
        """
        notes = self.get_notes(username)
        results = []
        
        tag_lower = tag.lower()
        
        for i, note in enumerate(notes):
            if note["is_locked"]:
                continue
            
            tags = [t.lower() for t in note.get("tags", [])]
            if tag_lower in tags:
                results.append((i, note))
        
        return results
    
    def toggle_favorite(self, username: str, index: int) -> tuple[bool, str]:
        """
        Toggle status favorite catatan
        
        Args:
            username: Username pemilik catatan
            index: Index catatan
            
        Returns:
            Tuple (success: bool, message: str)
        """
        notes = load_data(self.notes_file)
        user_notes = notes.get(username, [])
        
        if not 0 <= index < len(user_notes):
            return False, MESSAGES["invalid_note_number"]
        
        note = user_notes[index]
        note["favorite"] = not note.get("favorite", False)
        
        status = "ditambahkan ke" if note["favorite"] else "dihapus dari"
        
        if save_data(self.notes_file, notes):
            return True, f"✔ Catatan {status} favorite!"
        
        return False, MESSAGES["save_failed"]
    
    def get_favorites(self, username: str) -> List[Tuple[int, Dict]]:
        """
        Mendapatkan catatan favorite
        
        Args:
            username: Username pemilik catatan
            
        Returns:
            List tuple (index, note)
        """
        notes = self.get_notes(username)
        return [(i, note) for i, note in enumerate(notes) if note.get("favorite", False)]
    
    def get_statistics(self, username: str) -> Dict:
        """
        Mendapatkan statistik catatan
        
        Args:
            username: Username pemilik catatan
            
        Returns:
            Dictionary statistik
        """
        notes = self.get_notes(username)
        
        total = len(notes)
        locked = sum(1 for note in notes if note["is_locked"])
        unlocked = total - locked
        favorites = sum(1 for note in notes if note.get("favorite", False))
        
        # Get all tags
        all_tags = []
        for note in notes:
            all_tags.extend(note.get("tags", []))
        
        unique_tags = len(set(all_tags))
        
        return {
            "total": total,
            "locked": locked,
            "unlocked": unlocked,
            "favorites": favorites,
            "unique_tags": unique_tags
        }
    
    def export_notes(self, username: str, filename: str, 
                     include_locked: bool = False) -> tuple[bool, str]:
        """
        Export catatan ke file JSON
        
        Args:
            username: Username pemilik catatan
            include_locked: Apakah menyertakan catatan terkunci
            
        Returns:
            Tuple (success: bool, message: str)
        """
        notes = self.get_notes(username, include_locked=False)
        
        if not notes:
            return False, "❌ Tidak ada catatan untuk diekspor!"
        
        export_data = []
        for note in notes:
            if note["is_locked"] and not include_locked:
                continue
            
            export_data.append({
                "content": decode_text(note["content"]),
                "tags": note.get("tags", []),
                "favorite": note.get("favorite", False),
                "created_at": note["created_at"],
                "updated_at": note["updated_at"]
            })
        
        try:
            import json
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(export_data, f, indent=4, ensure_ascii=False)
            
            return True, f"✔ {len(export_data)} catatan berhasil diekspor ke {filename}"
        except IOError:
            return False, MESSAGES["export_failed"]
    
    def import_notes(self, username: str, filename: str) -> tuple[bool, str]:
        """
        Import catatan dari file JSON
        
        Args:
            username: Username pemilik catatan
            filename: Path file yang akan diimport
            
        Returns:
            Tuple (success: bool, message: str)
        """
        try:
            import json
            with open(filename, "r", encoding="utf-8") as f:
                import_data = json.load(f)
            
            if not isinstance(import_data, list):
                return False, "❌ Format file tidak valid!"
            
            imported_count = 0
            for item in import_data:
                content = item.get("content", "")
                tags = item.get("tags", [])
                
                if content:
                    success, _ = self.add_note(username, content, tags=tags)
                    if success:
                        imported_count += 1
            
            return True, f"✔ {imported_count} catatan berhasil diimport!"
        
        except (IOError, json.JSONDecodeError):
            return False, "❌ Gagal membaca file!"
