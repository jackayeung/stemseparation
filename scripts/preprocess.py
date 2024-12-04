"""
Preprocessing functions for audio data.
"""

import librosa
import soundfile as sf

def preprocess_audio(input_path):
    """
    Preprocess an audio file (e.g., resampling and trimming).
    Args:
        input_path (str): Path to the input audio file.
    Returns:
        str: Path to the processed audio file.
    """
    output_path = "data/processed_audio.wav"
    
    # Load audio file
    print("Loading audio...")
    y, sr = librosa.load(input_path, sr=44100)

    # Trim silence
    print("Trimming silence...")
    y_trimmed, _ = librosa.effects.trim(y)

    # Save processed audio
    print("Saving processed audio...")
    sf.write(output_path, y_trimmed, sr)

    return output_path
