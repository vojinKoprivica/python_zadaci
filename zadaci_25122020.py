# prvi nacin - najgluplji
# number = int(input("Molim vas unesite broj dana u nedelji: "))
# print(number)
# weekday = ["Ponedeljak"
#            "Utorak"
#            "Sreda"
#            "Cetvrtak"
#            "Petak"
#            "Subota"
#            "Nedelja"
#            ]
#
# if number == 1:
#     print("Ponedeljak")
# elif number == 2:
#     print("Utorak")
# elif number == 3:
#     print("Sreda")
# elif number == 4:
#     print("Cetvrtak")
# elif number == 5:
#     print("Petak")
# elif number == 6:
#     print("Subota")
# elif number == 7:
#     print("Nedelja")
# else:
#     print("neispravan unos")
# print()
# print(50 * "=")
# drugi nacin

# for n in :
#     if n:
#         print("izabrani dan je : " + {weekday[number]})
#     else :
#         print("Neispravan unos")


print(50*"-")
print()

#DRUGI ZADATAK

# godina = int(input("UNESITE GODINU: "))
# mesec = int(input("UNESITE MESEC: "))
#
# if mesec == 1:
#     print("Januar, 31 dan")
# elif mesec == 2:
#     if godina % 400 == 0 or (godina % 4 == 0 and godina % 100 != 0):
#         print("Februar, 29 dana")
#     else:
#         print("Februar, 28 dana")
# elif mesec == 3:
#     print("Mart, 31 dan")
# elif mesec == 4:
#     print("April, 30 dana")
# elif mesec == 5:
#     print("Maj, 31 dan")
# elif mesec == 6:
#     print("Jun, 30 dana")
# elif mesec == 7:
#     print("Jul, 31 dan")
# elif mesec == 8:
#     print("Avgust, 31 dan")
# elif mesec == 9:
#     print("Septembar, 30 dana")
# elif mesec == 10:
#     print("Oktobar, 31 dan")
# elif mesec == 11:
#     print("Novembar, 30 dana")
# elif mesec == 12:
#     print("Decembar, 31 dan")
# else :
#     print("Neispravan unos")

#Danijelov nacin


# def num_days(month, year):
#     mapping = {1:"Januar", 2:"Februar",3:"Mart",4:"April",5:"Maj",6:"Jun",7:"Jul",8:"Avgust",9:"Septembar",10:"Oktobar",11:"Novembar",12:"Decembar"}
#     if month not in range(1,13):
#         print("Please input number in correct range")
#     else:
#         if month in [1,3,5,7,8,10.12]:
#             print(f"{mapping[month]}, 31 dan")
#         elif month in [4,6,9,11]:
#             print(f"{mapping[month]}, 30 dana")
#         elif month == 2 and (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)):
#             print(f"{mapping[month]}, 29 dana - ova godina je prestupna")
#         else:
#             print(f"{mapping[month]}, 28 dana")
#
#
#
# month = int(input("Koji je mesec? "))
# year = int(input("Koja je godina? "))
#
# try:
#     num_days(int(month),int(year))
# except:
#     print("Invalid input")