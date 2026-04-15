import pytest



old_token = 'TLsMmp1O2RqZajk'
TEST_DATA = [{'text': 'Cat and his time',
              'url': 'https://i.pinimg.com/originals/73/a0/a3/73a0a3620bc479f24f5ab27f147d6aa1.jpg',
              'tags': ['fun', 'cat'],
              'info': {'text': 'I need you to think about me 23/7', 'language': 'english'}},
             {'text': 'Dog and his dream',
              'url': 'https://i.ebayimg.com/images/g/wzsAAOSwrklU-iak/s-l500.jpg',
              'tags': ['fun', 'dog', 'dream'],
              'info': {'text': 'Living the dream', 'language': 'english'}}
             ]


def test_create_new_user(token_endpoint):
    token_endpoint.get_token()
    token_endpoint.check_new_token_created()


def test_old_token_is_alive(token_endpoint):
    token_endpoint.check_old_token_is_alive(old_token)


def test_api_get_all_objects(get_object_endpoint):
    get_object_endpoint.get_object()
    get_object_endpoint.assert_status_code_is(200)


def test_api_get_one_object(get_object_endpoint, get_new_object_id):
    get_object_endpoint.get_object(object_id=get_new_object_id)
    get_object_endpoint.assert_status_code_is(200)


def test_api_get_one_wrong_object(get_object_endpoint, get_new_object_id):
    get_object_endpoint.get_object(object_id='wrong_id')
    get_object_endpoint.assert_status_code_is(404)


@pytest.mark.parametrize('payload', TEST_DATA)
def test_api_create_object(create_object_endpoint, payload):
    create_object_endpoint.create_object(payload=payload)
    create_object_endpoint.assert_status_code_is(200)


def test_api_create_object_with_incomplete_data(create_object_endpoint):
    incomplete_data = {'id': '10000',
                       'url': 'https://i.pinimg.com/originals/73/a0/a3/73a0a3620bc479f24f5ab27f147d6aa1.jpg',
                       'tags': ['fun', 'cats', 'time'],
                       'info': {'text': 'I need you to think about me 23/7, you got 1 hour for yourself',
                                'language': 'english'}}
    create_object_endpoint.create_object(payload=incomplete_data)
    create_object_endpoint.assert_status_code_is(400)


def test_api_create_object_with_wrong_data(create_object_endpoint):
    incomplete_data = {'id': 'wrong',
                       'text': 'I need you to think about me 23/7',
                       'url': 'https://i.pinimg.com/originals/73/a0/a3/73a0a3620bc479f24f5ab27f147d6aa1.jpg',
                       'tags': 500,
                       'info': {'text': 'I need you to think about me 23/7, you got 1 hour for yourself',
                                'language': 'english'}}
    create_object_endpoint.create_object(payload=incomplete_data)
    create_object_endpoint.assert_status_code_is(400)


def test_api_update_object(update_object_endpoint, get_new_object_id):
    update_object_endpoint.update_object(get_new_object_id)
    update_object_endpoint.assert_status_code_is(200)


def test_api_update_object_with_incomplete_data(update_object_endpoint, get_new_object_id):
    incomplete_data = {'id': get_new_object_id,
                       'url': 'https://i.pinimg.com/originals/73/a0/a3/73a0a3620bc479f24f5ab27f147d6aa1.jpg',
                       'tags': ['fun', 'cats', 'time'],
                       'info': {'text': 'I need you to think about me 23/7, you got 1 hour for yourself',
                                'language': 'english'}}
    update_object_endpoint.update_object(get_new_object_id,payload=incomplete_data)
    update_object_endpoint.assert_status_code_is(400)


def test_api_delete_object(delete_object_endpoint, get_new_object_id_without_deleting_object):
    delete_object_endpoint.delete_object(get_new_object_id_without_deleting_object)
    delete_object_endpoint.assert_status_code_is(200)
    delete_object_endpoint.check_object_is_deleted()


def test_api_delete_nonexistent_object(delete_object_endpoint):
    delete_object_endpoint.delete_object(-1)
    delete_object_endpoint.assert_status_code_is(404)
