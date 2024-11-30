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
        cc_url = ""  # To store the SRT file URL for captions

        # Loop through all available streams and capture resolution and URL
        for stream in yt.streams.filter(progressive=True):  # Using progressive streams for video and audio combined
            streamurl += f"Resolution: {stream.resolution} : {stream.url}\n\n"

        # Check if English captions (SRT) are available
            try:
                caption = yt.captions['en']
                caption.save_captions(f"{title}.srt")
                #pass
            except Exception as e:
                print(f"No ENGLISH CAPTION. An error occurred: {e}")
        
        # Write the video title, stream URLs, and captions URL to the file
        file.write(f"Title: {title}\n{streamurl}{cc_url}{'-'*40}\n")
        
        # Print success message for each processed video
        print(f"Successfully processed: {title}")

print("Stream URLs and captions saved to 'streams_urls.txt'")
