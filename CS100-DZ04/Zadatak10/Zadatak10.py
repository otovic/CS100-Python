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
        if x == 0 or x == n - 1: #Pitamo da li je prvi ili zadnji red, ako jeste popunjavamo ceo red sa x
            outputStr = outputStr + "x"
        else: # Ako je bilo koji drugi red ulazi u else
            if y == 0 or y == n - 1: # Pitamo da li je kolona 1 ili zadnja kolona, ako jesu upisujemo x
                outputStr = outputStr + "x"
            else: # Ako nisu upisujemo razmak
                outputStr = outputStr + " "
        outputStr = outputStr + " "
    outputStr = outputStr + "\n" # Posle svakog prolaza dodajemo novi red
print(outputStr)

