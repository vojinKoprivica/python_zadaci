# Napisati program koji učitava ceo broj n, a zatim n puta ispisuje tekst: “Mi volimo da programiramo”.
# U slučaju neispravnog unosa, ispisati odgovarajuću poruku o grešci.
# Napomena: Pretpostaviti da je tip unetog broja tačan.

while True :
    try:
        broj = input("Unesite zeljeni broj: ")

        for n in broj:
            print("Mi volimo da programiramo!\n" * int(broj))
        break
    except ValueError : print("Pogresan unos")

    