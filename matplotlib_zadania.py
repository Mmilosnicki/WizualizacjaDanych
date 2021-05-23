import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import openpyxl
import xlrd

# zadanie 1

# x = np.arange(20, 41, 1)
# y = 1 / x
#
# plt.plot(x, y, label='f(x)')
# plt.axis([20, 40, 0.02, 0.05])
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.legend()
#
# plt.show()

# zadanie 2

# x = np.arange(20, 41, 1)
# y = 1 / x
# #
# plt.plot(x, y, 'bo--')
# plt.axis([20, 40, 0.02, 0.05])
# plt.xlabel('x')
# plt.ylabel('1/x')
# plt.title('Wykres funkcji f(x) dla x[20,40]')
#
# plt.show()

# zadanie 3

# x = np.arange(0, 45, 0.1)
# s = np.sin(x)
# c = np.cos(x)
#
# plt.plot(x, s, label='sin(x)')
# plt.plot(x, c, label='cos(x)')
# plt.legend()
# plt.show()

# zadanie 4

# x = np.arange(0, 45, 0.1)
# s = np.sin(x)
# y = (np.sin(x) + 2) * -1
#
# plt.plot(x, s, label='sin(x)')
# plt.plot(x, y, label='sin(x)')
# plt.xlabel('x')
# plt.ylabel('sin(x)')
# plt.title('Wykres sin(x), sin(x)')
# plt.legend(loc='center left')
#
# plt.show()

# zadanie 7
# df = pd.read_csv("zamowienia.csv", header=0, sep=';', decimal='.')
# print(df)
#
# grupa = df.groupby(['Sprzedawca']).agg({'idZamowienia': ['count']})
#
# explode = (0, 0, 0.1, 0, 0, 0.1, 0, 0, 0.1)
# wykres = grupa.plot.pie(subplots=True, autopct='%.2f %%', fontsize=10, figsize=(6, 7), shadow=True, explode=explode)
# plt.legend(title='Sprzedawcy', loc='lower left', bbox_to_anchor=(-0.2, -0.2))
#
# plt.show()
