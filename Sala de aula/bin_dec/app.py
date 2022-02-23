import math
import os

i=0
dec = 0
base = [1,2,4,8,16,32,64,128]
binario = [0,0,0,0,0,0,0,0]

os.system('cls' if os.name == 'nt' else 'clear')
print("="*20)
print(" [1] Dec -> Bin")
print(" [2] Bin -> Dec")
print(" [3] Dec -> hexa")

escolha = int(input("escolha: "))

os.system('cls' if os.name == 'nt' else 'clear')

if escolha == 1:
    decimal = int(input("Digite um numero: "))
    print(f"{decimal} -> ", end="")
    while i < 7:
        binario[i] = decimal % 2
        decimal = math.trunc(decimal/2)
        i= i+1
    while i >= 0:
        print(binario[i], end="")
        i-=1

elif escolha == 2:
    binario = input("Digite um numero binario: ")
    i = len(binario)-1
    cont =0
    while i > 0:
        if binario[i] == "1":
            dec = dec+base[cont]
        i-=1
        cont+=1
    print(f"{binario} -> {dec}")

elif escolha == 3: 
    decimal = int(input("Digite um numero: "))
    while decimal %16 != 0:
        i= decimal%16
        print(i, end="")
        decimal = math.trunc(decimal/16)
        # Falta inverter
    