# test_coinlink.py
"""
Tests for CoinLink module.
"""

import unittest
from coinlink import CoinLink

class TestCoinLink(unittest.TestCase):
    """Test cases for CoinLink class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CoinLink()
        self.assertIsInstance(instance, CoinLink)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CoinLink()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
