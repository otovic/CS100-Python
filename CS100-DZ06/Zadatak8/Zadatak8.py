# Napisati program za pronalaženje frekvencije pojavljivanja svih reči iz proizvoljne tekstualne datoteke. 
# Program broji reči iz datoteke i na standardnom izlazu pokazuje pored svake reči broj ponavljanja te reči.
# Koristiti kontekstni menadžer.
reci = []
brojPonavljanja = []
trenutnaRec = ""

with open("text.txt", "r") as f:
    tekst = f.read()
    tekst += " "
    tekst = tekst.replace("\n", " ")
    for x in tekst:
        if x.isalpha() or x.isnumeric() or x == "'":
            trenutnaRec += x
        elif trenutnaRec != "":
            if trenutnaRec not in reci:
                reci.append(trenutnaRec)
                brojPonavljanja.append(1)
            else:
                brojPonavljanja[reci.index(trenutnaRec)] += 1
            trenutnaRec = ""

for x in range(len(reci)):
    print(str(reci[x]) + " broj ponavljanja -> " + str(brojPonavljanja[x]) + "\n")