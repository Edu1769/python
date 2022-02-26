print("=============================================================")
vel = int(input("Digite a velocidade do carro[km]: "))

if vel > 80:
    print("Você foi multado")
    mult = vel - 80
    mult = mult*7
    print("Valor da multa: R${} reais " .format(mult))

else:
    print("Tenha uma boa viagem")
print("=============================================================")