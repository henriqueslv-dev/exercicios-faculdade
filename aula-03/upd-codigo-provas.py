media = 6.0
avaliacao_1 = float(input("Digite sua nota da avaliação 1: "))
while avaliacao_1 > 5 or avaliacao_1 < 0:
    print("ERRO. nota máxima 5.0")
    avaliacao_1 = float(input("Digite novamente a sua nota da avaliação 1: "))

avaliacao_2 = float(input("Digite sua nota da avaliação 2: "))
while avaliacao_2 > 5 or avaliacao_2 < 0:
     print("ERRO. nota máxima 5.0")
     avaliacao_2 = float(input("Digite novamente a sua nota da avaliação 2: "))

avaliacao_final = 0.0 

if ((avaliacao_1 + avaliacao_2) >= media):                                     # av1 e av2 devem ser maior que media 6 para aprovação aoutomatica;
    print("APROVADO.")                                                         # avF substitui menor nota;
elif (avaliacao_1 < 1 and avaliacao_2 < 1):                                    # and = as duas condições devem ser true; or = uma das condições deve ser true;
    print("REPROVADO")                                                         # fazendo a verificação da nota final mais a soma das av1 ou av2 para ser maior que a média;
else:
    print("Você está de FINAL.")

    avaliacao_final = float(input("Digite sua nota na Final: "))

    if avaliacao_1 < avaliacao_2:
        avaliacao_1 = avaliacao_final

    elif avaliacao_2 < avaliacao_1:
        avaliacao_2 = avaliacao_final

    if ((avaliacao_1 + avaliacao_2) >= media):
        print("APROVADO.")
    else:
        print("REPROVADO")
    
