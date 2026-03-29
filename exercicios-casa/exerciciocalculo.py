"""11. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
a. o produto do dobro do primeiro com metade do segundo .
b. a soma do triplo do primeiro com o terceiro."""

I1 = int(input("Digite um número inteiro: "))
I2 = int(input("Digite mais um número inteiro: "))
R = float(input("Digite um número real: "))

cond1 = (I1 * 2) * (I2/2)
cond2 = (I1 * 3) + R

print("o produto do dobro do primeiro com metade do segundo é : ", cond1)
print("a soma do triplo do primeiro com o terceiro: ", cond2)
