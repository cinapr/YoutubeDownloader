from pytubefix.contrib.search import Search, Filter

filters = {
    'upload_date': Filter.get_upload_date('Today'),
    'type': Filter.get_type("Video"),
    'duration': Filter.get_duration("Under 4 minutes"),
    'features': [Filter.get_features("4K"), Filter.get_features("Creative Commons")],
    'sort_by': Filter.get_sort_by("Upload date")
}

s = Search('music', filters=filters)
for video in s.videos:
    print(video.watch_url)