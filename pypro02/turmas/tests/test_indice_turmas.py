import pytest
from django.urls import reverse


@pytest.fixture
def resp(db, client):
    return client.get(reverse('turmas:indice'))


def test_status_code(resp):
    assert resp.status_code == 200
