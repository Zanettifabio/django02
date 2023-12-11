import pytest
from pypro02.django_assertions import assert_contains
from django.urls import reverse
from model_mommy import mommy
from pypro02.modulos.models import Modulo, Aula


@pytest.fixture
def modulo(db):
    return mommy.make(Modulo)


@pytest.fixture
def aulas(modulo):
    return mommy.make(Aula, 3, modulo=modulo)


@pytest.fixture
def resp(client, modulo: Modulo, aulas):
    resp = client.get(reverse('modulos:detalhe', kwargs={'slug': modulo.slug}))
    return resp


def test_titulo_do_modulo(resp, modulo: Modulo):
    assert_contains(resp, modulo.titulo)


def test_publico_do_modulo(resp, modulo: Modulo):
    assert_contains(resp, modulo.publico)


def test_descricao_do_modulo(resp, modulo: Modulo):
    assert_contains(resp, modulo.descricao)


def test_titulo_aulas(resp, aulas):
    for aula in aulas:
        assert_contains(resp, aula.titulo)


def test_aulas_links(resp, aulas):
    for aula in aulas:
        assert_contains(resp, aula.get_absolute_url())
