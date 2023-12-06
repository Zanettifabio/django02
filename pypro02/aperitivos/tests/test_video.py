import pytest
from django.urls import reverse
from pypro02.aperitivos.models import Video
from pypro02.django_assertions import assert_contains
from model_mommy import mommy


@pytest.fixture
def video(db):
    return mommy.make(Video)


@pytest.fixture
def resp(client, video):
    return client.get(reverse('aperitivos:video', args=(video.slug,)))


@pytest.fixture
def resp_video_nao_encontrado(client, video):
    return client.get(reverse('aperitivos:video', args=(video.slug+'slug_nao_existente',)))


def test_status_code(resp):
    assert resp.status_code == 200


def test_status_code_video_nao_encontrado(resp_video_nao_encontrado):
    assert resp_video_nao_encontrado.status_code == 404


def test_titulo_video(resp, video):
    assert_contains(resp, video.titulo)


def test_conteudo_video(resp, video):
    assert_contains(resp, f'<iframe src="https://player.vimeo.com/video/{video.vimeo_id}?badge=0&amp;autopause=0&amp'
                          ';quality_selector=1&amp;player_id=0&amp;app_id=58479"')
