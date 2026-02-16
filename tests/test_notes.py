"""
Unit tests for NotesManager
"""

import os
import sys
import pytest
import tempfile

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from notes_manager import NotesManager


@pytest.fixture
def temp_notes_file():
    """Create temporary notes file for testing"""
    fd, path = tempfile.mkstemp(suffix='.json')
    os.close(fd)
    yield path
    if os.path.exists(path):
        os.unlink(path)


@pytest.fixture
def notes_manager(temp_notes_file):
    """Create NotesManager instance with temp file"""
    return NotesManager(temp_notes_file)


class TestAddNote:
    """Test adding notes functionality"""
    
    def test_add_simple_note(self, notes_manager):
        """Test adding a simple note"""
        success, message = notes_manager.add_note("testuser", "Test content")
        assert success is True
        assert "berhasil" in message.lower()
    
    def test_add_locked_note(self, notes_manager):
        """Test adding a locked note"""
        success, message = notes_manager.add_note(
            "testuser", "Secret content", lock_key="mykey123"
        )
        assert success is True
        
        notes = notes_manager.get_notes("testuser")
        assert notes[0]["is_locked"] is True
    
    def test_add_note_with_tags(self, notes_manager):
        """Test adding note with tags"""
        success, message = notes_manager.add_note(
            "testuser", "Tagged content", tags=["work", "important"]
        )
        assert success is True
        
        notes = notes_manager.get_notes("testuser")
        assert "work" in notes[0]["tags"]
    
    def test_add_empty_note(self, notes_manager):
        """Test adding empty note"""
        success, message = notes_manager.add_note("testuser", "")
        assert success is False


class TestGetNotes:
    """Test retrieving notes functionality"""
    
    def test_get_notes_empty(self, notes_manager):
        """Test getting notes when none exist"""
        notes = notes_manager.get_notes("testuser")
        assert len(notes) == 0
    
    def test_get_notes_multiple(self, notes_manager):
        """Test getting multiple notes"""
        notes_manager.add_note("testuser", "Note 1")
        notes_manager.add_note("testuser", "Note 2")
        notes_manager.add_note("testuser", "Note 3")
        
        notes = notes_manager.get_notes("testuser")
        assert len(notes) == 3
    
    def test_get_notes_exclude_locked(self, notes_manager):
        """Test getting notes excluding locked ones"""
        notes_manager.add_note("testuser", "Open note")
        notes_manager.add_note("testuser", "Locked note", lock_key="key")
        
        notes = notes_manager.get_notes("testuser", include_locked=False)
        assert len(notes) == 1
        assert notes[0]["is_locked"] is False


class TestViewNote:
    """Test viewing note content"""
    
    def test_view_unlocked_note(self, notes_manager):
        """Test viewing unlocked note"""
        notes_manager.add_note("testuser", "Test content")
        success, content = notes_manager.view_note("testuser", 0)
        
        assert success is True
        assert "Test content" in content
    
    def test_view_locked_note_correct_key(self, notes_manager):
        """Test viewing locked note with correct key"""
        notes_manager.add_note("testuser", "Secret", lock_key="mykey")
        success, content = notes_manager.view_note("testuser", 0, key="mykey")
        
        assert success is True
        assert "Secret" in content
    
    def test_view_locked_note_wrong_key(self, notes_manager):
        """Test viewing locked note with wrong key"""
        notes_manager.add_note("testuser", "Secret", lock_key="mykey")
        success, message = notes_manager.view_note("testuser", 0, key="wrongkey")
        
        assert success is False
        assert "salah" in message.lower()
    
    def test_view_invalid_index(self, notes_manager):
        """Test viewing note with invalid index"""
        success, message = notes_manager.view_note("testuser", 99)
        assert success is False


class TestEditNote:
    """Test editing notes functionality"""
    
    def test_edit_unlocked_note(self, notes_manager):
        """Test editing unlocked note"""
        notes_manager.add_note("testuser", "Original content")
        success, message = notes_manager.edit_note(
            "testuser", 0, new_content="Updated content"
        )
        
        assert success is True
        _, content = notes_manager.view_note("testuser", 0)
        assert "Updated content" in content
    
    def test_edit_locked_note_correct_key(self, notes_manager):
        """Test editing locked note with correct key"""
        notes_manager.add_note("testuser", "Original", lock_key="mykey")
        success, message = notes_manager.edit_note(
            "testuser", 0, new_content="Updated", key="mykey"
        )
        
        assert success is True
    
    def test_edit_locked_note_wrong_key(self, notes_manager):
        """Test editing locked note with wrong key"""
        notes_manager.add_note("testuser", "Original", lock_key="mykey")
        success, message = notes_manager.edit_note(
            "testuser", 0, new_content="Updated", key="wrongkey"
        )
        
        assert success is False
    
    def test_edit_add_lock(self, notes_manager):
        """Test adding lock to unlocked note"""
        notes_manager.add_note("testuser", "Content")
        notes_manager.edit_note("testuser", 0, new_lock="newkey")
        
        notes = notes_manager.get_notes("testuser")
        assert notes[0]["is_locked"] is True
    
    def test_edit_remove_lock(self, notes_manager):
        """Test removing lock from locked note"""
        notes_manager.add_note("testuser", "Content", lock_key="mykey")
        notes_manager.edit_note("testuser", 0, new_lock="", key="mykey")
        
        notes = notes_manager.get_notes("testuser")
        assert notes[0]["is_locked"] is False


class TestDeleteNote:
    """Test deleting notes functionality"""
    
    def test_delete_unlocked_note(self, notes_manager):
        """Test deleting unlocked note"""
        notes_manager.add_note("testuser", "To be deleted")
        success, message = notes_manager.delete_note("testuser", 0)
        
        assert success is True
        notes = notes_manager.get_notes("testuser")
        assert len(notes) == 0
    
    def test_delete_locked_note_correct_key(self, notes_manager):
        """Test deleting locked note with correct key"""
        notes_manager.add_note("testuser", "To be deleted", lock_key="mykey")
        success, message = notes_manager.delete_note("testuser", 0, key="mykey")
        
        assert success is True
    
    def test_delete_locked_note_wrong_key(self, notes_manager):
        """Test deleting locked note with wrong key"""
        notes_manager.add_note("testuser", "Protected", lock_key="mykey")
        success, message = notes_manager.delete_note("testuser", 0, key="wrongkey")
        
        assert success is False
        notes = notes_manager.get_notes("testuser")
        assert len(notes) == 1


class TestSearchNotes:
    """Test searching notes functionality"""
    
    def test_search_notes_found(self, notes_manager):
        """Test searching notes with results"""
        notes_manager.add_note("testuser", "Python programming")
        notes_manager.add_note("testuser", "Java development")
        notes_manager.add_note("testuser", "Python tutorial")
        
        results = notes_manager.search_notes("testuser", "Python")
        assert len(results) == 2
    
    def test_search_notes_not_found(self, notes_manager):
        """Test searching notes with no results"""
        notes_manager.add_note("testuser", "Some content")
        results = notes_manager.search_notes("testuser", "NotFound")
        assert len(results) == 0
    
    def test_search_skips_locked_notes(self, notes_manager):
        """Test that search skips locked notes"""
        notes_manager.add_note("testuser", "Python tutorial")
        notes_manager.add_note("testuser", "Python locked", lock_key="key")
        
        results = notes_manager.search_notes("testuser", "Python")
        assert len(results) == 1
    
    def test_search_by_tags(self, notes_manager):
        """Test searching notes by tags"""
        notes_manager.add_note("testuser", "Content 1", tags=["work"])
        notes_manager.add_note("testuser", "Content 2", tags=["personal"])
        
        results = notes_manager.search_notes("testuser", "work", search_tags=True)
        assert len(results) >= 1


class TestNoteStatistics:
    """Test note statistics functionality"""
    
    def test_statistics_empty(self, notes_manager):
        """Test statistics with no notes"""
        stats = notes_manager.get_statistics("testuser")
        assert stats["total"] == 0
        assert stats["locked"] == 0
        assert stats["unlocked"] == 0
    
    def test_statistics_multiple_notes(self, notes_manager):
        """Test statistics with multiple notes"""
        notes_manager.add_note("testuser", "Note 1")
        notes_manager.add_note("testuser", "Note 2", lock_key="key")
        notes_manager.add_note("testuser", "Note 3")
        
        stats = notes_manager.get_statistics("testuser")
        assert stats["total"] == 3
        assert stats["locked"] == 1
        assert stats["unlocked"] == 2


class TestFavorites:
    """Test favorite notes functionality"""
    
    def test_toggle_favorite(self, notes_manager):
        """Test toggling favorite status"""
        notes_manager.add_note("testuser", "Content")
        
        # Toggle to favorite
        success, message = notes_manager.toggle_favorite("testuser", 0)
        assert success is True
        
        notes = notes_manager.get_notes("testuser")
        assert notes[0]["favorite"] is True
        
        # Toggle back
        notes_manager.toggle_favorite("testuser", 0)
        notes = notes_manager.get_notes("testuser")
        assert notes[0]["favorite"] is False
    
    def test_get_favorites(self, notes_manager):
        """Test getting favorite notes"""
        notes_manager.add_note("testuser", "Note 1")
        notes_manager.add_note("testuser", "Note 2")
        notes_manager.toggle_favorite("testuser", 1)
        
        favorites = notes_manager.get_favorites("testuser")
        assert len(favorites) == 1


class TestExportImport:
    """Test export and import functionality"""
    
    def test_export_notes(self, notes_manager, tmp_path):
        """Test exporting notes"""
        notes_manager.add_note("testuser", "Note 1")
        notes_manager.add_note("testuser", "Note 2")
        
        export_file = tmp_path / "export.json"
        success, message = notes_manager.export_notes("testuser", str(export_file))
        
        assert success is True
        assert export_file.exists()
    
    def test_export_empty_notes(self, notes_manager, tmp_path):
        """Test exporting when no notes exist"""
        export_file = tmp_path / "export.json"
        success, message = notes_manager.export_notes("testuser", str(export_file))
        
        assert success is False


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
