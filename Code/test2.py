from youtube_dl import YoutubeDL

# Create a YoutubeDL object - verbose to get more information while downloading

ydl = YoutubeDL({'verbose': True})

# Download video
ydl.download(['https://www.youtube.com/watch?v=dQw4w9WgXcQ'])  # replace with your YouTube video URL