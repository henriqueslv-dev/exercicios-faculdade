print("1=PEDRA, 2=PAPEL, 3=TESOURA")
player = int(input("PEDRA, PAPEL OU TESOURA?:"))


import random

pc = random.randint(1, 3)

if pc == 1:
    print("PC:PEDRA")

if pc == 2:
    print("PC:PAPEL")

if pc == 3:
    print("PC:TESOURA")

if pc == 1 and player == 1:
    print("EMPATE")

elif pc == 1 and player == 2:
    print("PLAYER VENCEU.")

elif pc == 1 and player == 3:
    print("PC VENCEU.")

if pc == 2 and player == 1:
    print("PLAYER VENCEU.")

elif pc == 2 and player == 2:
    print("EMPATE.")

elif pc == 2 and player == 3:
    print("PLAYER VENCEU.")

if pc == 3 and player == 1:
    print("PLAYER VENCE")

elif pc == 3 and player == 2:
    print("PC VENCEU.")

