import pytest
import requests

from bears.bear_api import make_bear_url , get_info_about_bear_by_id , get_info_about_all_bears


bears_of_all_types = [
    {'bear_type': 'POLAR', 'bear_name': 'MIFA1', 'bear_age': 33.0},
    {'bear_type': 'BROWN', 'bear_name': 'MIFA2', 'bear_age': 34.0},
    {'bear_type': 'BLACK', 'bear_name': 'MIFA3', 'bear_age': 35.0},
    {'bear_type': 'GUMMY', 'bear_name': 'MIFA4', 'bear_age': 36.0},
]


@pytest.mark.parallel
@pytest.mark.parametrize('data_for_create', bears_of_all_types)
def test_create_bears(data_for_create):
    url = make_bear_url()
    new_bear_id = requests.post(url, json=data_for_create)
    new_bear_info = get_info_about_bear_by_id(new_bear_id.text)
    assert new_bear_info['bear_id']

    new_bear_info.pop('bear_id')
    assert new_bear_info == data_for_create


@pytest.mark.parallel
@pytest.mark.parametrize('data_for_update', bears_of_all_types)
def test_update_bear(get_new_bear_id, data_for_update):
    url = make_bear_url(get_new_bear_id)
    response = requests.put(url, json=data_for_update)
    assert response.ok

    data_for_update['bear_id'] = get_new_bear_id
    new_bear_info = get_info_about_bear_by_id(get_new_bear_id)
    assert new_bear_info == data_for_update


@pytest.mark.parallel
def test_delete_bear_by_id(get_new_bear_id):
    url = make_bear_url(get_new_bear_id)
    response = requests.delete(url)
    bear_info = get_info_about_bear_by_id(get_new_bear_id)

    assert response.ok
    assert bear_info == 'EMPTY'


@pytest.mark.not_in_parallel
def test_delete_all_bears(get_new_bear_id):
    url = make_bear_url()
    response = requests.delete(url)
    assert response.ok

    info_about_all_bears = get_info_about_all_bears()
    assert not info_about_all_bears
