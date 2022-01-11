import forca
import adivinhacao
def escolha():
    print("#" * 35)
    print("\t\t JOGOS PYTHON3")
    print("#" * 35)

    print("1 - Forca, 2 - Adivinhação")
    jogo = int(input("Digite sua escola: "))

    if (jogo == 1):
        forca.jogar()
    elif (jogo == 2):
        adivinhacao.jogar()
if (__name__ == "__main__"):
    escolha()