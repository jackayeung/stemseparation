"""
Main script for stem separation.
Usage: `python main.py`
"""

from scripts.preprocess import preprocess_audio
from scripts.visualize import plot_waveform
from spleeter.separator import Separator
import os

# Paths
INPUT_FILE = "data/example.mp3"
OUTPUT_DIR = "results/"

def main():
    # Preprocess audio
    print("Preprocessing audio...")
    preprocessed_file = preprocess_audio(INPUT_FILE)
    
    # Visualize audio
    print("Visualizing audio waveform...")
    plot_waveform(preprocessed_file)

    # Perform stem separation
    print("Separating stems...")
    separator = Separator("spleeter:2stems")
    separator.separate_to_file(preprocessed_file, OUTPUT_DIR)

    print(f"Results saved in {OUTPUT_DIR}")

if __name__ == "__main__":
    main()
