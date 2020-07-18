import sys
import unittest
import suzyBot

class TestSuzyBot(unittest.TestCase):
    def test_on_ready(self):
        self.assertEqual(suzyBot.on_ready(), 0)

    def test_on_message(self):
        self.assertEqual(suzyBot.on_message(), 0)

if __name__ == "__main__":
    unittest.main()