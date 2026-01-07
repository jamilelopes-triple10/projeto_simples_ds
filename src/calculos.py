def calcular_media_idade(dados):
    return sum(p["idade"] for p in dados) / len(dados)
