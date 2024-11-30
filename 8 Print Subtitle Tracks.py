from pytubefix import YouTube

yt = YouTube('http://youtube.com/watch?v=2lAe1cqCOXo')
caption = yt.captions['a.en']
print(caption.generate_srt_captions())