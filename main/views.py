from django.shortcuts import render
from django.conf import settings
import requests
def index(request):
    search_url = 'https://www.googleapis.com/youtube/v3/search'
    video_url = 'https://www.googleapis.com/youtube/v3/videos'
    param = {
           'part': 'snippet',
           'key' : settings.YOUTUBE_DATA_API_KEY,
           'maxResults' : 9,
           'q': 'ni rehna',
           'type': 'video'
            }
    r = requests.get(search_url, params = param)   
    videos_id = []
    results = r.json()['items']
    for result in results:
        videos_id.append(result['id']['videoId'])

    param = {
           'part': 'snippet',
           'key' : settings.YOUTUBE_DATA_API_KEY,
           'id':','.join(videos_id)
            }
    r = requests.get(video_url, params = param)
    results = r.json()['items']
    videos = []
    for result in results:
        video_data = {
            'title' : result['snippet']['title'],
            'id': result['id'],
            'url': f'https://www.youtube.com/watch?v={result["id"]}',
            'thumbnail': result['snippet']['thumbnails']['high']['url']
            }
        videos.append(video_data)
    context = {
        'videos':videos
        }
       
    return render(request, 'index.html', context)
