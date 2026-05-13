from frete import calcular_frete


def test_frete_peso_zero_ou_negativo():
    assert calcular_frete(0) == 0.0
    assert calcular_frete(-10) == 0.0


def test_frete_ate_um_kg():
    assert calcular_frete(0.5) == 5.0
    assert calcular_frete(1.0) == 5.0


def test_frete_acima_de_um_ate_cinco_kg():
    assert calcular_frete(1.01) == 10.0
    assert calcular_frete(5.0) == 10.0


def test_frete_acima_de_cinco_kg():
    assert calcular_frete(5.01) == 18.0
    assert calcular_frete(10) == 18.0