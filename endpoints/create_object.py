import requests
import allure
from endpoints.endpoint import Endpoint


class PostObject(Endpoint):

    @allure.step('Create new object')
    def create_object(self, payload):
        self.response = requests.post(f'{self.url}/meme',
                                      json = payload,
                                      headers = self.headers)
        self.json = self.response.json() if self.response.status_code == 200 else None
        return self.response