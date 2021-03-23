### NUMPY ###


import numpy as np
# a = np.arange(15).reshape(3, 5)
# print(a)
# print(a.shape)
# print(a.ndim)
# print(a.dtype.name)
# print(a.itemsize)
# print(a.size)
# print(type(a))
# b = np.array([6, 7, 8])
# print(b)
# print(type(b))


# Przykłady tworzenia zmiennych array

# import numpy as np
# a = np.array([2,3,4])
# print(a)
# print(a.dtype)
# b = np.array([1.2, 3.5, 5.1])
# print(b)
# print(b.dtype)
# c = np.array([(1.5,2,3), (4,5,6)])
# print(c)
# print(c.dtype)
# d = np.array( [ [1,2], [3,4] ], dtype=complex )
# print(d)
# print(d.dtype)

# # Przykład błędny

# # a = np.array(1,2,3,4) 

# # Shape manipulation

# myP = np.zeros([3,3,3])
# myP[1][1][1] =1
# print(myP)


# MATPLOTLIB

# Podstawy

# zwykła funckja liniowa

import matplotlib.pyplot as plt
# plt.plot([1, 2, 3, 4])
# plt.ylabel('some numbers')
# plt.show()

# wiązanie listy X i Y. Wywietlaanie punktów

# plt.plot([1, 2, 3, 4, 5.5], [1, 4, 9, 16, 31], 'ro')
# plt.axis([0, 6, 0, 40])
# plt.show()

# Przykład  z funkcją kwadratową 1

# arguments = [x for x in range(-100, 100)]
# plt.plot(arguments, list(map(lambda x: x**2, arguments)))

# Przykład z funckją kwadratową 2

# argu = np.arange(-10., 10., 0.2)
# plt.plot(argu, argu**2, 'b.')
# plt.show()

# Przykład z wykresami

# names = ['group_a', 'group_b', 'group_c']
# values = [1, 10, 100]

# plt.figure(figsize=(9, 7))

# plt.subplot(321)
# plt.bar(names, values)
# plt.subplot(322)
# plt.scatter(names, values)
# plt.subplot(323)
# plt.plot(names, values)
# plt.suptitle('Categorical Plotting')
# plt.show()

# Przykład z sinusami

# def f(t):
#     return np.exp(-t) * np.cos(2*np.pi*t)

# t1 = np.arange(0.0, 5.0, 0.1)
# t2 = np.arange(0.0, 5.0, 0.02)

# plt.figure()
# plt.subplot(211)
# plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

# plt.subplot(212)
# plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
# plt.show()