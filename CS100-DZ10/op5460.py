import random

def generisiSB() -> str("v0b87n1ext"): #funkcija vraca jedan serijski broj
    karakteri = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    duzina = random.randrange(5, 11)
    serijski_broj = ''

    for x in range(duzina):
        karakter = karakteri[random.randrange(0, len(karakteri))]
        karakter.upper() if random.randrange(0, 2) == 0 else karakter.lower()
        serijski_broj += karakter
    
    return serijski_broj

def dodajSerijskeBrojeve(imeFajla, kolicina): #Funkciji se prosledjuje ime fajla i kolicina. Kolicina oznacava koliko ce serijskih brojeva biti dodato u fajl
    with open(imeFajla, 'a') as fa:
        for x in range(kolicina):
            sb = generisiSB()
            for x in range(random.randrange(0, 3)):
                fa.write(sb + "\n")