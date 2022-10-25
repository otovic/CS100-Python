# Napisati zadatak koji od korisnika zahteva da unese jedan ceo broj manji od 20, n. Nakon toga
# program ispisuje sve brojeve do unetog broja n, ali tako da se svaki broj ponavlja onoliko puta
# kolika mu je vrednost.
# Primer za n=5:
# 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5

n = int(input("Ceo broj manji od 20 -> "))

outputStr = ""

if n > 20 and n < 1:
    print("Broj mora biti manji od 20 i veci od 0!")
else:
    for x in range(1, n + 1):
        for y in range(x):
            outputStr = outputStr + str(x) + " "

print(outputStr)