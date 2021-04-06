# Napisati program koji učitava cele brojeve sve do unosa broja nula i ispisuje proizvod onih unetih brojeva koji su pozitivni.
#
# Unesite brojeve: -87 12 -108 -13 56 0
# Proizvod pozitivnih brojeva je 672.

lista_brojeva = []
rezultat = 1
n = 1
while n != 0:
    n = int(input("Unesite brojeve: "))
    lista_brojeva.append(n)
    if n > 0:
        rezultat *= n
print(rezultat)

