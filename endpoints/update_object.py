import requests
import allure
from endpoints.endpoint import Endpoint


class PutObject(Endpoint):

    @allure.step('Update object')
    def update_object(self, object_id, payload=None):
        payload = payload \
            if payload \
            else {'id': object_id,
                  'text': 'Cat and my time',
                  'url': 'https://i.pinimg.com/originals/73/a0/a3/73a0a3620bc479f24f5ab27f147d6aa1.jpg',
                  'tags': ['fun', 'cats', 'time'],
                  'info': {'text': 'I need you to think about me 23/7, you got 1 hour for yourself',
                           'language': 'english'}}
        self.response = requests.put(f'{self.url}/meme/{object_id}',
                                      json = payload,
                                      headers = self.headers)
        self.json = self.response.json() if self.response.status_code == 200 else None
        return self.response