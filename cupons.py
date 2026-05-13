def aplicar_cupom(codigo_cupom: str, valor_compra: float) -> float:
    codigo = codigo_cupom.upper()

    if codigo == "CUPOM10":
        return 0.10
    elif codigo == "CUPOM25" and valor_compra > 100:
        return 0.25
    elif codigo == "DESCONTOVIP" and valor_compra > 500:
        return 0.35
    else:
        return 0.0