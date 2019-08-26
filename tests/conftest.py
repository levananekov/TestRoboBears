import pytest
import requests

from bears.bear_api import create_bear , make_bear_url

data_for_default_bear = {'bear_type': 'POLAR', 'bear_name': 'default_one', 'bear_age': 33.0}


@pytest.fixture(scope='session')
def get_new_bear_id():
    bear_id = create_bear(data_for_default_bear)
    yield bear_id
    url = make_bear_url(bear_id)
    requests.delete(url)