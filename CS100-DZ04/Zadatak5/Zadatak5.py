# Napisati zadatak koji od korisnika zahteva da unese pozitivan ceo broj n, a nakon toga
# izračunava njegov faktorijel koristeći petlje.
# Faktorijel se računa na sledeći način: 4! = 1 x 2 x 3 x 4 = 24

n = int(input("Pozitivan broj -> "))

x = 1
sum = 1

if n < 1:
    print("Broj mora biti pozitivan!")
else:
    while(x < n + 1):
        sum = sum * x
        x += 1
    print(sum)