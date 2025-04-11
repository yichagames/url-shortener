import requests
import json

class generate_link():
    def __init__(self):
        self.key = '1134f5453068c09b464b7c8f1088668e4a81d'
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
