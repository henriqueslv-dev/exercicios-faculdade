rendimentomensal = float(input("Digite seu rendimento mensal: "))
numerodependentes = float(input("Digite o numero de dependentes: "))
valorpensaoaliment = float(input("Digite o valor da pensão alimentícia: "))
outrasdeducoes = float(input("Digite o valor de outras deduções: "))
deducaopordependente = 189.59

basedecalculo = rendimentomensal - ((deducaopordependente * numerodependentes) + valorpensaoaliment + outrasdeducoes)
print(f"Sua base de calculo é: {basedecalculo: .2f}")

#faixa de rendimento alíquota:

print("CALCULO DO IMPOSTO:")
print(" - Faixa 1: Alíquota de 0% com renda até 1.903,98")
print(" - Faixa 2: Alíquota de 7,5% com renda até 2.826,65")
print(" - Faixa 3: Alíquota de 15,0% com renda até 3.751,05")
print(" - Faixa 4: Alíquota de 22,5% com renda até 4.664,68")
print(" - Faixa 5: Alíquota de 27,5% com renda acima de 4.664,68")

#calculo do imposto

if basedecalculo <= 1903.98:
    imposto = (0/100) * basedecalculo
    print(f"Você se enquadra na faixa 1, seu IMPOSTO É: {imposto: .2f}")

elif basedecalculo <= 2826.65:
    imposto = (7.5/100) * basedecalculo     
    print(f"Você se enquadra na faixa 2, seu IMPOSTO É: {imposto: .2f}")

elif basedecalculo <= 3751.05:
    imposto = (15/100) * basedecalculo
    print(f"Você se enquadra na faixa 3, seu IMPOSTO é: {imposto: .2f}")

elif basedecalculo <= 4664.68:
    imposto = (22.5/100) * basedecalculo
    print(f"Você se enquadra na faixa 4, seu IMPOSTO é: {imposto: .2f}")

else:
    imposto = (27.5/100) * basedecalculo
    print(f"Você se enquadra na faixa 5, seu IMPOSTO é: {imposto: .2f}")

#calculo da aliquota efetiva

aliquotaefetiva = imposto/basedecalculo
print(f"A alíquota efetiva é : {aliquotaefetiva: .2f} ")
