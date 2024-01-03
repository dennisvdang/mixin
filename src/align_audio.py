import os
import subprocess
import pandas as pd

# Define your directories and file paths here
downloaded_audio_folder = '../data/audio_files/raw_audio'
transformed_audio_folder = '../data/audio_files/processed_audio'
match_data_csv = '../data/reference_data/salami_youtube_pairings.csv"

def reshape_audio_ffmpeg(salami_id, row):
    input_filename = os.path.join(downloaded_audio_folder, f"{salami_id}.mp3")
    output_filename = os.path.join(transformed_audio_folder, f"{salami_id}.mp3")
    
    start_time_in_yt = row["onset_in_youtube"] - row["onset_in_salami"]
    end_time_in_yt = start_time_in_yt + row["salami_length"]

    # Prepare ffmpeg command for trimming and padding
    ffmpeg_cmd = ["ffmpeg", "-i", input_filename]

    # Apply padding if necessary
    if start_time_in_yt < 0:
        pad_duration = abs(start_time_in_yt)
        ffmpeg_cmd.extend(["-af", f"apad=pad_dur={pad_duration}", "-ss", "0"])
        start_time_in_yt = 0
    else:
        ffmpeg_cmd.extend(["-ss", str(start_time_in_yt)])

    # Set the duration of the output file
    ffmpeg_cmd.extend(["-t", str(row["salami_length"])])

    # Specify output file
    ffmpeg_cmd.append(output_filename)

    # Execute the ffmpeg command
    try:
        subprocess.run(ffmpeg_cmd, check=True)
        print(f"Successfully processed file: {output_filename}")
    except subprocess.CalledProcessError as e:
        print(f"Error processing file {input_filename}. Error: {e}")

def main():
    # Load match data from CSV
    match_data = pd.read_csv(match_data_csv)

    # Ensure the transformed audio directory exists
    if not os.path.exists(transformed_audio_folder):
        os.makedirs(transformed_audio_folder)

    # Process each entry in the match data
    for _, row in match_data.iterrows():
        reshape_audio_ffmpeg(row['salami_id'], row)

if __name__ == "__main__":
    main()