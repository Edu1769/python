import random

aleat = random.randint(0, 5)
Nescolhido = int(input("Sorteie um numero entre 0 e 5: "))

if Nescolhido == aleat:
    print ("Parabéns vc acertou o numero [{}]" .format(Nescolhido))
else:
    print ("Você errou!! o numero aleatorio foi:", aleat)