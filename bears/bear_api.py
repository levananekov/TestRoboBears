import json
from urllib.parse import urljoin

import requests

from bears.config import default_url


def make_bear_url(bear_id=None):
    endpoint = 'bear'
    if bear_id:
        return urljoin(default_url, f'{endpoint}/{bear_id}')
    return urljoin(default_url, endpoint)


def create_bear(data_for_bear):
    url = make_bear_url()
    response = requests.post(url, json=data_for_bear)
    return response.json()


def get_info_about_all_bears():
    url = make_bear_url()
    response = requests.get(url)
    return response.json()


def get_info_about_bear_by_id(bear_id):
    url = make_bear_url(bear_id)
    response = requests.get(url)
    assert response.ok
    try:
        result = response.json()
    except json.JSONDecodeError:
        result = response.text
    return result


