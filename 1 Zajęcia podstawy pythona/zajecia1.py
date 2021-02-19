# Rodzaje zmiennych w Pythonie

liczba = 22 # liczba całkowita (integer)
liczba2 = 4.6 # liczba zmiennoprzecinkowa (float)
imie = "Mateusz" # łańcuch znaków (string)
logiczna = True  # Zmienna logiczna (boolean)
# lista = [1, 2.0, "tekst"] # Lista (list)
krotka = (1, 3.0, "to jest krotka") # Krotka (tuple)
zbiory = {1, 2, 3, 4, 5, 6} # Zbiór (set) (nie można mieć 2 tych samych wartosci)
slownik = {"pies":"dog", "kot":"cat"} # Słownik (dictionary)

# Liczenie

a = 8
b = 4
c = -2

# print(a+b)
# print(a-b)
# print(a/b)
# # Modulo z liczby
# print(a%b)
# # Reszta z dzielenia, zaokraglane do liczby calkowitej
# print(a//b)
# print(a*b)
# # Potęgowanie
# print(a**b)
# # Pierwiastkowanie
# print(a**(1/2))
# # Wartosć bezwzględna
# print(abs(c))

# Komentowanie zaznaczonego tekstu ctrl + 1

# Podstawianie

nazwa = "Jan" + " oraz " + "Kowalski" 
znaczek = 30*"xXx"

do_wstawienia = 15
komunikat1 = "Mam xxx lat"
print(komunikat1)
print(komunikat1.replace("xxx", str(do_wstawienia)))
komunikat1 = "Mam {} lat i mam na imię {}".format(do_wstawienia, imie)
print(komunikat1)

# Formatowanie

tekst = 'To jest przykładowe zdanie do nauki Pythona'
print(tekst)
print(tekst.casefold())
print(tekst.endswith('Pythona'))
print(tekst.count('a'))
print(tekst.find('jest'))
print(tekst.title())
print(tekst[4])
print(slownik["kot"])

# Operacje na listach

# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(lista[3])
# lista.append(10)
# lista.insert(0, 10)
# print(lista)
# print(lista.count(1))
# print(lista.index(6))
# lista.pop(5)
# print(lista)

#Porównianie list, zbiorów

# A = {1, 2, 3, 4, 5, 6, 7, 8}
# B = {2, 4, 6, 8}
# A.add(9)
# print(B.difference(A))
# print(B.intersection(A))
# print(B.union(A))

# Funkcje (podstawowe)

# a = 6
# print(8+7, "sdfds,",a)
# print(type(a))
# b = str(a)
# print(type(b))
# c = float(a)
# print(type(c))
# d = (1, 2, 3)
# e = list(d)
# print(e, type(e))
# # haslo = input("Hasło: ")
# print(min(d))
# print(max(d))
