import numpy as np

# "main"
# distribuir_navios(mapa), função distribuir navios em um mapa aleatorio
# atacar(mapa_atacante, mapa_defensor), parte de ataque se acertou ou não os ataques
# def criar_mapa(), cria uma função para criar o mapa com apenas uma linha de código


def criar_mapa():
    return np.zeros((10,10))

def mostrar_mapa(mapa):
    print(mapa)

def atacar(mapa_atacante, mapa_defensor):
    X = int(input("Digite o eixo X: "))
    while X > 9 or X < 0:
        print("Erro, essa não é uma posição válida (1 a 9)")
        X = int(input("Digite o eixo X: "))

    Y = int(input("Digite o eixo Y: "))
    while Y > 9 or Y < 0:
        print("Erro, essa não é uma posição válida (1 a 9)")
        Y = int(input("Digite o eixo Y: "))

    if mapa_defensor[X][Y] == 0:
        print("ACERTOU A ÁGUA!")
        mapa_atacante[X][Y] = -1
    else:
        mapa_atacante[X][Y] = mapa_defensor[X][Y]
        print(f"Você acertou um navio de tamanho {mapa_defensor[X][Y]}")

def distribuir_navios(mapa):
    navios = [5, 4, 4, 3, 3, 3, 2, 2]

    for navio in navios:
        mostrar_mapa(mapa)
        X = int(input("Digite o eixo X: "))
        Y = int(input("Digite o eixo Y: "))
        H = int(input("Digite 1 para horizontal e 2 para vertical: "))

        erro = False

        if H == 1:
            for i in range(Y, Y + navio):
                if mapa[X][i] != 0:
                    erro = True
                    print("ERRO. POSIÇÃO INVÁLIDA")

            if erro == False:
                for i in range(Y, Y + navio):
                    mapa[X][i] = navio

        else:
            for i in range(X, X + navio):
                if mapa[i][Y] != 0:
                    erro = True
                    print("ERRO POSIÇÃO INVALIDA.")

            if erro == False:
                for i in range(X, X + navio):
                    mapa[i][Y] = navio


mapa_j1 = criar_mapa()
mapa_j2 = criar_mapa()
mapa_atk_j1 = criar_mapa()
mapa_atk_j2 = criar_mapa()

mapa_j2[0][0] = 2

atacar(mapa_j1, mapa_j2)
mostrar_mapa(mapa_atk_j1)

# validação de posição de navio
# validação de venceu ou perdeu
# enquanto não houver vencedor, o jogo continua

