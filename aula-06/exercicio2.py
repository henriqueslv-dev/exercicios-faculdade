quant = int(input("Digite a quantidade de números na lista:"))
lis = []
lista_ord_crec  = []

for i in range(quant):
    num = int(input(f"Digite o {i + 1}º número:"))
    lis.append(num)

contador_crec = int()
for i in range(len(lis)):
    contador_crec = lis[0]
    for j in range(len(lis)):
        if lis[j] <= contador_crec:
            contador_crec = lis[j]

    lista_ord_crec.append(contador_crec) 
    lis.remove(contador_crec)

print(lista_ord_crec)
