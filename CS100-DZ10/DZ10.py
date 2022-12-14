def cita_i_pretvara_u_niz(fajl):

    niz = []

    with open(fajl, "r") as fin:

        for linija in fin: 
            linija = linija.strip() 
            niz.append(linija)

    return niz

def ispisuje_u_terminalu(niz):
    niz = [x for x in set(niz)]
    for i in range(len(niz)):
        print(niz[i])

import random

def generisi_SB() -> str("v0b87n1ext"): #funkcija vraca jedan serijski broj
    karakteri = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    duzina = random.randrange(5, 11)
    serijski_broj = ''

    for x in range(duzina):
        karakter = karakteri[random.randrange(0, len(karakteri))]
        karakter = karakter.upper() if random.randrange(0, 2) == 0 else karakter.lower()
        serijski_broj += karakter
    
    return serijski_broj

def dodaj_serijske_brojeve(ime_fajla, kolicina): #Funkciji se prosledjuje ime fajla i kolicina. Kolicina oznacava koliko ce serijskih brojeva biti dodato u fajl
    with open(ime_fajla, 'a') as fa:
        for x in range(kolicina):
            sb = generisi_SB()
            num = random.randint(1, 3)
            #funkcija upisuje od 1 do 3 ista serijska broja u fajl zato sto mogu vise kontejnera da imaju isti serijski broj
            for y in range(num):
                fa.write(sb + "\n")

def upisi_serijske_brojeve(ime_fajla, kolicina): #Funkciji se prosledjuje ime fajla i kolicina. Kolicina oznacava koliko ce serijskih brojeva biti dodato u fajl
    with open(ime_fajla, 'w') as fa:
        for x in range(kolicina):
            sb = generisi_SB()
            num = random.randint(1, 3)
            #funkcija upisuje od 1 do 3 ista serijska broja u fajl zato sto mogu vise kontejnera da imaju isti serijski broj
            for y in range(num):
                fa.write(sb + "\n")

def serial_check(serial_number, serialreplace):

    if len(serial_number) == 5 or serial_number == serialreplace:

        replaced = serial_number.replace(serial_number,"#")

        return replaced
    else:

        return serial_number

def menja_u_znak(fajl, serijskibroj):

    with open(fajl, "r") as fin:
        linije = fin.readlines()

    #Pretvara elemente fajla u listu
    lista = [x.strip() for x in linije]

    #Menja sve serijske brojeve duzine pet karaktera u #####
    for i in range(len(lista)):
        zamena = serial_check(lista[i], serijskibroj)
        lista[i] = zamena

    #Dodaje nove podatke u fajl
    with open(fajl, "w") as fout:
        for j in lista:
            fout.write("%s\n" % j)

odgovor = input("Sta bi ste hteli da uradite? \n1. da se izlistaju svi serijski brojevi \n2. da se dodaju novi serijski brojevi \n3. da se upisu novi serijski brojevi \n4. da se zameni odgovarajuci serijski broj sa #\n5. Izlaz iz programa\n")
while True:
    if odgovor == '1':
        niz = cita_i_pretvara_u_niz(r"DZ10.txt")  
        ispisuje_u_terminalu(niz)
    elif odgovor == '2':
        broj = int(input("Koliko serijskih brojeva zelite dodati?\n"))
        dodaj_serijske_brojeve(r"DZ10.txt", broj)
    elif odgovor == '3':
        broj = int(input("Koliko serijskih brojeva zelite upisati?\n"))
        upisi_serijske_brojeve(r"DZ10.txt", broj)
    elif odgovor == '4':
        serijskiBroj = str(input("Koj serijski broj kontejnera zelite da zamenite: "))
        menja_u_znak(r"DZ10.txt", serijskiBroj)
    elif odgovor == '5':
        break
    odgovor = input("Sta bi ste hteli da uradite? \n1. da se izlistaju svi serijski brojevi \n2. da se dodaju novi serijski brojevi \n3. da se upisu novi serijski brojevi \n4. da se zameni odgovarajuci serijski broj sa #\n5. Izlaz iz programa\n")


