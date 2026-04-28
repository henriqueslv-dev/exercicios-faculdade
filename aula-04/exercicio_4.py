quantidade = int(input("Digite a quantidade de alunos: "))
abaixo_media = 0
acima_media = 0
for i in range(quantidade):
    nota = int(input(f"Digite a nota do {1 + i}º aluno:"))
    while nota > 100:
        print("Nota inválida.")
        nota = int(input(f"Digite novamente a nota do {1 + i}º aluno:"))
    if nota < 60:
        abaixo_media += 1
    else:
        acima_media += 1

print(f"A quantidade de alunos acima da média é: {acima_media}")
print(f"A quantidade de alunos abaixo da média é: {abaixo_media}")

