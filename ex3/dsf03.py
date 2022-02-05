import random

alun1 = input("Digite o nome do 1º aluno: ")
alun2 = input("Digite o nome do 2º aluno: ")
alun3 = input("Digite o nome do 3º aluno: ")
alun4 = input("Digite o nome do 4º aluno: ")

alunos = [alun1, alun2, alun3, alun4]
aleatorio = random.choice(alunos)
print("Aluno sorteado foi: ", aleatorio)
 