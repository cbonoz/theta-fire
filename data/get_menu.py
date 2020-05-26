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
            'id': str(i + 500),
            'title': title,
            'description': title,
            'duration': str(60),
            'thumbURL': s['thumbnail_url'],
            'imgURL': s['thumbnail_url'],
            'videoURL': s['video_url_map']['2d']['master'],
            'categories': [s['game']['name']],
            'channel_id': "13454"
        }
    data.append(obj)





with open('data.json', 'w') as f:
    s = json.dumps(data)
    f.write(s)

