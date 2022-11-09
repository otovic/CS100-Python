# Napisati program za pronalaženje najduže reči iz proizvoljne tekstualne datoteke. 
# Ne koristiti kontekstni menadžer.

fr = open("text.txt", "r")
reci = fr.read()

maxDuzina = 0 #najveca duzina reci
najduzaRec = [] #u ovom nizu cuvam sve reci sa njavecom duzinom
trenutnaRec = ""
trenutnaDuzina = 0

for slovo in reci: #prolazim kroz ceo tekst slovo po slovo
    if slovo.isalpha() or slovo.isnumeric(): #ako je karakter slovo ili broj, to racunam u duzinu, znaci dodajem 1
        trenutnaDuzina += 1
        trenutnaRec += slovo #pridruzujem to slovo u rec
        if trenutnaDuzina > maxDuzina: #ako je trenutna najveca duzina veca od postojece
            najduzaRec.clear() #praznim ceo niz sa najduzim recima, zato sto te reci nisu vise najduze
            maxDuzina = trenutnaDuzina #postavljam novu maksimalnu duzinu
            najduzaRec.append(trenutnaRec) #dodajem novu najduzu rec u niz
        elif trenutnaDuzina == maxDuzina: #ako je trenutna duzina jednaka maksimalnoj duzini to znaci da smo nasli rec koja ima isti broj slova kao i najduza i dodajemo je u niz
            if trenutnaRec not in najduzaRec: #proveravamo da li rec koja se ubacuje nije vec u nizu kako ne bi ubacio dve iste
                najduzaRec.append(trenutnaRec)
    else:
        trenutnaDuzina = 0 #ako for naidje na karakter koji nije slovo ili broj resetuje trenutnu duzinu i trenutnu rec
        trenutnaRec = ""

#ovo ispod je samo sredjivanje finalnog stringa za stampanje

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
fr.close()