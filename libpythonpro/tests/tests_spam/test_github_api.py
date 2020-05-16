from libpythonpro import github_api
from unittest.mock import Mock


def test_buscar_avatar():
    resp_mock = Mock()
    resp_mock.json.return_value = {'login': 'Pbezerra-dev', 'id': 51804133, 'node_id': 'MDQ6VXNlcjUxODA0MTMz',
                                   'avatar_url': 'https://avatars0.githubusercontent.com/u/51804133?v=4'}
    github_api.requests.get = Mock(return_value=resp_mock)
    url = github_api.buscar_avatar('Pbezerra-dev')
    assert 'https://avatars0.githubusercontent.com/u/51804133?v=4' == url
