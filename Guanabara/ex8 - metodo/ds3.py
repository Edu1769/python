from time import sleep

def maior(*num):
    cont = maior = 0
    print("\n Analisando os valores passador...")
    for valor in num:
        print(f"{valor}", end="", flush=True)
        sleep(0.2)

maior(2, 4, 8, 9, 0)
maior(4, 7, 0)
maior(1, 1, 2)