# Napisati program koji učitava nenegativan ceo broj n i izračunava njegov faktorijel.
# U slučaju neispravnog unosa ispisati odgovarajuću poruku o grešci.

# n = int(input("Unesite pozitivan broj: "))
# f = 1
#
# if n <= 0 :
#     print("Unestie pozitivan broj!")
# else:
#     for i in range(1,n+1):
#         f = i*f
#         print(f"faktorijel broja {n} je: {f}")

print("\n")

# Napisati program koji učitava realan broj x i ceo nenegativan broj n i izračunava n-ti stepen broja x.
# U slučaju neispravnog unosa ispisati odgovarajuću poruku o grešci.
# Zadatak rešiti bez korišćenja aritmetičkog operatora **.
#
# x = input("unesite zeljeni realan broj: ")
# n = int(input("Unesite zeljeni pozitivan broj: "))
# x = float(x)
#
# if n <= 0 or x < 0:
#     print('Unesite pozitivan broj razlicit od nule: ')
# else:
#      x1 = 1
#      for r in range(n):
#         x1 *= x
#      print(f"Rezultat kvadriranja je: {x1}")
# r = 1
# while r <= n:
#     x1=x*(r*r)
#     print(print(f"{n} stepen broja {x} je: {x1}") )
#     break
# else:
#     rez = 1
#     for r in range(n):
#         rez *= x
#     print(f"rezultat: {rez}")


# Pravi delioci celog broja su svi delioci osim jedinice i samog tog broja.
# Napisati program koji za uneti pozitivan ceo broj n ispisuje sve njegove prave delioce.
# U slučaju neispravnog unosa ispisati odgovarajuću poruku o grešci.

# br = int(input("Unesite zeljeni broj veci od nule: "))

# pravi_delioci = []
#
# if br < 0:
#     print("Neispravan unos. Pokusajte ponovo")
# else:
#
#     for i in range(2, br):
#         if br % i == 0:
#             pravi_delioci.append(i)
#     print(*pravi_delioci)

### drugi pristup :
#
# br1 = int(input("Unesite zeljeni broj veci od nule: "))
#
# if br1 < 0:
#      print("Neispravan unos. Pokusajte ponovo")
# else:
#     x =" ".join([str(i) for i in range (2,br1) if br1 % i == 0])
#     print(*x)

# Napisati program koji za uneti ceo broj ispisuje broj dobijen uklanjanjem svih nula sa desne strane unetog broja.
#
# Unesite broj: 12000
# Rezultat: 12

# n1 = int(input("uneti zeljeni broj: "))
#
# privremena_promenljiva = n1
#
# while privremena_promenljiva % 10 == 0 and privremena_promenljiva != 0:
#     privremena_promenljiva //= 10
# print(privremena_promenljiva)

### drugi pristup

