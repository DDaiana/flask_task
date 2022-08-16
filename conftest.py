import pytest
import server

@pytest.fixture
def api(monkeypatch):
    test_repos = [{'id': 1, 'name': 'Mochi'}, {'id': 2, 'name': 'Masha'}]
    monkeypatch.setattr(server, "dogs", test_repos)
    api = server.app.test_client()
    return api