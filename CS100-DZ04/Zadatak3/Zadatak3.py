# Napisati zadatak koji od korisnika zahteva da unese donju i gornju granicu, n i m. Nakon toga
# prebrojava koliko ima brojeva deljivih sa 3 i 5 unutar unetih granica.

n = int(input("Donja granica -> "))
m = int(input("Gornja granica -> "))

counter = 0

if n > m:
    print("Unesite ispravne granice!")
else:
    for x in range(n, m + 1):
        if x % 3 == 0 and x % 5 == 0:
            counter += 1
    print(counter)
