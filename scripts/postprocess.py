"""
Postprocessing functions for separated stems.
"""

import os
import soundfile as sf

def normalize_audio(input_path):
    """
    Normalize audio volume for consistency.
    Args:
        input_path (str): Path to the audio file.
    """
    print("Normalizing audio...")
    y, sr = sf.read(input_path)
    max_amp = max(abs(y))
    y_normalized = y / max_amp
    sf.write(input_path, y_normalized, sr)
