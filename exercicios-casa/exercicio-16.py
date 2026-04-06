""" Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa
deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
a. Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
b. Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre oprograma;
c. Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
d. Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;"""

A = float(input("Informe o valor de A: "))
if A == 0:
    print("0 NÃO CONDIZ COM EQUAÇÃO DE SEGUNDO GRAU. PROGRAMA ENCERRADO.")
else:
    B = float(input("Informe o valor de B: "))
    C = float(input("Informe o valor de C: "))

    delta = ((B ** 2) - 4 * A * C)

    if delta < 0:
        print("Essa equação não possui raizes reais. PROGRAMA ENCERRADO.")
    elif delta == 0:
        X1 = -B  / (2 * A)
        print(f"Essa equação possui uma raiz real: {X1: .2f}")
    else:
        X1 = (-B + delta ** 0.5) / (2 * A) 
        X2 = (-B - delta ** 0.5) / (2 * A)
        print(f"A equação possui duas raizes reais: {X1: .2f}, {X2: .2f}")
