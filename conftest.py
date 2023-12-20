import pytest
from model_mommy import mommy


@pytest.fixture
def usuario_logado(django_user_model):
    usuario_modelo = mommy.make(django_user_model, first_name='Fulano')
    return usuario_modelo


@pytest.fixture
def client_com_usuario_logado(client, usuario_logado):
    client.force_login(usuario_logado)
    return client
