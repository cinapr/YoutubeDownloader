from pytubefix import YouTube
from pytubefix.cli import on_progress

url = "https://www.youtube.com/watch?v=URL"

yt = YouTube(url, on_progress_callback=on_progress)
print(f"Title: {yt.title}")

# Loop through all available streams and print their resolutions and URLs
for stream in yt.streams.filter(progressive=True):  # Using progressive streams for video and audio combined
    print(f"Resolution: {stream.resolution}, URL: {stream.url}")
