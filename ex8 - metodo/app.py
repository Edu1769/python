def dobre (lst_valor):
    i = 0
    while i < len(lst_valor):
        lst_valor[i] = lst_valor[i]* 2
        i+=1
        
valores = [8, 0, 6, 7, 5]
dobre(valores)
print(valores)