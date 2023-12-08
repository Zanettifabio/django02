import pytest
from pypro02.django_assertions import assert_contains
from django.urls import reverse
from model_mommy import mommy
from pypro02.modulos.models import Modulo


@pytest.fixture
def modulo(db):
    return mommy.make(Modulo)


@pytest.fixture
def resp(client, modulo: Modulo):
    resp = client.get(reverse('modulos:detalhe', kwargs={'slug': modulo.slug}))
    return resp


def test_titulo_do_modulo(resp, modulo: Modulo):
    assert_contains(resp, modulo.titulo)


def test_publico_do_modulo(resp, modulo: Modulo):
    assert_contains(resp, modulo.publico)


def test_descricao_do_modulo(resp, modulo: Modulo):
    assert_contains(resp, modulo.descricao)
