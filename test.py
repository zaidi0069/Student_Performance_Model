import unittest
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        # Create a test client
        self.app = app.test_client()
        # Propagate exceptions to the test client
        self.app.testing = True

    def test_home_page(self):
        # Send a GET request to the '/' route
        response = self.app.get('/')
        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

    def test_predict_endpoint(self):
        # Sample request data for prediction
        data = {
            'Hours Studied': '7',
            'Previous Scores': '90',
            'Extracurricular Activities': 'Yes',
            'Sleep Hours': '8',
            'Sample Question Papers Practiced': '3'
        }
        # Send a POST request to the '/predict' route with sample data
        response = self.app.post('/predict', data=data)
        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        # Check if the prediction text is present in the response content
        self.assertIn(b"Student Performance Index is:", response.data)

if __name__ == '__main__':
    unittest.main()
