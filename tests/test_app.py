import unittest
import logging
from src.app import app  # Correct import if app.py is in the src/ directory

class FlaskTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Run this once before any tests are executed."""
        cls.logger = logging.getLogger('src.app')  # Logger from your app
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    def setUp(self):
        """Set up a test client before each test."""
        self.app = app.test_client()  # Create a test client for Flask
        self.app.testing = True       # Set Flask testing mode to True

    def test_home(self):
        """Test the home route for correct response and log output."""
        # Simulate a GET request to '/'
        with self.assertLogs(self.logger, level='INFO') as log:
            response = self.app.get('/')
        
        # Check the status code and content of the response
        self.assertEqual(response.data.decode(), "Hello World !!")  # Assert correct response
        self.assertEqual(response.status_code, 200)  # Assert status code is 200 (OK)

        # Check if the log contains the expected info message
        self.assertIn("flask app execution begins", log.output[0])

    def test_error_handling(self):
        """Test if errors are logged correctly."""
        with self.assertRaises(Exception):
            try:
                # Simulate an error by logging an exception
                raise Exception("This is a test error")
            except Exception as e:
                with self.assertLogs(self.logger, level='ERROR') as log:
                    logging.error(f"An error occurred: {e}")
                    self.assertIn("An error occurred: This is a test error", log.output[0])

if __name__ == '__main__':
    unittest.main()
