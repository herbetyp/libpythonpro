from libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario
import pytest


class EnviadorMock(Enviador):

    def __init__(self):
        super().__init__()
        self.qtd_email_enviados = 0
        self.param_de_envio = None

    def enviar(self, remetente, destinatario, assunto, corpo):
        self.param_de_envio = (remetente, destinatario, assunto, corpo)
        self.qtd_email_enviados += 1


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
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'renzo@python.pro.br',
        'Curso Python Pro',
        'Confira os módulos fantástico'
    )
    assert len(usuarios) == enviador.qtd_email_enviados


def test_param_de_spam(sessao):
    usuario = Usuario(nome='Renzo', email='renzo@python.pro.br')
    sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'herbetyp@gmail.com',
        'Curso Python Pro',
        'Confira os módulos fantástico'
    )
    assert enviador.param_de_envio == (
        'herbetyp@gmail.com',
        'renzo@python.pro.br',
        'Curso Python Pro',
        'Confira os módulos fantástico'
    )
