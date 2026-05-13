from notas import converter_nota_para_conceito


def test_nota_conceito_a():
    assert converter_nota_para_conceito(9.0) == "A"
    assert converter_nota_para_conceito(10.0) == "A"


def test_nota_conceito_b():
    assert converter_nota_para_conceito(7.0) == "B"
    assert converter_nota_para_conceito(8.9) == "B"


def test_nota_conceito_c():
    assert converter_nota_para_conceito(5.0) == "C"
    assert converter_nota_para_conceito(6.9) == "C"


def test_nota_conceito_d():
    assert converter_nota_para_conceito(3.0) == "D"
    assert converter_nota_para_conceito(4.9) == "D"


def test_nota_conceito_f():
    assert converter_nota_para_conceito(0) == "F"
    assert converter_nota_para_conceito(2.9) == "F"


def test_nota_invalida():
    assert converter_nota_para_conceito(-1) == "Nota inválida"
    assert converter_nota_para_conceito(11) == "Nota inválida"