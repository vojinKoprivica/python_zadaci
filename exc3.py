# Napisati program koji za unetu godinu i mesec ispisuje naziv meseca kao i koliko dana ima u tom mesecu te godine.
# U slučaju neispravnog unosa ispisati odgovarajuću poruku o grešci.
# Napomena: Godina je prestupna kada je deljiva sa 400 ili kada je deljiva sa 4 a nije deljiva sa 100.

# Output format = Januar, 31 dan

try:
    godina = input("Unesite godinu: ")
    mesec = int(input("Unesite mesec: "))

    if mesec == 1:
        print("Januar, 31 dan")
    elif mesec == 2:
        if int(godina) % 400 == 0:
            print("Februar, 29 dana")
        else:
            print("Februar, 28 dana")
    elif mesec == 3:
        print("Mart, 31 dan")
    elif mesec == 4:
        print("April, 30 dana")
    elif mesec == 5:
        print("Maj, 31 dan")
    elif mesec == 6:
        print("Jun, 30 dana")
    elif mesec == 7:
        print("Jul, 31 dan")
    elif mesec == 8:
        print("Avgust, 31 dan")
    elif mesec == 9:
        print("Septembar, 30 dana")
    elif mesec == 10:
        print("Oktobar, 31 dan")
    elif mesec == 11:
        print("Novembar, 30 dana")
    elif mesec == 12:
        print("Decembar, 31 dan")
except:
    ValueError : print("Pogresan unos")