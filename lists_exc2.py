n = int(input("Unesite broj cifara: "))
cifre = []
if n <= 0:
    print("Neispravan unos")
else:
    k = 0
    for m in range(n):
        b = float(input("Unesite zeljene cifre: "))
        cifre.append(b)
        # if b < 0:
        #     negativno += 1
        # else:
        #     pozitivno +=1
    promena = 0
    prosla = 1
    for br in cifre:
        if br == 0:
            sign = -1
        else:
            sign = br/abs(br)
            # print(sign)
        if sign == -prosla:
            promena += 1
            prosla = sign
    print(promena)





