import inspect

import pytest
import requests
from endpoints.delete_object import DeleteObject
from endpoints.get_object import GetObject
from endpoints.create_object import PostObject
from endpoints.update_object import PutObject
from endpoints.delete_object import DeleteObject
from endpoints.get_token import Token


@pytest.fixture()
def get_object_endpoint():
    return GetObject()

@pytest.fixture()
def create_object_endpoint():
    return PostObject()

@pytest.fixture()
def update_object_endpoint():
    return PutObject()

@pytest.fixture()
def delete_object_endpoint():
    return DeleteObject()

@pytest.fixture()
def token_endpoint():
    return Token()


@pytest.fixture()
def get_token():
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url = 'http://memesapi.course.qa-practice.com/authorize', json = {'name': 'username'}, headers=headers)
    myjson = response.json()
    print(myjson['token'])
    return myjson['token']


@pytest.fixture()
def get_new_object_id(create_object_endpoint, delete_object_endpoint):
    payload = {'text': 'Dog and homework',
               'url': 'https://i.pinimg.com/736x/a0/05/ad/a005ad834b3ed27c71b4b3fe58701b51.jpg',
               'tags': ['fun', 'dog', 'homework'],
               'info': {'text': 'This homework looks hard...', 'language': 'english'}}
    object_id = create_object_endpoint.create_object(payload).json()['id']
    yield object_id
    delete_object_endpoint.delete_object(object_id)

@pytest.fixture()
def get_new_object_id_without_deleting_object(create_object_endpoint):
    payload = {'text': 'Dog and homework',
               'url': 'https://i.pinimg.com/736x/a0/05/ad/a005ad834b3ed27c71b4b3fe58701b51.jpg',
               'tags': ['fun', 'dog', 'homework'],
               'info': {'text': 'This homework looks hard...', 'language': 'english'}}
    object_id = create_object_endpoint.create_object(payload).json()['id']
    yield object_id