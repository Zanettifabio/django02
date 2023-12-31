import pytest
from django.urls import reverse
from model_mommy import mommy

from pypro02.django_assertions import assert_contains, assert_not_contains


@pytest.fixture
def resp(client, db):
    return client.get(reverse('login'))


@pytest.fixture
def resp_home(client, db):
    return client.get(reverse('base:home'))


@pytest.fixture
def resp_home_com_usuario_logado(client_com_usuario_logado, db):
    return client_com_usuario_logado.get(reverse('base:home'))


@pytest.fixture
def usuario(django_user_model, db):
    usuario_modelo = mommy.make(django_user_model)
    senha = 'senha'
    usuario_modelo.set_password(senha)
    usuario_modelo.save()
    usuario_modelo.senha_plana = senha
    return usuario_modelo


@pytest.fixture
def resp_post(client, usuario):
    return client.post(reverse('login'), {'username': usuario.email, 'password': usuario.senha_plana})


def test_status_code(resp):
    assert resp.status_code == 200


def test_login_redirect(resp_post):
    assert resp_post.url == reverse('modulos:indice')
    assert resp_post.status_code == 302


def test_botao_entrar(resp_home):
    assert_contains(resp_home, 'Entrar')


def test_link_botao_entrar(resp_home):
    assert_contains(resp_home, reverse('login'))


def test_botao_entrar_indisponivel(resp_home_com_usuario_logado):
    assert_not_contains(resp_home_com_usuario_logado, 'Entrar')


def test_link_botao_entrar_indisponivel(resp_home_com_usuario_logado):
    assert_not_contains(resp_home_com_usuario_logado, reverse('login'))


def test_botao_sair_disponivel(resp_home_com_usuario_logado):
    assert_contains(resp_home_com_usuario_logado, 'Sair')


def test_nome_usuario_disponivel(resp_home_com_usuario_logado, usuario_logado):
    assert_contains(resp_home_com_usuario_logado, usuario_logado.first_name)


def test_link_logout_disponivel(resp_home_com_usuario_logado):
    assert_contains(resp_home_com_usuario_logado, reverse('logout'))
