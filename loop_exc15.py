# Napisati program koji učitava cele brojeve sve do unosa broja nula, a zatim izračunava i ispisuje aritmetičku sredinu unetih brojeva
# na četiri decimale.
#
# Unesite brojeve: 8 5 6 3 0
# Aritmeticka sredina: 5.5000
#
# Unesite brojeve: 0
# Nisu uneti brojevi.


brojevi = []

while True :
    broj = int(input("Unesite zeljeni broj: "))
    brojevi.append(broj)
    # print(brojevi)
    if broj == 0:
        break
if len(brojevi) == 1:
    print("Nisu uneti brojevi")
else:
    rez = 0
    aritmeticka_sredina = 0
    for n in brojevi:
        rez += n
        aritmeticka_sredina = rez / len(brojevi)
    # print(rez)
    rezultat = float(aritmeticka_sredina)
    rez_decimal = "{:.4f}".format(rezultat)

    print((rez_decimal))



