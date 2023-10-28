import unittest
from fastapi.testclient import TestClient
from server.api import app
from server.database import SessionLocal, engine
from server.models import Artist, Album, Track

class TestServer(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)
        self.db = SessionLocal()
        self.setup_test_data()

    def tearDown(self):
        self.db.close()

    def setup_test_data(self):
        # In this method, you can populate the test database with sample data for testing.
        # Create artists, albums, and tracks as needed.
        pass

    def test_search_artists(self):
        # Test searching for artists
        response = self.client.get("/artists/?artist_name=John")
        self.assertEqual(response.status_code, 200)
        # You can add more assertions based on the expected response data.

    def test_get_albums(self):
        # Test getting albums by artist ID
        response = self.client.get("/albums/?artist_id=1")
        self.assertEqual(response.status_code, 200)
        # You can add more assertions based on the expected response data.

    def test_get_tracks(self):
        # Test getting tracks by album ID
        response = self.client.get("/tracks/?album_id=1")
        self.assertEqual(response.status_code, 200)
        # You can add more assertions based on the expected response data.

if __name__ == "__main__":
    unittest.main()

