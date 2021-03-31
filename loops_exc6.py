# Napisati program koji učitava realan broj x i ceo nenegativan broj n i izračunava n-ti stepen broja x.
# U slučaju neispravnog unosa ispisati odgovarajuću poruku o grešci.
# Zadatak rešiti bez korišćenja aritmetičkog operatora **.

# Unesite redom brojeve x i n: 4 3
# Rezultat: 64.00000


prvi_broj = int(input("Unesite prvi broj: "))
drugi_broj = int(input("Unesite drugi broj: "))

if prvi_broj < 0:
    print("Prvi broj mora biti pozitivan broj!")
else:
    rezultat = 1
    for b in range(drugi_broj):
        rezultat *= prvi_broj
    print(rezultat)


