numeros = []

for i in range(5):
    numero = int(input(f"Informe o {1+i}º número:"))
    numeros.append(numero)

par = [num for num in numeros if  num % 2 == 0]
impar = [num for num in numeros if num % 2 != 0]
if par:
    print(f"O maior número par dessa lista é:{max(par)}")
else:
    print("Não há números pares nessa lista.")

if impar:
    print(f"O menor número ímpar dessa lista é:{min(impar)}")
else:
    print("Não há números ímpares nessa lista.")

soma = sum(numeros)
media = soma / len(numeros)

print(f"A soma dos números dessa lista é: {soma}")
print(f"A média dos números dessa lista é: {media:.2f}")
