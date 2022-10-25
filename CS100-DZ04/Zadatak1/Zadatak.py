# Napisati zadatak koji ispisuje tablicu množenja. Korisnik unosi dva cela broja, n i m, svaki u
# posebnom redu. Na izlazu program štampa tablicu množenja sa n vrsta i m kolona.
# Primer za n=5, m=4.
# 1*1 = 1 1*2 = 2 1*3 = 3 1*4 = 4
# 2*1 = 2 2*2 = 4 2*3 = 6 2*4 = 8
# 3*1 = 3 3*2 = 6 3*3 = 9 3*4 = 12
# 4*1 = 4 4*2 = 8 4*3 = 12 4*4 = 16
# 5*1 = 5 5*2 = 10 5*3 = 15 5*4 = 20

n = int(input("Prvi broj: "))
m = int(input("Drugi broj: "))

outputStr = ''

for x in range(1, n + 1):
    for y in range(1, m + 1):
        outputStr = outputStr + str(x) + '*' + str(y) + " = " + str(x * y) + " "
    print(outputStr)
    outputStr = ""