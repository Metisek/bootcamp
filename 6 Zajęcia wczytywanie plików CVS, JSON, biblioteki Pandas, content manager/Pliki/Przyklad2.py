myFile = open("przyklad1.txt")

linie = myFile.readlines()

myFile.close()

poprawne_linie = list()

czyZaczynamyOdczyt = False

for linia in linie:
    if czyZaczynamyOdczyt:
        poprawne_linie.append(linia)
    if ":" in linia:
        czyZaczynamyOdczyt = True