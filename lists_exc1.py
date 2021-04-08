# U prodavnici se nalaze artikli čije su cene pozitivni realni brojevi.
# Napisati program koji učitava cene artikala sve do unosa broja nula i izračunava i ispisuje prosečnu vrednost cena u radnji.
# U slučaju neispravnog unosa, ispisati odgovarajuću poruku o grešci.
#
# Unesite cene: 8 5.2 6.11 3 0
# print("Prosecna cena: 5.5775{}")

cena_artikala = []

while True :
    try:
        cena = float(input("Unesite cenu artikla: "))
        cena_artikala.append(cena)
        if cena == 0:
           break
    except ValueError : print("Pogresan unos, pokusajte ponovo")
print(cena_artikala)

zbir_cena = 0
prosek = 0
for c in cena_artikala:
    zbir_cena += c
    prosecna_cena = zbir_cena / (len(cena_artikala) - 1)
    prosek = '{:.2f}'.format(prosecna_cena)
# print(zbir_cena)
print(f"Prosecna cena aritikala u prodavnici je {prosek}")
