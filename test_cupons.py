from cupons import aplicar_cupom


def test_cupom10_qualquer_valor():
    assert aplicar_cupom("CUPOM10", 50.0) == 0.10
    assert aplicar_cupom("CUPOM10", 200.0) == 0.10


def test_cupom10_minusculo():
    assert aplicar_cupom("cupom10", 100.0) == 0.10


def test_cupom25_valido():
    assert aplicar_cupom("CUPOM25", 150.0) == 0.25


def test_cupom25_invalido_por_valor_baixo():
    assert aplicar_cupom("CUPOM25", 50.0) == 0.0


def test_descontovip_valido():
    assert aplicar_cupom("DESCONTOVIP", 600.0) == 0.35


def test_descontovip_invalido_por_valor_baixo():
    assert aplicar_cupom("DESCONTOVIP", 400.0) == 0.0


def test_cupom_invalido():
    assert aplicar_cupom("CUPOM_FALSO", 1000.0) == 0.0