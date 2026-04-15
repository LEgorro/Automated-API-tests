import requests
import allure


class Token:


    @allure.step('Get token')
    def get_token(self, old_token=None):
        if 'Token is alive' in requests.get(url=f'http://memesapi.course.qa-practice.com/authorize/{old_token}').text:
            return old_token
        else:
            self.response = requests.post(url=f'http://memesapi.course.qa-practice.com/authorize', json={'name': 'username'})
            return self.response.json()['token']

    @allure.step('Check new token created')
    def check_new_token_created(self):
        assert self.response.json()['token'] is not None, 'Token not found'


    @allure.step('Check old token is alive')
    def check_old_token_is_alive(self, old_token):
        assert ('Token is alive' in
                requests.get(url=f'http://memesapi.course.qa-practice.com/authorize/{old_token}').text)