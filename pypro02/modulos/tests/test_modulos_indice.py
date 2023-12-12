import pytest
from pypro02.django_assertions import assert_contains
from django.urls import reverse
from model_mommy import mommy
from pypro02.modulos.models import Modulo, Aula


@pytest.fixture
def modulos(db):
    return mommy.make(Modulo, 2)


@pytest.fixture
def aulas(modulos):
    aulas = []
    for modulo in modulos:
        aulas.extend(mommy.make(Aula, 3, modulo=modulo))
    return aulas


@pytest.fixture
def resp(client, modulos, aulas):
    resp = client.get(reverse('modulos:indice'))
    return resp


def test_indice_disponivel(resp):
    assert resp.status_code == 200


def test_titulo_do_modulo(resp, modulos: list[Modulo]):
    for modulo in modulos:
        assert_contains(resp, modulo.titulo)


def test_publico_do_modulo(resp, modulos: list[Modulo]):
    for modulo in modulos:
        assert_contains(resp, modulo.publico)


def test_descricao_do_modulo(resp, modulos: list[Modulo]):
    for modulo in modulos:
        assert_contains(resp, modulo.descricao)


def test_titulo_aulas(resp, aulas: list[Aula]):
    for aula in aulas:
        assert_contains(resp, aula.titulo)


def test_aulas_links(resp, aulas: list[Aula]):
    for aula in aulas:
        assert_contains(resp, aula.get_absolute_url())
