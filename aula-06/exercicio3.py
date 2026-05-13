quant = int(input("Digite a quantidade de números na lista:"))
lis = []
lista_ord_dec  = []

for i in range(quant):
    num = int(input(f"Digite o {i + 1}º número:"))
    lis.append(num)

contador_dec = int()
for i in range(len(lis)):
    contador_dec = lis[0]
    for j in range(len(lis)):
        if lis[j] >= contador_dec:
            contador_dec = lis[j]

    lista_ord_dec.append(contador_dec) 
    lis.remove(contador_dec)

print(lista_ord_dec)
