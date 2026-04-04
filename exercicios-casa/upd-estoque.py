qntprodutos = int(input("Quantos produtos você quer registrar? : "))
while qntprodutos <= 0:
    print("ERRO. PERMITIDOS APENAS NÚMEROS MAIORES QUE 0 (ZERO)")                 #pergunta ao usuario a quantidade de produtos que ele quer registar, e faz a validação se o numero é positivo
    qntprodutos = int(input("Quantos produtos você quer registrar? : "))

caixaA = []
caixaB = []                                                                       # cria a lista com caixaA e caixaB
for _ in range(qntprodutos):
    produtos = input("Qual produto você quer registrar? : ")

    numerodeserie = int(input("Digite o número de série: "))
    while numerodeserie <= 0:
        print("NÚMERO DE SÉRIE DEVE SER MAIOR QUE 0")
        numerodeserie = int(input("Digite novamente o número de série: "))         #faz a validação para numero de serie ser maior que zero

    if numerodeserie % 2 == 0:
        caixaA.append(produtos)
        print(f"O produto: {produtos}, vai para caixa A.")                         #aqui tem a condição de se numero de serie for par vai para Caixa A, e impar caixa B
    else:
        caixaB.append(produtos)
        print(f"O produto: {produtos}, vai para caixa B.")

print(f"Caixa A: {', '.join(caixaA)}")                                            # ".join" junta todos os itens da lista em uma única string, separados por vírgula e espaço
print(f"Caixa B: {', '.join(caixaB)}")
