qntprodutos = int(input("Quantos produtos você quer registrar? : "))
caixaA = 0
caixaB = 0
for i in range(qntprodutos):
    produtos = input("Qual produto você quer registrar? : ")

    numerodeserie = int(input("Digite o número de série: "))

    if numerodeserie % 2 == 0:
        caixaA += 1
        print(f"O produto: {produtos}, vai para caixa A.")
    else:
        caixaB += 1
        print(f"O produto: {produtos}, vai para caixa B.")

print(f"Na caixa A tem: {caixaA} produtos.")
print(f"Na caixa B tem: {caixaB} produtos.")
