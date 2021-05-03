# Napisati funkciju razlomljeni_deo() koja izračunava razlomljeni deo broja x.
# Napisati program koji učitava jedan realan broj i ispisuje njegov razlomljeni deo na šest decimala.

def razlomak():
    number = float(input("Unesite zeljeni broj: "))
    rez = abs(number - int(number))
    return format(rez,'.6f')

print(razlomak())