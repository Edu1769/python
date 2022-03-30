import pandas as pd

alunos= {"nome":["Otavio","Gabriel","Ricardo","Carlo"],
        "notas":[4, 7.6, 8, 5],
        "aprovado":["não", "sim", "sim", "não"]}

alunosDF = pd.DataFrame(alunos)
print(alunosDF["aprovado"]) #printa a coluna escolhida
print("~"*100)

#------------------------------------------------------------#
print(alunosDF.loc[[0,2]])# printa a linha dos seguintes indices (nesse caso 0 e 2)
print("~"*100)
#------------------------------------------------------------#

print(alunosDF.loc[alunosDF["notas"]==8])# printa a linha que tiver a nota 8