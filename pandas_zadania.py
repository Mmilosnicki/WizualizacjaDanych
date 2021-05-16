import numpy as np
import pandas as pd
import openpyxl
import xlrd

# zadanie 1

# data = pd.read_excel('imiona.xlsx', header=0)
# df = pd.DataFrame(data)
# print(df)

# zadanie 2

# print(df[df['Liczba'] > 1000])

# print(df[df['Imie'] == 'MATEUSZ'])

# print(df['Liczba'].sum())

# print(df[(df['Rok'] >= 2000) & (df['Rok'] <= 2005)].agg({'Liczba': ['sum']}))

# print('Suma urodzonych chlopcow: ')
# print(df[df['Plec'] == 'M'].agg({'Liczba': ['sum']}))
# print('Suma urodzonych dziewczynek: ')
# print(df[df['Plec'] == 'K'].agg({'Liczba': ['sum']}))



# zadanie 3

# df = pd.read_csv('zamowienia.csv', header=0, sep=';', decimal='.')
# print(df)

# print(df['Sprzedawca'].unique())


# grupa = df.groupby(['Sprzedawca']).agg({'idZamowienia': ['count']})
# print(grupa)

# grupa = df.groupby(['Kraj']).agg({'idZamowienia': ['count']})
# print(grupa)

# rok = pd.DatetimeIndex(df['Data zamowienia']).year

# grupa = df.where((df['Kraj'] == 'Polska') & (rok == 2005)).groupby(['Sprzedawca']).agg({'idZamowienia': ['count']})
# print(grupa)


