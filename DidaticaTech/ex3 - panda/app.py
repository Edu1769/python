import pandas as pd #Panda cria tabelas
import numpy as np #Numpy cria arrays

#Isso é um dicionario, coloco parametros e dentro do parametros coloco valores
alunos= {"nome":["Otavio","Gabriel","Ricardo","Carlo"],
        "notas":[4, 7.6, 8, 5],
        "aprovado":["não", "sim", "sim", "não"]}

dataframe = pd.DataFrame(alunos) #DataFrame cria uma tabela vertical
print(dataframe)
print("~"*100)

#Função Series cria uma tabela vertical (unidimensional) 
objeto1 = pd.Series([2, 6, 9, 10, 5]) 
print(objeto1)
print("~"*100)

#--------------------------ex--------------------------------#
array1 = np.array([6, 5, 2, 15, 10])
array2 = np.array([(1, 3, 6, 5, 0),(26, 8, 1, 12, 1)])
print(array1)
print(array2)
print("~"*100)
#Transformando essa array em tabela:

objeto2 = pd.Series(array1)
print(objeto2)

#--------------------------fim--------------------------------#