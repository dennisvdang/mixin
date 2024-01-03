import pandas as pd
import subprocess
import sys
import os

# Check if youtube-dl is installed; if not, install it
try:
    subprocess.call(["youtube-dl", "--version"])
except OSError:
    subprocess.call([sys.executable, "-m", "pip", "install", "youtube-dl"])

# Read the DataFrame from the provided CSV file
csv_file = 'C:/Users/denni/OneDrive/Desktop/Springboard/MusicAnnotator/data/metadata/salami_youtube_pairings.csv'
output_dir = 'C:/Users/denni/OneDrive/Desktop/Springboard/MusicAnnotator/data/unprocessed_music'

df = pd.read_csv(csv_file)

# Iterate over each row in the DataFrame
for index, row in df.iterrows():
    youtube_id = row['youtube_id']
    salami_id = row['salami_id']

    # Build the YouTube URL
    youtube_url = f"https://www.youtube.com/watch?v={youtube_id}"

    # Define the output file path
    output_file = os.path.join(output_dir, f"{salami_id}.mp3")

    # Use youtube-dl to download the song as an MP3 file
    subprocess.call(["youtube-dl", "-x", "--audio-format", "mp3", "-o", output_file, youtube_url])

    print(f"Downloaded song with SALAMI ID: {salami_id}")
