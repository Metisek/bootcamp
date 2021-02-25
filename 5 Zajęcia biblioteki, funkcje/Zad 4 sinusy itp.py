from math import sin, cos, tan
# Wyliczanie sinusa, cosinusa, tangensa z wartosci danego kąta.
def trygo(znak):
    znak = znak.casefold()
    if znak == "sinus" or znak == "sin":
        def f(kat):
            return(sin(kat))
        return f
    elif znak == "cosinus" or znak == "cos":
        def f(kat):
            return(cos(kat))
        return f
    elif znak == "tangens" or znak == "tg":
        def f(kat):
            return(tan(kat))
        return f
    else: return False

tryg = trygo(input("Podaj funkcję trygonometryczną: (sin)us, (cos)inus, tangens (tg): "))
if tryg != False:
    print(tryg(int(input("Podaj kąt do wyliczenia funkcji trygonometrycznej podanej wcześniej: "))))
print(sin(30), sin(45), sin(60))
print(tan(30), tan(45), tan(60))
