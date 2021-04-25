import numpy as np
# zad1
# a = np.array([13, 37, 22])
# b = np.array([5, 7, 34])
# c = a * b
# print(c)

# zad2
# d = np.arange(9).reshape(3, 3)
# print(d)
# print("")
# e = np.arange(16).reshape(4, 4)
# print(e)
#
# print("")
#
# print(d.min(axis=1))
# print(d.min(axis=0))
# print("")
# print(e.min(axis=1))
# print(e.min(axis=0))

# zad3
# a = np.array([13, 37, 22])
# b = np.array([5, 7, 34])
# print(a)
# print(b)
# c = b.reshape(3, 1)
# print(c)
# print(a.dot(c))

# zad4
# a = np.array([9, 9, 7], dtype='int')
# b = np.array([1.8, 4.2, 6.3], dtype='float')
# print(a)
# print(b)
# print("")
# print(a * b)

# zad5
# x = np.array([[9, 9, 7], [4, 2, 0]])
# a = np.sin(x)
# print(a)

# zad6
# y = np.array([[9, 9, 7], [4, 2, 0]])
# b = np.cos(y)
# print(b)

# zad7
# # macierze z zadania 5 i 6
# print(a + b)

# zad8
# a = np.arange(9).reshape(3, 3)
# for x in range(3):
#     print(a[x, :])
#     print("")

# zad9
# a = np.arange(9).reshape(3, 3)
# print(a)
# for x in a.flat:
#     print(x)
#     print("")

# zad11
# a = np.arange(12)
# b = a.reshape(3, 4)
# c = a.reshape(4, 3)
# d = a.reshape(2, 6)
#
# print(a)
# print("")
# print(b)
# print("")
# print(c)
# print("")
# print(d)
# print("")
#
# print(b.ravel())
# print(c.ravel())
# print(d.ravel())