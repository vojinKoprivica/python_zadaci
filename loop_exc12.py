# Napisati program koji učitava pozitivan ceo broj n, a potom i n celih brojeva.
# Izračunati i ispisati zbir onih brojeva koji su istovremeno neparni i negativni.
# U slučaju neispravnog unosa ispisati odgovarajuću poruku o grešci.
#
# Unesite broj n: 5
# Unesite n brojeva: 1 -5 -6 3 -11
# Zbir neparnih i negativnih: -16

pozitivan_broj = int(input("Unesite pozitivan broj: "))

if pozitivan_broj < 0:
    print("Neispravan unos")
else:
    lista_brojeva = []
    for n in range(pozitivan_broj):
        brojevi = int(input("Unesite zeljene brojeve: "))
        lista_brojeva.append(brojevi)
# print(lista_brojeva)

    rez = 0
    for t in lista_brojeva:
        if t < 0 and t % 2 != 0:
            rez += t
    print(f"Zbir neparnih negativnih je: {rez}")



