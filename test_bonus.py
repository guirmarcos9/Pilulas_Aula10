from bonus import calcular_bonus


def test_bonus_excelente():
    assert calcular_bonus(1000, "Excelente") == 200.0


def test_bonus_bom():
    assert calcular_bonus(1000, "Bom") == 100.0


def test_bonus_regular():
    assert calcular_bonus(1000, "Regular") == 20.0


def test_bonus_ruim_ou_invalido():
    assert calcular_bonus(1000, "Ruim") == 0.0
    assert calcular_bonus(1000, "Mais ou Menos") == 0.0


def test_bonus_salario_negativo():
    assert calcular_bonus(-1000, "Excelente") == 0.0