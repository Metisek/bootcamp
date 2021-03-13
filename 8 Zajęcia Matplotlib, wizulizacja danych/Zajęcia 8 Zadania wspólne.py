# # ZAD 1

# import numpy as np
# a = np.loadtxt("pomiary.txt", dtype = int)

# Zad 2

# import numpy as np
# a = np.loadtxt("pomiary.txt", dtype = int) #Wczytywanie pliku
# b = a.max(axis=0) #maxymalna waetoć dla danej kolumny
# c = a.min(axis=0) #minimalna wartoć dla danej kolumny
# d = np.average(a, axis=0) #Średnia dla danej kolumny
# e = np.std(a, axis=0) #Odchylenie standardowe

# print(a, b, c, d, e, sep="\n")

# Zad 2 wykonanie alternatywne

# import numpy as np
# myData = np.loadtxt('pomiary.txt')
# for column in range(myData.shape[1]):
#     print("Column {} analysis:".format(str(column)))
#     print("- maximum value: {}".format(str(max(myData[:, column]))))
#     print("- minimum value: {}".format(str(min(myData[:, column]))))
#     print("- mean value: {}".format(str(np.mean(myData[:, column]))))
#     print("- standard deviation: {}".format(str(np.std(myData[:, column]))))
#     print(30*"-")


# Zad 3

# import numpy as np

# a = np.zeros((5,5))
# b = a.shape[1]
# c = a.shape[0]

# a[0, :] = 1
# a[c-1, :] = 1
# a[:, 0] = 1
# a[:, b-1] = 1

# print(a)

# Zad 4

# import numpy as np
# from random import randint

# a = np.zeros((6, 2), dtype = int)
# b = 0

# if a.size >= 10:
#     while b < 10:
#         c = [randint(0, a.shape[0]-1), randint(0, a.shape[1] - 1)]
#         x, y = c[0], c[1]
#         if a[x, y] != 1:
#             a[x, y] = 1 
#             b += 1 
#         else: continue
#     print(a)
# else: print("Nie da się")

# Zad 5

# import numpy as np
# import matplotlib.pyplot as plt

# a = np.loadtxt("pomiary2.txt", dtype = int, skiprows = 1, usecols =[x for x in range(1,25)])
# daty = np.genfromtxt('pomiary2.txt', usecols = list(range(1,25)), skip_footer=31, dtype = np.str_)
# godziny = [x for x in range(1, 25)]
# plt.figure(figsize=(18,6))
# plt.plot(godziny, a[0, :])
# plt.plot(godziny, a[1, :])
# plt.legend(daty[0:2])
# plt.show()

# Zad 6

# import matplotlib.pyplot as plt
# import requests

# req = requests.get("https://api.exchangeratesapi.io/history?start_at=2021-02-01&end_at=2021-03-01").json()
# data = req["rates"]
# y = []
# x = []

# for d in data:
#     x.append(d)
# for val in x:
#     y.append(data[val]["PHP"])
# plt.figure(figsize=(24,6))

# plt.plot(x, y)
# plt.xlabel("DATA")
# plt.ylabel("KURS")
# plt.show()

# Zad 7


