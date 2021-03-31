# Pravi delioci celog broja su svi delioci osim jedinice i samog tog broja.
# Napisati program koji za uneti pozitivan ceo broj n ispisuje sve njegove prave delioce.
# U slučaju neispravnog unosa ispisati odgovarajuću poruku o grešci.

# Dakle ako je % broja = 0
#
# Unesite broj n: 100
# Pravi delioci: 2 4 5 10 20 25 50

# Koristimo npr. listu

broj = int(input("Unesite broj: "))

if broj < 1 :
    print("Unesite broj veci od 0")
else:
    rezultat = 1
    for n in range(2,broj):
        if broj % n == 0:
            rezultat = n
            print(f"Pravi delioci {broj} su: {n} ")
