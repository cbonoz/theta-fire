import requests
import json

url = 'https://api.theta.tv/v1/theta/channel/list?number=100'
data = requests.get(url).json()

channels = data['body']

data = []

for i, c in enumerate(channels):
    s = c['live_stream']
    title = s['title'].encode('ascii', 'ignore').decode('ascii')
    obj = {
            'id': str(i + 1),
            'title': title,
            'description': title,
            'duration': str(60),
            'thumbURL': s['game']['thumbnail_url'],
            'imgURL': s['game']['logo_url'],
            'videoURL': s['video_url_map']['2d']['master'],
            'categories': [s['game']['name']],
            'channel_id': "123456"
        }
    data.append(obj)
    break





with open('data.json', 'w') as f:
    s = json.dumps(data)
    f.write(s)

