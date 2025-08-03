import requests
import os
import json
from dotenv import load_dotenv

load_dotenv(dotenv_path='config/.env') # Deve-se criar o diretório e o arquivo conforme especificado
API_KEY = os.getenv('API_KEY') # Deve-se armazenar a chave API dentro da variável API_KEY no arquivo '.env'

url = 'https://www.googleapis.com/youtube/v3/videos'

params = {
    'part': 'snippet,statistics',
    'chart': 'mostPopular',
    'regionCode': 'BR', 
    'maxResults': 5,
    'key': API_KEY
}

if __name__ == '__main__':
    response = requests.get(url, params=params)
    data = response.json()
    print(json.dumps(data, indent=2))
