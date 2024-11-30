from pytubefix import YouTube
from pytubefix.cli import on_progress

url = "url"

yt = YouTube(url, use_oauth=True, allow_oauth_cache=True, on_progress_callback=on_progress)
ys = yt.streams.get_highest_resolution()
ys.download()  # Authenticate once for subsequent downloads