""" Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:"""

nota_parc1 = float(input("Digite sua nota da prova 1: "))                           #Pede as notas das avaliações parciais 1 e 2, com nota máxima limitada em 10, e minimo 0;
while nota_parc1 > 10 or nota_parc1 < 0:
    if nota_parc1 > 10:
        print("ERROR. NOTA MÁXIMA 10")
    elif nota_parc1 < 0:
        print("ERROR. NÃO SÃO PERMITIDAS NOTAS MENORES QUE 0 (ZERO)")
    nota_parc1 = float(input("Digite novamente sua nota da prova 1: "))


nota_parc2 = float(input("Digite sua nota da prova 2: "))
while nota_parc2 > 10 or nota_parc2 < 0:
    if nota_parc2 > 10:
        print("ERROR. NOTA MÁXIMA 10")
    elif nota_parc2 < 0:
        print("ERRO. NÃO SÃO PERMITIDAS NOTAS MENORES QUE 0 (ZERO)")
    nota_parc2 = float(input("Digite novamente sua nota da prova 2: "))   

media = ((nota_parc1 + nota_parc2)/2)                                               #Faz o cálculo da média, e mostra na tela para o usuário;
print(f"sua média é: {media:.2f}")

if media >= 9 and media <= 10:
    conceito = "A"
elif media >= 7.5 and media < 9:
    conceito = "B"                                                                   #Define o conceito da nota A,B,C,D ou E;
elif media >= 6 and media < 7.5:
    conceito = "C"
elif media >= 4 and media < 6:
    conceito = "D"
else:
    conceito = "E"

print(f"Você se enquadra em: {conceito}")

if conceito in ["A", "B", "C"]:                                                        #Usando a lista define se foi aprovado ou reprovado.
    print("APROVADO")
else:
    print("REPROVADO")
