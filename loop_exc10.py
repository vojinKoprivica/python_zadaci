# Napisati program koji za uneti pozitivan ceo broj ispisuje da li je on deljiv sumom svojih cifara.
# U slučaju neispravnog unosa, ispisati odgovarajuću poruku o grešci.
#
# Unesite broj: 12
# Broj 12 je deljiv sa 3.
#
# Unesite broj: -4
# Greska: neispravan unos.
#
# Unesite broj: 2564
# Broj 2564 nije deljiv sa 17.
#
# Unesite broj: 0
# Greska: neispravan unos.

broj = int(input("Unesite zeljeni pozitivan ceo broj: "))

zbir_cifara = 0

if broj > 0:
    for n in str(broj):
        zbir_cifara += int(n)
    if broj % zbir_cifara == 0:
        print(f"{broj} je deljiv sa {zbir_cifara}")
    else:
        print(f"{broj} nije deljiv sa {zbir_cifara}")
else:
    print("Pogresan unos, broj mora biti veci od 0")

# print(zbir_cifara)