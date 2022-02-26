def voto(a):
    idade = 2022 - a
    if idade>=18 and idade <=80:
        print(f"Você tem {idade} e o Voto é obrigatorio")
    elif idade<18:
        print(f"Você tem {idade} e Não vota")
    else:
        print(f"Você tem {idade} e o Voto é opicional")

ano = int(input("Digite o ano de seu nascimento: "))
voto(ano)