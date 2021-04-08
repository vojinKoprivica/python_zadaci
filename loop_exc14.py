# Napisati program koji za uneti ceo broj proverava i ispisuje da li se cifra 5 nalazi u njegovom zapisu.
#
# Unesite broj: 1857
# Broj 1857 sadrzi cifru 5.
# Broj x ne sadrzi cifru 5.

broj = int(input("Unesite zeljeni broj: "))
cifre = []
pomocna_prom = broj

while pomocna_prom > 0:
    cifre.append(pomocna_prom%10) # nacin kako da iteriramo kroz visecifreni broj
    pomocna_prom //= 10

contains_5 = False
for cifra in cifre:
    if cifra == 5:
        contains_5 = True

if contains_5:
    print(f"Broj 5 se nalazi u broju {broj}")
else:
    print(f"Broj 5 se ne nalazi u broju {broj}")