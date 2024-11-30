from pytubefix import YouTube, Playlist
from pytubefix.cli import on_progress

url_playlist = "https://www.youtube.com/playlist?list=PLAYLISTURL"

# Open the text file in write mode to save the results
with open('streams_urls.txt', 'w', encoding='utf-8') as file:
    # Fetch the playlist
    playlist = Playlist(url_playlist)
    
    # Loop through all videos in the playlist
    for url in playlist.video_urls:
        yt = YouTube(url, on_progress_callback=on_progress)
        title = yt.title
        streamurl = ""

        # Loop through all available streams and capture resolution and URL
        for stream in yt.streams.filter(progressive=True):  # Using progressive streams for video and audio combined
            streamurl += f"Resolution: {stream.resolution} : {stream.url}\n\n"
        
        # Append the video title and stream URLs to the file
        file.write(f"Title: {title}\n{streamurl}\n{'-'*40}\n")
        
        # Print success message for each processed video
        print(f"Successfully processed: {title}")

print("Stream URLs saved to 'streams_urls.txt'")
