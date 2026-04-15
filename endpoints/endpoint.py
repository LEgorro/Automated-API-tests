import allure
import requests


def is_token_alive(token):
    response = requests.get(url=f'http://memesapi.course.qa-practice.com/authorize/{token}')
    return 'Token is alive' in response.text


def get_token():
    token = 'kanJBTzIclqhy7O'
    if is_token_alive(token):
        print(f'Жив старый токен: {token}')
        return token
    else:
        response = requests.post(url = 'http://memesapi.course.qa-practice.com/authorize', json = {'name': 'username'})
        print(f'Новый токен: {response.json()['token']}')
        return response.json()['token']



class Endpoint:
    url = 'http://memesapi.course.qa-practice.com/'
    token = get_token()
    headers = {'Authorization': token}
    response = None
    json = None

    @allure.step('Check response status code')
    def assert_status_code_is(self, code):
        assert self.response.status_code == code, f'Wrong status code: {self.response.status_code}'