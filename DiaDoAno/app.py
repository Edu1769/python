dia = int(input("\n Digite um dia: "))
mes = int(input(" Digite um mês: "))
ano = int(input(" Digite um ano: "))

meses = [31, 28, 31, 30, 31, 30 ,31, 31, 30, 31, 30, 31]
quantDias = 0

for i in range(0, mes):
    quantDias = meses[i] + quantDias

print("\n===================================\n")
print(" Data escolhada {}/{}/{}" .format(dia,mes,ano))
print(" Quantidades de dias: {}" .format(quantDias))
print("\n===================================")
