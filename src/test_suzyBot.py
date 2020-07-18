import sys
import unittest
from suzyBot import SuzyBot
import pytest

class TestSuzyBot(pytest.Class):
    def __init__(self):
        self.client = SuzyBot()
        
    def test_on_ready(self):
        pass

    def test_on_message(self):
        self.assertEqual(self.client.on_message(), 0)

if __name__ == "__main__":
    unittest.main()