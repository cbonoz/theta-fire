import requests
import json

url = 'https://api.theta.tv/v1/theta/channel/list?number=100'
data = requests.get(url).json()

channels = data['body']

data = []

for c in channels:
    s = c['live_stream']
    obj = {
            'title': s['title'],
            'categories': [s['game']['thumbnail_url']],
            'description': s['title'],
            'videoUrl': s['video_url_map']['2d']['master'],
            'channel_id': c['live_stream_id']
        }
    data.append(obj)





with open('data.json', 'w') as f:
    f.write(json.dumps(data))

