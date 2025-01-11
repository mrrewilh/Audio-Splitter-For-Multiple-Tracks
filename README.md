# Audio-Splitter-For-Multiple-Tracks
This project simplifies the audio editing process, saving time for content creators and streamers. 

# Project Description:
This project is a Python script that is requested to automatically separate audio channels from .mp4 video files with multi-channel audio switching. I created this for NVIDIA ShadowPlay. It typically uses two distinct audio channels: one for the microphone (user's voice) and another for the system audio (game and application sounds). The script analyzes these audio streams and exports each as a separate .mp3 file.

# Features:
Scans and processes .mp4 files in the working directory.

Exports microphone audio as {filename}-MIC.mp3.

Exports system audio as {filename}-STA.mp3.

Fully automated and user-friendly.

Uses FFmpeg for high-speed and high-quality audio extraction.


# Use Cases:
For users recording gameplay with NVIDIA ShadowPlay who want separate audio tracks for editing or sharing.

For streamers or content creators requiring professional-grade audio processing.

# Requirements:
Python 3.x must be installed.

FFmpeg must be installed and added to the system PATH.

# How to Use:
Place the Python script in the directory containing your .mp4 files.

Run the script. It will scan all .mp4 files and separate the audio channels.

Outputs will be saved in the same directory as {filename}-MIC.mp3 and {filename}-STA.mp3.
