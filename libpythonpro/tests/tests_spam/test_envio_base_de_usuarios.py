from libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario
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
def test_qtd_de_span(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Enviador()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'renzo@python.pro.br',
        'Curso Python Pro',
        'Confira os módulos fantástico'
    )
    assert len(usuarios) == enviador.qtd_email_enviados
