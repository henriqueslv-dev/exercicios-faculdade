fut = {'Neymar':['Ney 2011', 'Ney 2015', 'Ney 2017', 'Ney 2023', 'Ney 2026']}
fut['Messi'] = ['Messi 2009', 'Messi 2012', 'Messi 2015', 'Messi 2023', 'Messi 2025']
fut['Cristiano'] = ['CR7 2008', 'CR7 2013', 'CR7 2017', ' CR7 2019', 'CR7 2026' ]

print("Os jogadores são: \n Messi \n Neymar \n Cristiano")
print(f"Os modos são:\n {fut['Messi']}\n {fut['Neymar']}\n {fut['Cristiano']}")

modo = input("remova um modo: ")
nome = input("Diga o nome do jogador: ")  

fut[nome].remove(modo)
fut[nome].sort()

for i in fut:
    print(i, fut[i])
