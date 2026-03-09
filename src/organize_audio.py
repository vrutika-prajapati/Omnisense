import os
import shutil
import pandas as pd

# Paths
CSV_FILE = "data/audio/ESC-50/meta/esc50.csv"
AUDIO_FOLDER = "data/audio/ESC-50/audio"
OUTPUT_FOLDER = "data/audio/ESC-50/organized_audio"

# Load metadata
df = pd.read_csv(CSV_FILE)

# Create output directory
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

for _, row in df.iterrows():
    filename = row["filename"]
    category = row["category"]

    source_path = os.path.join(AUDIO_FOLDER, filename)

    class_folder = os.path.join(OUTPUT_FOLDER, category)
    os.makedirs(class_folder, exist_ok=True)

    destination_path = os.path.join(class_folder, filename)

    shutil.copy(source_path, destination_path)

print("Audio files organized successfully!")