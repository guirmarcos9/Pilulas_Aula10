def converter_nota_para_conceito(nota: float) -> str:
    if nota < 0 or nota > 10:
        return "Nota inválida"
    elif nota >= 9:
        return "A"
    elif nota >= 7:
        return "B"
    elif nota >= 5:
        return "C"
    elif nota >= 3:
        return "D"
    else:
        return "F"