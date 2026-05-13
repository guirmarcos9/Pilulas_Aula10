def acao_semaforo(cor: str) -> str:
    cor = cor.lower()

    if cor == "vermelho":
        return "Pare"
    elif cor == "amarelo":
        return "Atenção"
    elif cor == "verde":
        return "Siga"
    else:
        return "Cor inválida"