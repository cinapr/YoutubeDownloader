from pytubefix import YouTube

yt = YouTube('http://youtube.com/watch?v=2lAe1cqCOXo')
caption = yt.captions['a.en']
caption.save_captions("captions.txt")