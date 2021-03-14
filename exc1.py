# Napisati program koji pomaže kasirki da obračuna kusur koji treba da vrati kupcu.
# Za unetu cenu artikla, količinu artikla i iznos koji je kupac dao, program treba da ispiše vrednost kusura.
# Sve ulazne vrednosti su pozitivni celi brojevi. Napomena: Pretpostaviti da je unos ispravan.

# print("Verzija Jedan...")
#

proizvodi_kg = dict(jabuka = 220,
                    kruska = 100,
                    sljiva = 150,
                    kajsija = 300)

while True :
    try :
        izabrani_proizvod = input(f"Izaberite zeljeni proizvod: ")
        if izabrani_proizvod in proizvodi_kg.values():
            continue
    except ValueError:
        print("Molim vas ponovite unos proizvoda: ")
    else :
        cena = proizvodi_kg.get(izabrani_proizvod)
        kolicina = input("Unesite kolicinu: ")
        cena_kupovine = cena*int(kolicina)
        print(f"Cena vaseg proizvoda iznosi: {cena_kupovine} ")
        uplata = input("Uplacen iznos: ")
        kusur = int(uplata) - int(cena_kupovine)
        print(f"Vas kusur iznosi: {kusur}")
        break
    finally:
        print("Hvala na kupovini!")
    # print(proizvodi_kg.get(izabrani_proizvod))

