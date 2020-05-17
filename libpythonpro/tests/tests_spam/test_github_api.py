from libpythonpro import github_api
from unittest.mock import Mock
import pytest


@pytest.fixture
def avatar_url(mocker):
    resp_mock = Mock()
    url = 'https://avatars0.githubusercontent.com/u/51724123?v=4'
    resp_mock.json.return_value = {
        'login': 'Pbezerra-dev', 'id': 51804133,
        'avatar_url': url
    }
    get_mock = mocker.patch('libpythonpro.github_api.requests.get')
    get_mock.return_value = resp_mock
    return url


def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('Pbezerra-dev')
    assert avatar_url == url


def test_buscar_avatar_integracao():
    url = github_api.buscar_avatar('Pbezerra-dev')
    assert 'https://avatars0.githubusercontent.com/u/51804133?v=4' == url
