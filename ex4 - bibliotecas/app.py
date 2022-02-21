import random
from turtle import color 

frase = input("Digite uma frase: ")
taman = len(frase)
aleat = random.randint(0, taman)
print(" ===========================================")
print("   Letra sorteada da sua frase: ", frase[aleat].upper())
print("   Quantidade de letras", frase[aleat].upper(), "Na sua frase:", frase.count(frase[aleat]))
print(" ===========================================")