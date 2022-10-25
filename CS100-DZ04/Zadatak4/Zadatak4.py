# Napisati zadatak koji od korisnika zahteva da unese ceo broj n. Nakon toga izračunava
# aritmetičku sredinu svih parnih brojeva do n

n = int(input("Ceo broj -> "))

totalNumbers = 0
sumNumbers = 0

for x in range(1, n + 1):
    if x % 2 == 0:
        totalNumbers += 1
        sumNumbers = sumNumbers + x

print("Aritmeticka sredina je -> " + str(sumNumbers / totalNumbers))