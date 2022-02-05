from tokenize import Double


nome = input ("digite seu nome: ")
idade = int (input ("digite sua idade: "))
peso = float (input ("Digite seu peso: "))

# print("Bem vindo", nome, "Idade:", idade, "Peso:", peso)
print("Bem vindo {} Idade: {} Peso: {}" .format(nome, idade, peso))