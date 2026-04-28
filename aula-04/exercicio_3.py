a = []
print("Digite 10 numeros inteiros.")
for i in range(10):
    numero = int(input(f"Digite o {1 + i}º número inteiro:"))
    a.append(numero)

maior = max(a)
menor = min(a)

print(f"O maior número é:{maior}")
print(f"O menor número é:{menor}")
