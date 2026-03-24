num1 = int(input("Digite o primeiro numero:"))
num2 = int(input("Digite o segundo numero:"))

opcao = str(input("Informe a operação:"))
if opcao == "soma":
    soma = num1 + num2
    print("soma:",soma)

elif opcao == "multiplicacao":
    multiplicacao = num1 * num2
    print("multiplicação:", multiplicacao)


elif opcao == "divisao":
    divisao = num1 / num2
    print("divisão:",divisao)

elif opcao == "subtracao":
    subtracao = num1 - num2
    print("subtração:", subtracao)

else:
    print("escolha entre as opções: soma, multiplicacao, divisao, subtração")
