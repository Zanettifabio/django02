import pytest
from django.urls import reverse

from pypro02.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    return client.get(reverse('aperitivos:video', args=('motivacao',)))


def test_status_code(resp):
    assert resp.status_code == 200


def test_titulo_video(resp):
    assert_contains(resp, '>Vídeo Aperitivo: Motivação</h1>')


def test_conteudo_video(resp):
    assert_contains(resp, '<iframe src="https://player.vimeo.com/video/887979526?badge=0&amp;autopause=0&amp'
                          ';quality_selector=1&amp;player_id=0&amp;app_id=58479"')
