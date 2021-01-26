# 1. Napisati program koji na standardni izlaz ispisuje pet puta rečenicu: “Mi volimo da programiramo”.

# n = 5
# for i in range(n):
#     print("Mi volimo da programiramo!!!")

### drugi nacin preko WHILE

# r = 0
# while r < 5:
#     print("mi volimo da programiramo!!!")
#     r+=1
#
print(50*"-")

# 2. Napisati program koji učitava ceo broj n, a zatim n puta ispisuje tekst: “Mi volimo da programiramo”.
# U slučaju neispravnog unosa, ispisati odgovarajuću poruku o grešci. Napomena: Pretpostaviti da je tip unetog broja tačan.

print(50*"-")

# u = input("unesite zeljeni broj koliko volite programiranje (od 1-5): ")
#
# if u.isdigit():
#     for n in range(int(u)):
#         print("Mi volimo da programiramo!")
# else:
#     print("Neispravan unos! Unesite ispravan broj")

# prvi zadatak sa TRY AND EXCEPT
# try:
#     ulaz = int(ulaz)
#     for n in range(ulaz):
#         print("Mi volimo da programiramo!")
# except:
#     raise TypeError("Neispravan unos, probaj opet")

#3. Napisati program koji učitava nenegativan ceo broj n a potom ispisuje sve cele brojeve od 0 do n.
# U slučaju neispravnog unosa ispisati odgovarajuću poruku o grešci.

# print("***Moje resenje***")
# unos = input("Unesite zeljeni broj: ")
#
# if unos.isdigit() and unos >= "0":
#     unos = int(unos)
#     for n in range(unos+1):
#         print(n)
# else:
#     print("Neispravan unos, broj mora biti nenegativan")


#### Komplikovanije : Try i Except -> ako ne zelim raise Error vec zelim da ostavim poruku

# print("*** Resenje sa radionice ***")
# unos = input("Unesite zeljeni broj: ")
# while True :
#     try:
#         unos = int(unos)
#         if unos <= 0:
#             print("Broj mora biti nenegativan")
#         break
#     except:
#         print("Unet je neispravan format")
#         unos = input("Unesite zeljeni broj: ")
#
# print(' \n'.join([str(i) for i in range(unos+1)]))

# 4. Napisati program koji učitava dva cela broja n i m (n <= m) i ispisuje sve cele brojeve iz intervala [n, m].
# Rešiti zadatak korišćenjem:
# 	a) While petlje
# 	b) For petlje
# U slučaju neispravnog unosa ispisati poruku o grešci.

print("_______Moje resenje________")
n = input("Unesite prvi broj: ")
m = input("Unesite drugi broj: ")
#
# if  n <= m and (n.isdigit() and m.isdigit()):
#     n = int(n)
#     m = int(m)
#     for p in range(n,m+1):
#         print(p)
# else:
#     print("neispravan unos")

while n<m :
    if n.isdigit() and m.isdigit():
        print(n,m)
            break
    else:
        print("Unos mora biti broj!")

print("Prvi broj mora biti manji od drugog")



# print("_______Radionica________")





