from time import sleep


def contador(i, f, p):

    if i<f:
        while i <= fim:
            print(f"{i} ", end="", flush=True)
            sleep(0.3)
            i = i+p
    else:
        while i >= fim:
            print(f"{i} ", end="", flush=True)
            sleep(0.3)
            i = i-p
    

inicio = int(input("Digite o valor inicial: "))
fim = int(input("Digite o valor final: "))
passo = int(input("Digite o passo: "))

contador(inicio, fim, passo)