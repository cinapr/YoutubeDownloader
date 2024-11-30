from pytubefix import YouTube
from pytubefix.cli import on_progress

url = "url"

yt = YouTube(url, on_progress_callback=on_progress)
print(yt.title)

# Get the stream with the highest resolution
ys = yt.streams.get_highest_resolution()

# Instead of downloading, just print the download URL
download_url = ys.url  # This will return the direct download URL
print(f"Download URL: {download_url}")
