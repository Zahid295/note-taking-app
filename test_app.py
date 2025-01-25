# test_app.py

import unittest
from app import app

class NotesTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_add_note(self):
        response = self.app.post('/notes', json={'note': 'Test Note'})
        self.assertEqual(response.status_code, 201)

    def test_get_notes(self):
        response = self.app.get('/notes')
        self.assertEqual(response.status_code, 200)

    def test_get_note_detail(self):
        self.app.post('/notes', json={'note': 'Test Note'})
        response = self.app.get('/notes/0')
        self.assertEqual(response.status_code, 200)

    def test_delete_note(self):
        self.app.post('/notes', json={'note': 'Test Note'})
        response = self.app.delete('/notes/0')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
