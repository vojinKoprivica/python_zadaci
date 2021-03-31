# Napisati program koji za uneti ceo broj ispisuje broj dobijen uklanjanjem svih nula sa desne strane unetog broja.
#
# Unesite broj: 12000
# Rezultat: 12

broj = int(input("Unesite zeljeni broj: "))

# rezultat = str(broj).strip("0")
# print(rezultat)

rez = broj
while rez % 10 == 0 and rez != 0:
    rez //= 10
print(rez)


