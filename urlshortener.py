import requests
from dotenv import load_dotenv
import os

load_dotenv()

class generate_link():
    def __init__(self):
        self.key = os.getenv('KEY')
    def shorten(self, link):
        return (self.gen(link))
    def gen(self, link):
        post = {
            'key': self.key,
            'short': link
        }
        response = requests.post("https://cutt.ly/api/api.php", params=post)
        data = response.json()  
        print(data)
        return (data['url']['shortLink'])

if __name__ == "__main__":
    x = generate_link()
