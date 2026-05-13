from semaforo import acao_semaforo


def test_semaforo_vermelho_deve_retornar_pare():
    assert acao_semaforo("vermelho") == "Pare"


def test_semaforo_amarelo_deve_retornar_atencao():
    assert acao_semaforo("amarelo") == "Atenção"


def test_semaforo_verde_deve_retornar_siga():
    assert acao_semaforo("verde") == "Siga"


def test_semaforo_cor_invalida():
    assert acao_semaforo("azul") == "Cor inválida"