import pandas as pd
import os

os.system('cls' if os.name == 'nt' else 'clear')
print("="*100)

dados = pd.read_excel('C:/Users/eduar/Desktop/programas/python/DidaticaTech/ex14 - panda/exemplo.xlsx')


dados2 = pd.read_csv('C:/Users/eduar/Desktop/programas/python/DidaticaTech/ex14 - panda/athlete_events.csv')
print(dados2.head(5))
