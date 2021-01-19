# trocifreni_broj = int(input("Molim vas unesite troficfreni broj: "))
#
# jedinica = trocifreni_broj % 10
# desetica = (trocifreni_broj//10) % 10
# stotina = trocifreni_broj // 100
#
# print(f"Stotina : {stotina}, Desetica: {desetica}, Jedinica: {jedinica}")


#Napisati program koji za uneti pozitivan cetvorocifreni broj racuna njihove cifre jedinica, desetica i stotina a potom ispisati najvecu cifru
print(50*"-")
broj = int(input("Molim vas unesite cetvorocifreni broj: "))

jedinica = broj % 10
desetica = (broj//10) % 10
stotina = (broj // 100) % 10
hiljada = broj // 1000

if broj < 1000 or broj > 9999:
    print("Uneti broj nije cetvorocifren")
#Obrnuti broj
print(50*"-")

rev_numb = 0

while broj > 0:
    ostatak = broj%10 # ostatak od unetog broja
    rev_numb = (rev_numb*10)+ostatak # u prvoj iteraciji 0*10 + ostatak
    broj = broj//10

print(f"Obrnuti broj je : {rev_numb}")

obrnuti_broj = jedinica*1000 + desetica*100 + stotina*10 + hiljada
print(obrnuti_broj)

print(50*"-")
#Test broj : 8209

#poredjenje parova brojeva:

if jedinica > desetica:
    jedinica_vs_desetica = jedinica
else:
    jedinica_vs_desetica = desetica

if stotina > hiljada:
    stotina_vs_hiljada = stotina
else:
    stotina_vs_hiljada = hiljada
if jedinica_vs_desetica > stotina_vs_hiljada:
    print(f"Najveca cifra je : {jedinica_vs_desetica}")
else:
    print((f"Najveca cifra je : {stotina_vs_hiljada}"))




# print(f"Stotina : {stotina}, Desetica: {desetica}, Jedinica: {jedinica}")