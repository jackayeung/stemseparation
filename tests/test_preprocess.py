"""
Test script for preprocess.py
"""

import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from scripts.preprocess import preprocess_audio

class TestPreprocess(unittest.TestCase):
    def test_preprocess_audio(self):
        """
        Test the preprocess_audio function.
        """
        output_file = preprocess_audio("data/Clarity.mp3")
        self.assertTrue(output_file.endswith(".wav"), "Output file should be a .wav file.")

if __name__ == "__main__":
    unittest.main()
