from math import pow, sqrt

CatetoAdj = float(input("Digite o Cateto adjacente: "))
CatetoOpos = float(input("Digite o Cateto oposto: "))

hipotenusa = sqrt(pow(CatetoAdj,2)+ pow(CatetoOpos,2))

print("A soma dos catetos {} e {} ao quadrado é igual a hipotenusa ao quadrado {}" .format(CatetoAdj, CatetoOpos, hipotenusa))