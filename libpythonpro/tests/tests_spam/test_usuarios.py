from libpythonpro.spam.db import Conexao
from libpythonpro.spam.modelos import Usuario
import pytest


@pytest.fixture
def conexao():
    return Conexao()


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Herbety')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(sessao):
    usuarios = [Usuario(nome='Herbety'), Usuario(nome='Paulo')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
