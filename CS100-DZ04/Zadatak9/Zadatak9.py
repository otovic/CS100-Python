# Napisati program koji od korisnika zahteva da unosi brojeve. Kada korisnik unese broj koji je
# manji od trenutnog broja negativnih brojeva, prekida se unos i program prikazuje koliko je bilo
# unetih negativnih brojeva.
# Npr. 1 2 -5 -2 1 stopira se unos (broj negativnih do ovog trenutka je 2, a novi uneti broj je 1

negativeNumbers = 0
condition = True

while(condition):
    x = int(input("Broj -> "))
    if x < 0:
        negativeNumbers += 1
    elif x > 0 and negativeNumbers != 0:
        condition = True if x > negativeNumbers else False

print("Ukupan broj negativnih brojeva -> " + str(negativeNumbers))
    
    