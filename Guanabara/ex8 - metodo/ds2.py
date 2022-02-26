def linha (texto):
    print("~" * (len(texto)+4))
    print(f"  {texto} ")
    print("~" * (len(texto)+4))

escreva = input("\n Digite uma frase: ")
linha(escreva)