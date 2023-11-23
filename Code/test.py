from pytube import YouTube
from playsound import playsound

# Define the URL of the YouTube video
url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # replace with your YouTube video URL

# Create a YouTube object
youtube = YouTube(url)

# Get the highest quality audio stream
audio_stream = youtube.streams.get_audio_only()

# Download the audio stream
filename = audio_stream.download()

# Get size of the file
filesize = audio_stream.filesize
print("File size: " + str(filesize) + " bytes")
