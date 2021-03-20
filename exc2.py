# Napisati program koji za uneti redni broj dana u nedelji ispisuje ime odgovarajućeg dana.
# U slučaju neispravnog unosa, ispisati odgovarajuću poruku o grešci.
#
# Unesite broj:
# U pitanju je:
# Greska: neispravan unos podataka

try:
    broj = int(input("Unesti broj dana u nedelji: "))
    if broj >= 1:
    # broj = int(input("Unesti broj dana u nedelji: "))
        dan = 0
        if broj == 1:
         dan = "Ponedeljak"
        elif broj == 2:
            dan = "Utorak"
        elif broj == 3:
            dan = "Sreda"
        elif broj == 4:
            dan = "Cetvrtak"
        elif broj == 5:
            dan = "Petak"
        elif broj == 6:
            dan = "Subota"
        elif broj == 7:
            dan = "Nedelja"
        print(f"U pitanju je : {dan}")
    else:
        raise ValueError
except ValueError:
        print("Pogresan unos! Uneta vrednost mora biti broj veci od  0")



