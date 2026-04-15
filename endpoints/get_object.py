import requests
import allure
from endpoints.endpoint import Endpoint


class GetObject(Endpoint):

    @allure.step('Get_object')
    def get_object(self, object_id=None):
        if object_id:
            self.response = requests.get(f'{self.url}/meme/{object_id}', headers=self.headers)
        else:
            self.response = requests.get(f'{self.url}/meme', headers=self.headers)
        self.json = self.response.json() if self.response.status_code == 200 else None
        return self.response
