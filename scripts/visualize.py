"""
Visualization functions for audio data.
"""

import librosa
import librosa.display
import matplotlib.pyplot as plt

def plot_waveform(audio_path):
    """
    Plot the waveform of an audio file.
    Args:
        audio_path (str): Path to the audio file.
    """
    print("Generating waveform plot...")
    y, sr = librosa.load(audio_path, sr=44100)

    # Plot waveform
    plt.figure(figsize=(10, 4))
    librosa.display.waveshow(y, sr=sr)
    plt.title("Waveform")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.show()
