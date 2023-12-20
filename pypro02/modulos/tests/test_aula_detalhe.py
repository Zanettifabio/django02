import pytest
from pypro02.django_assertions import assert_contains
from django.urls import reverse
from model_mommy import mommy
from pypro02.modulos.models import Modulo, Aula


@pytest.fixture
def modulo(db):
    return mommy.make(Modulo)


@pytest.fixture
def aula(modulo):
    return mommy.make(Aula, modulo=modulo)


@pytest.fixture
def resp(client_com_usuario_logado, aula):
    resp = client_com_usuario_logado.get(reverse('modulos:aula', kwargs={'slug': aula.slug}))
    return resp


@pytest.fixture
def resp_sem_usuario_logado(client, aula):
    resp = client.get(reverse('modulos:aula', kwargs={'slug': aula.slug}))
    return resp


def test_titulo_aula(resp, aula):
    assert_contains(resp, aula.titulo)


def test_vimeo(resp, aula):
    assert_contains(resp, f'https://player.vimeo.com/video/{ aula.vimeo_id }')


def test_modulo_breadcrumb(resp, modulo: Modulo):
    assert_contains(resp, f'<li class="breadcrumb-item nav-item"><a class="nav-link text-primary d-flex" href="'
                          f'{modulo.get_absolute_url()}">{modulo.titulo}</a></li>')


def test_usuario_nao_logado_redirect(resp_sem_usuario_logado):
    assert resp_sem_usuario_logado.status_code == 302
    assert resp_sem_usuario_logado.url.startswith(reverse('login'))
