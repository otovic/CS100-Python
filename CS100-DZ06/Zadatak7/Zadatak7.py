# Napisati program za pronalaženje najduže reči iz proizvoljne tekstualne datoteke. 
# Ne koristiti kontekstni menadžer.

fr = open("text.txt", "r")
reci = fr.read()

maxDuzina = 0
najduzaRec = []
trenutnaRec = ""
trenutnaDuzina = 0

for slovo in reci:
    if slovo.isalpha() or slovo.isnumeric():
        trenutnaDuzina += 1
        trenutnaRec += slovo
        if trenutnaDuzina > maxDuzina:
            najduzaRec.clear()
            maxDuzina = trenutnaDuzina
            najduzaRec.append(trenutnaRec)
        elif trenutnaDuzina == maxDuzina:
            if trenutnaRec not in najduzaRec:
                najduzaRec.append(trenutnaRec)
    else:
        trenutnaDuzina = 0
        trenutnaRec = ""

if len(najduzaRec) == 1:
    outputStr = "Najduza rec je: "
else:
    outputStr = "Najduze reci su: "

for x in range(len(najduzaRec)):
    if x < len(najduzaRec) - 1:
        outputStr += str(najduzaRec[x]) + ", "
    elif x == len(najduzaRec) - 1 and len(najduzaRec) > 1:
        outputStr += najduzaRec[x] + " | Duzina tih reci je " + str(maxDuzina) + " slova!"
    else:
        outputStr += najduzaRec[x] + " | Duzina te reci je " + str(maxDuzina) + " slova!"

print(outputStr)