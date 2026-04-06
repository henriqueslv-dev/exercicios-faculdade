lado1 = int(input("Digite o valor do primeiro lado: "))  
while lado1 <= 0:
    lado1 = int(input("Digite novamente o valor do primeiro lado: "))  
                                        
lado2 = int(input("Digite o valor do segundo lado: "))
while lado2 <= 0:
    lado2 = int(input("Digite novamente o valor do segundo lado: "))  

lado3 = int(input("Digite o valor do terceiro lado: "))
while lado3 <= 0:
    lado3 = int(input("Digite novamente o valor do terceiro lado: "))  


while (lado1 + lado2) < lado3 or (lado2 + lado3) < lado1 or (lado1 + lado3) < lado2:
    print("Os valores selecionados NÃO podem formar um triângulo")
    lado1 = int(input("Digite novamente o valor do primeiro lado: "))       
    while lado1 <= 0:
        lado1 = int(input("Digite novamente o valor do primeiro lado: "))

    lado2 = int(input("Digite novamente o valor do segundo lado: "))  
    while lado2 <= 0:
        lado2 = int(input("Digite novamente o valor do segundo lado: "))       

    lado3 = int(input("Digite novamente o valor do terceiro lado: "))
    while lado3 <= 0:
        lado3 = int(input("Digite novamente o valor do terceiro lado: "))

print("Os valores selecionados podem formar um triângulo")                                  

equilatero = lado1 == lado2 == lado3
isoceles = (lado1 == lado2 or lado1 == lado3 or lado2 == lado3) and not equilatero                             #condições para cada tipo especifico de triangulo
escaleno = lado1 != lado2 and lado1 != lado3 and lado2 != lado3

if equilatero:
    print("Seu triângulo é equilatero.")
elif isoceles:
    print("Seu triângulo é isoceles.")                                                     #print do tipo do seu triangulo
else:
    print("Seu triangulo é escaleno.")
