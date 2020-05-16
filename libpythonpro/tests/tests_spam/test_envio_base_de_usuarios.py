from libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario
from unittest.mock import Mock
import pytest


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Herbety', email='herbetyp@gmail.com'),
            Usuario(nome='Paulo', email='paulo@email.com')
        ],
        [
            Usuario(nome='Herbety', email='herbetyp@gmail.com'),
        ]
    ]
)
def test_qtd_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'renzo@python.pro.br',
        'Curso Python Pro',
        'Confira os módulos fantástico'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_param_de_spam(sessao):
    usuario = Usuario(nome='Renzo', email='renzo@python.pro.br')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'herbetyp@gmail.com',
        'Curso Python Pro',
        'Confira os módulos fantástico'
    )
    enviador.enviar.assert_called_once_with(
        'herbetyp@gmail.com',
        'renzo@python.pro.br',
        'Curso Python Pro',
        'Confira os módulos fantástico'
    )
