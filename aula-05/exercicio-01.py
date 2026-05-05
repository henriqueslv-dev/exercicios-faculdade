seq_numeros = input("Digite uma sequência de x números:")
num = []
maior_seq = 1
qnt_valor_conseq = 1


for i in seq_numeros.split(","):
    num.append(i)

num_maior_seq = num[0]


for i in range(1, len(num)):
    
    if num[i] == num[i-1]:
        qnt_valor_conseq = qnt_valor_conseq +1
    else:
        qnt_valor_conseq = 1
    
    if maior_seq < qnt_valor_conseq:
        maior_seq = qnt_valor_conseq
        num_maior_seq = num[i-1]

print("Os numeros da lista são: ", num)
print("A maior sequência de números é: ", maior_seq)
print("O numero que se repete é:",num_maior_seq)
