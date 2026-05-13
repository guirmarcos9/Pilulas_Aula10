def calcular_bonus(salario_base: float, avaliacao: str) -> float:
    if salario_base < 0:
        return 0.0

    if avaliacao == "Excelente":
        return salario_base * 0.20
    elif avaliacao == "Bom":
        return salario_base * 0.10
    elif avaliacao == "Regular":
        return salario_base * 0.02
    else:
        return 0.0