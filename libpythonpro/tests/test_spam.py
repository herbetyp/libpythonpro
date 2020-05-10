from libpythonpro.spam.enviador_de_email import Enviador


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


def test_remetente():
    enviador = Enviador()
    resultado = enviador.enviar(
        'renzo@python.pro.br',
        'luciano@python.pro.br',
        'Curso Python Pro',
        'Turma Luiz Vital'
    )
    assert 'renzo@python.pro.br' in resultado
