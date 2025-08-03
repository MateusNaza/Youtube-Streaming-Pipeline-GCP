import requests
import os
import json
from dotenv import load_dotenv

from pprint import pprint

from kafka import KafkaProducer

load_dotenv(dotenv_path='config/.env') # Deve-se criar o diretório e o arquivo conforme especificado
API_KEY = os.getenv('API_KEY') # Deve-se armazenar a chave API dentro da variável API_KEY no arquivo '.env'

url = 'https://www.googleapis.com/youtube/v3/videos'

params = {
    'id': 'AAS5UJiHQ4M',
    'part': 'snippet, statistics, status',
    'key': API_KEY
}


if __name__ == '__main__':
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

    response = requests.get(url, params=params)
    data = json.loads(response.text)['items']

    for video in data:
        video_res = {
            'title': video['snippet']['title'],
            'likes': int(video['statistics'].get('likeCount', 0)),
            'comments': int(video['statistics'].get('commentCount', 0)),
            'views': int(video['statistics'].get('viewCount', 0)),
            'favorites': int(video['statistics'].get('favoriteCount', 0)),
            'thumbnail': video['snippet']['thumbnails']['default']['url']
        }

        pprint(video_res)

        producer.send('youtube_videos', json.dumps(video_res).encode('utf-8'))
        producer.flush()
