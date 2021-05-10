import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xlrd
import openpyxl

# zadanie 1
# df = pd.read_excel('imiona.xlsx', header=0)
# print(df)
#
# grupa = df.groupby(['Rok']).agg({'Liczba':['sum']})
#
# wykres = grupa.plot()
# plt.show()

# zadanie 2
# df = pd.read_excel('imiona.xlsx', header=0)
# print(df)
#
# grupa = df.groupby(['Plec']).agg({'Liczba':['sum']})
#
# wykres = grupa.plot.bar()
# plt.xticks(rotation=0)
# plt.title('Ilość urodzonych kobiet i mężczyzn')
# plt.show()

# zadanie 3
# df = pd.read_excel('imiona.xlsx', header=0)
# print(df)
#
# # nie wiem jak dodać warunek na ostatnie 5 lat
# grupa = df.groupby(['Rok']).agg({'Liczba':['sum']})
#
# wykres = grupa.plot.pie(subplots=True, autopct='%.2f %%', fontsize=8, figsize=(6, 6), legend=(0, 0))
# plt.legend(loc='lower right')
# plt.show()


