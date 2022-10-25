# Napisati program koji od korisnika zahteva da unosi brojeve. Kada korisnik unese nulu,
# prekida se unos i program prikazuje maksimalni i minimalni broj od svih unetih.
n = 1
min = 100000
max = 0

n = int(input("Broj -> "))
min = n
max = n

while(n != 0):
    n = int(input("Broj -> "))
    max = n if n > max else max
    min = n if n < min and n != 0 else min

print("Max broj je -> " + str(max) + ", Min broj je -> " + str(min))