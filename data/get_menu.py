import requests
import json

url = 'https://api.theta.tv/v1/theta/channel/list?number=100'
data = requests.get(url).json()

channels = data['body']

data = []

for c in channels:
    s = c['live_stream']
    obj = {
            'id': c['user_id'],
            'title': s['title'],
            'description': s['title'],
            'duration': 60,
            'thumbUrl': s['game']['thumbnail_url'],
            'imgUrl': s['game']['logo_url'],
            'videoUrl': s['video_url_map']['2d']['master'],
            'categories': [s['game']['name']],
            'channel_id': c['live_stream_id']
        }
    data.append(obj)





with open('data.json', 'w') as f:
    f.write(json.dumps(data))

