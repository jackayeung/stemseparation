"""
Test script for preprocess.py
"""

import unittest
from scripts.preprocess import preprocess_audio

class TestPreprocess(unittest.TestCase):
    def test_preprocess_audio(self):
        """
        Test the preprocess_audio function.
        """
        output_file = preprocess_audio("data/example.mp3")
        self.assertTrue(output_file.endswith(".wav"), "Output file should be a .wav file.")

if __name__ == "__main__":
    unittest.main()
