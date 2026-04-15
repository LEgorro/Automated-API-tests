import requests
import allure
from endpoints.endpoint import Endpoint


class DeleteObject(Endpoint):

    @allure.step('Delete object')
    def delete_object(self, object_id):
        self.response = requests.delete(f'{self.url}/meme/{object_id}', headers=self.headers)
        return self.response


    @allure.step('Check object has been deleted')
    def check_object_is_deleted(self):
        assert 'successfully deleted' in self.response.text
