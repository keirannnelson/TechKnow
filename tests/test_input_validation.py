import unittest
from unittest.mock import patch
from src.input_validation import get_abcd_multi

class TestInputValidation(unittest.TestCase):

    @patch('builtins.input', return_value='a b c')
    def test_get_valid_input(self, mock_input):
        self.assertEqual(get_abcd_multi(), {'a','b','c'})

    @patch('builtins.input', side_effects=['invalid', 'a b c'])
    def test_get_invalid_input(self, mock_input):
        self.assertEqual(get_abcd_multi(), {'a','b','c'})

    @patch('builtins.input', return_value='c b a')
    def test_get_unordered_input(self, mock_input):
        self.assertEqual(get_abcd_multi(), set(['a','b','c']))