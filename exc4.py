# Napisati program koji za uneti pozitivan trocifreni broj ispisuje njegove cifre jedinica, desetica i stotina.
# Napomena: Pretpostaviti da je unos ispravan, tj. da je uneti broj zaista trocifren.
#
# Unesite trocifreni broj: 697
# Cifra jedinica: 7
# Cifra decetica: 9
# Cifra stotina: 6

broj = int(input("Please type a three digits number : "))

prva_cifra = broj % 10
druga_cifra = (broj//10) % 10
treca_cifra = broj//100
print(f"jedinica : {prva_cifra}")
print(f"desetica : {druga_cifra}")
print(f"stotine : {treca_cifra}")


