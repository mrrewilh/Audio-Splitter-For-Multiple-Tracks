import os
import subprocess

def separate_audio_channels(directory):
    # Iterate through all files in the directory
    for file_name in os.listdir(directory):
        # Process only .mp4 files
        if file_name.endswith(".mp4"):
            file_path = os.path.join(directory, file_name)
            base_name = os.path.splitext(file_name)[0]

            # Define output file names
            mic_output = os.path.join(directory, f"{base_name}-MIC.mp3")
            sta_output = os.path.join(directory, f"{base_name}-STA.mp3")

            try:
                # Extract microphone audio (usually 0:2 channel) to MIC output
                subprocess.run([
                    "ffmpeg",
                    "-i", file_path,
                    "-map", "0:2",  # Microphone channel
                    "-q:a", "0",
                    mic_output
                ], check=True)

                # Extract system audio (usually 0:1 channel) to STA output
                subprocess.run([
                    "ffmpeg",
                    "-i", file_path,
                    "-map", "0:1",  # System audio channel
                    "-q:a", "0",
                    sta_output
                ], check=True)

                print(f"Audio channels successfully separated for {file_name}.")

            except subprocess.CalledProcessError as e:
                print(f"An error occurred while processing {file_name}: {e}")

if __name__ == "__main__":
    # Get the current working directory
    current_directory = os.getcwd()
    # Separate audio channels for all .mp4 files in the directory
    separate_audio_channels(current_directory)
