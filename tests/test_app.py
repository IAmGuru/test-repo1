import unittest
from src.app import app  # Correct import if app.py is in src/

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()  # Create a test client for Flask
        self.app.testing = True       # Set Flask testing mode to True

    def test_home(self):
        response = self.app.get('/')  # Simulate a GET request to '/'
        self.assertEqual(response.data.decode(), "Hello World !!")  # Assert correct response
        self.assertEqual(response.status_code, 200)  # Assert status code is 200 (OK)

if __name__ == '__main__':
    unittest.main()
