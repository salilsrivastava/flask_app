import unittest

from homepage import homepage

class homepage_tests(unittest.TestCase):

    def setUp(self):
        homepage.testing = True
        self.homepage = homepage.test_client()

    def test_index_route(self):
        response = self.homepage.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello, World!', response.data)

    def test_nonexistent_route(self):
        response = self.homepage.get('/nonexistent')
        self.assertEqual(response.status_code, 404)

    def test_convert_epoch_to_datetime(self):
        epoch_time = 1710009507
        response = self.homepage.get(f'/convert_epoch?epoch_time={epoch_time}')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<h1>Converted Datetime:</h1>', response.data)
        self.assertIn(b'2024-03-09 18:38:27', response.data)

    def test_invalid_epoch_parameter(self):
        epoch_time = 'invalid_epoch'
        response = self.homepage.get(f'/convert_epoch?epoch_time={epoch_time}')
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'<h1>Error:', response.data)

    def test_missing_epoch_parameter(self):
        response = self.homepage.get('/convert_epoch')
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'<h1>Error: Epoch time parameter is required.</h1>', response.data)
