import unittest
from homepage import convert_epoch_to_datetime

class TestConvertEpochToDatetime(unittest.TestCase):

    def test_convert_epoch_to_datetime_valid(self):
        # Test with a valid epoch time
        epoch_time = 1710009507  # Example epoch time
        html_result = convert_epoch_to_datetime(epoch_time)
        self.assertIn('2024-03-09 18:38:27', html_result)
    
    def test_convert_epoch_to_datetime_negative(self):
        # Test with a negative epoch time
        epoch_time = -1615380000  # Example negative epoch time
        html_result = convert_epoch_to_datetime(epoch_time)
        self.assertIn('<h1>Error: Epoch time cannot be negative.</h1>', html_result)

    def test_convert_epoch_to_datetime_zero(self):
        # Test with epoch time as zero
        epoch_time = 0
        html_result = convert_epoch_to_datetime(epoch_time)
        self.assertIn('<p>1970-01-01 00:00:00</p>', html_result)

    def test_convert_epoch_to_datetime_none(self):
        # Test with None as epoch time
        epoch_time = None

        html_result = convert_epoch_to_datetime(epoch_time)
        print(html_result)
        self.assertIn('<h1>Error: Epoch time parameter is required.</h1>', html_result)
