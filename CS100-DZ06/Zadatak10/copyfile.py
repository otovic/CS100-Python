# Napisati program za pisanje prvih n ne-negativnih celih brojeva (svaki broj je jedan red u datoteci). 
# Zatim, učitati tu datoteku, i na standardni izlaz štampati, red po red, zbir reda n i n+1 iz datoteke. 
# Ne koristiti kontekstni menadžer.

fw = open("brojevi.txt", "w")

n = int(input("Unesite pozitivan broj -> "))
if n < 1: #unosimo broj pozitivnih brojeva
    print("Unesite ispravan broj!")
else:
    for x in range(n): #upisujemo brojeve u fajl
        if x < n - 1:
            fw.write(str(x + 1) + "\n") #ako nije zadnji broj dodajem \n 
        else:
            fw.write(str(x + 1)) #ako je zadnji ne dodajem \n kako ne bi imao prazan zadnji red
    fw.close()
        
    fr = open("brojevi.txt", "r") #otvaram fajl za citanje
    f= fr.readlines() #ucitavam svaku liniju

    x = 0

    while x in range(len(f)):
        b1 = int((f[x].replace("\n", "")))
        if x + 1 < len(f): #ako zadnji broj nema para onda ne stampam
            b2 = int((f[x + 1]).replace("\n", ""))
            print(f"Zbir {b1} i {b2} je -> {b1 + b2}")
        x += 1
fr.close()