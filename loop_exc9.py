# Napisati program koji učitava ceo broj i ispisuje njegove cifre u obrnutom poretku.

# Unesite ceo broj: 6789
# Rezultat: 9876

broj = int(input("Unesite zeljeni broj: "))

cifre = []

if broj < 0:
    broj = abs(broj)
# print(broj)

for n in str(broj):
    cifre.append(n)
    rez = cifre[::-1]
    # cifre.append(b)
    # break
    rezultat = "".join(map(str,rez))
print(rezultat)

