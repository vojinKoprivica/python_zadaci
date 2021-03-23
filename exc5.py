# Napisati program koji za uneti pozitivan četvorocifreni broj računa njegove cifre jedinica, desetica i stotina a potom ispisati najveću cifru.
# Program takođe treba ispisati grešku ukoliko uneti broj nije četvorocifren.
# Test primeri:
#
# Unesite cetvorocifreni broj: 6835
# Najveca cifra: 8

while type(True):
    broj = int(input("unesite zeljeni cetvorocifreni broj: "))
    try:
        if broj < 1000 or broj > 9999:
            print("neispravan unos, broj mora biti cetvorocifren")
            break
    except ValueError: print("Sorry, pogresan input")

    else:
        jedinica = broj % 10
        desetica = (broj % 100) // 10
        stotina = (broj // 100) % 10
        hiljada = broj // 1000
        print(f"Jedinica : {jedinica} \
                      Desetica : {desetica} \
                      Stotina : {stotina} \
                      Hiljada : {hiljada}"
                    )

        a = 0
        if jedinica > desetica :
            a = jedinica
                    # print(f"Najveci broj je {jedinica}")
        elif jedinica == desetica:
            a = jedinica
                    # print(f"Najveci broj je {jedinica}")
        else:
             a = desetica
                    # print(f"Najveci broj je {desetica}")

        if stotina > hiljada :
            b = stotina
                # print(f"Najveci broj je {b}")
        elif stotina == hiljada:
            b = stotina
                    # print(f"Najveci broj je ")
        else:
            b = hiljada

        if a > b:
            print(f"Najveci broj u cifri je {a}")
        elif a==b:
            print(f"Najveci broj u cifri je {b}")
        else:
            print("Najveci broj u cifri je {b}")
else:
    print("Wrong input!")




