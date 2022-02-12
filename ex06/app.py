lanche = ("Hamburguer", "Suco", "Pizza", "Pudim") # As tuplas(arrays) são imutaveis ou seja não podem ser mudadas, e elas usam parenteses ()
print(lanche[1])

comida = ["Hamburguer", "Suco", "Pizza", "Pudim"] # As listas são mutaveis ou seja podem ser mudadas, e elas usam colchetes []
comida[3] = "Sorvete"

comida.append("Cookie") # Serve para adicionar um elemento no final da lista 
comida.insert(0,"Arroz") # Adiciona um elemento no lugar descrito 
del comida[0] # Elemina o elemento também pode se utilizar: comida.remove["Arroz"]
print(comida)

valores = [8,4,2,4,5,6,9,0]
valores.sort() # Ordena a lista
print(valores)