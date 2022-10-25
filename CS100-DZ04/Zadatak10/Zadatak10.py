# Napisati program koji od korisnika zahteva da unese broj n koji je manji od 10 i iscrtava
# karakter x po obodu matrice. Matrica je kvadratna, ima n vrsta i n kolona.
# Primer n = 5
# x x x x x
# x       x
# x       x
# x       x
# x x x x x

n = int(input("Broj veci od 0 i manji od 10 -> "))
outputStr = ""

for x in range(n):
    for y in range(n):
        if x == 0 or x == n - 1:
            outputStr = outputStr + "x"
        elif x > 0 and x < n - 1:
            if y == 0 or y == n - 1:
                outputStr = outputStr + "x"
            else:
                outputStr = outputStr + " "
        outputStr = outputStr + " "
    outputStr = outputStr + "\n"
print(outputStr)

