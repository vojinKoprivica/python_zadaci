# Napisati program koji učitava nenegativan ceo broj n a potom ispisuje sve cele brojeve od 0 do n.
# U slučaju neispravnog unosa ispisati odgovarajuću poruku o grešci.
while True:
    try:
        broj = int(input("Unesite zeljeni broj: "))

        if broj < 0:
            print("Pogresan unos, broj mora biti nenegativan!")
        else:
            for n in range(0,broj):
                print(n+1)
            break
    except ValueError : print("Pogresan unos. Uneta vrednost mora biti nenegativan broj")

