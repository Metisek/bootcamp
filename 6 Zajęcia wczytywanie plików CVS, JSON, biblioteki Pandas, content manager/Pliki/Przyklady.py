

myFile = open(r'C:\Users\User\Projekty\bootcamp\6 Zajęcia wczytywanie plików CVS, JSON, biblioteki Pandas, content manager\Pliki\przyklad1.txt')

print(myFile.mode)
linia = myFile.readline()
print(linia)
linia = myFile.readline()
print(linia)
linia = myFile.readline()
print(linia)

myFile.close()


myFile = open(r'C:\Users\User\Projekty\bootcamp\6 Zajęcia wczytywanie plików CVS, JSON, biblioteki Pandas, content manager\Pliki\przyklad1.txt')

print(myFile.mode)
linia = myFile.readline()
print(linia)
linia = myFile.readline()
print(linia)
linia = myFile.readline()
print(linia)
linie = myFile.readlines()
countLines = len(linie)
myFile.close()


myFile = open('przyklad1.txt')

for _ in range(countLines):
    linia = myFile.readline()
    print(linia)
    
myFile.close()

myFile = open(r'C:\Users\User\Projekty\bootcamp\6 Zajęcia wczytywanie plików CVS, JSON, biblioteki Pandas, content manager\Pliki\przyklad1.txt', mode='r')
print("Tryb pracy:", myFile.mode)
myFile.close()

myFile = open(r'C:\Users\User\Projekty\bootcamp\6 Zajęcia wczytywanie plików CVS, JSON, biblioteki Pandas, content manager\Pliki\przykladdodatnia1.txt', mode='w')
print("Tryb pracy:", myFile.mode)
myFile.close()

myFile = open('przyklad1.txt')
for line in myFile.readlines():
    print(line)
myFile.close()