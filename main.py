from src.dados import carregar_dados
from src.calculos import calcular_media_idade

def main():
    dados = carregar_dados()
    media = calcular_media_idade(dados)
    print("Média de idade:", media)

if __name__ == "__main__":
    main()
