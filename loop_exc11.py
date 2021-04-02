# Knjigovođa vodi evidenciju o transakcijama jedne firme i treba da napiše izveštaj o godišnjem poslovanju te firme.
# Firma je tokom godine imala t transakcija.
# Transakcije su predstavljene celim brojevima i u slučaju da je vrednost transakcije pozitivna, ta transakcija označava prihod firme,
# a u slučaju da je negativna rashod.
# Napisati program koji učitava ceo broj t i podatke o t transakcija i zatim izračunava i ispisuje ukupan prihod, rashod i
# zaradu odnosno gubitak koji je firma ostvarila tokom godine.
# U slučaju neispravnog unosa ispisati odgovarajuću poruku o grešci.
# Unesite broj t: 7
# Unesite transakcije:
# 8 -50 45 2007 -67 -123 14
# Prihod: 2074
# Rashod: -240
# Zarada: 1834

t = int(input("Unesite broj transakcija: "))

if t < 0:
    print("Pogresan unos transakcija")
elif t == 0:
    print("Nema evidentiranih transakcija")
else:
    transakcije = []
    prihod = 0
    rashod = 0
    zarada = 0
    for n in range(t):
        transakcija = int(input("Unesite vrednost transakcije: ")) #ispisace unos transakcije n puta
        transakcije.append(transakcija)
    # print(transakcije)
    for tran in transakcije:
        if tran >= 0:
            prihod += tran
        else:
            rashod += tran
        zarada = prihod - abs(rashod)

# print(transakcije)
    print(f"Prihod firme u protekloj godini iznosio je : {prihod}")
    print(f"Rashod firme u protekloj godini iznosio je: {rashod}")
    if zarada < 0:
        print(f"Firma je poslovala u minusu. Iznos minusa je : {zarada}")
    elif zarada == 0:
        print("Firma je poslovala u pozitivnoj 0")
    else:
        print(f"Firma je poslovana u plusu. Iznos plusa je : {zarada}")


