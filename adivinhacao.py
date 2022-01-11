import random
def jogar():
    print("#" * 35)
    print("\t\t JOGO DA ADIVINHAÇÃO")
    print("#" * 35)

    numero_secreto = random.randrange(1, 101)
    total_tentativas = int(5)
    pontos = 100


    print("Escolha o nível de dificuldade: ")
    print("1 - Fácil", "2 - Médio ", "3 - Difícil", sep="\n")
    nivel = int(input())

    if (nivel == 1):
        total_tentativas = 10
    elif (nivel == 2):
        total_tentativas = 5
    else:
        total_tentativas = 3

    while (total_tentativas > 0):
        chute = int(input("Digite seu chute: "))
        pontos_perdidos = abs(numero_secreto - chute)
        acertou = chute == numero_secreto
        eh_maior = chute > numero_secreto
        eh_menor = chute < numero_secreto
        if (acertou):
            print("Você acertou!!!!!\t Sua pontuação foi {} pontos.".format(pontos))
            break
        elif (eh_maior):
            print("Você chutou mais alto :(")
            pontos -= pontos_perdidos
        elif (eh_menor):
            print("Você chutou mais baixo :(")
            pontos -= pontos_perdidos
        total_tentativas -= 1

        print("Restam: {}".format(total_tentativas))

    print("#" * 35)
    print("\t\tFIM DO JOGO", end="\n")
    print("#" * 35)

if (__name__ == "__main__"):
    jogar()