# Napisati program koji učitava nenegativan ceo broj n i izračunava njegov faktorijel.
# U slučaju neispravnog unosa ispisati odgovarajuću poruku o grešci.

while True:
    try:
        n = int(input("Unesite zeljeni broj: "))
        a = 1
        for i in range(1,n+1):
            a *= i
        print(a)
        break
    except ValueError:
        print("Neispravan unos")