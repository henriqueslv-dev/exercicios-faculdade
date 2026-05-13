n = int(input("Informe o valor do n: "))


for i in range(1, n + 1):
    espaços = (n - i)
    controle = (i * 2)
    print(" " * espaços + "X" * controle)
