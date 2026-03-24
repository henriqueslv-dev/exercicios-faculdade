nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

media = nota1 + nota2 + nota3 + nota4

mediafinal = media / 4
print("A média é: ", mediafinal)

if mediafinal >= 7:
    print("APROVADO.")

elif mediafinal >= 4:
    print("VOCE ESTA DE FINAL.")

else:
    print("REPROVADO.")
