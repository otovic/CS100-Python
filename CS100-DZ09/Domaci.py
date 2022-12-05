import matplotlib.pyplot as plt
import numpy as np

def unosOpstinaIKolicine():
    with open('Podaci.txt', 'w') as fw:
        velicina = int(input("Unesite broj opstina: "))
        while velicina < 1:
            print("Unesite ispravnu vrednost!")
            velicina = int(input("Unesite broj opstina: "))
        for x in range(velicina):
            imeOpstine = str(input(f"Unesite ime {x + 1}. opstine: "))
            kolicinaDjubreta = ''
            for y in range(velicina):
                kolicinaDjubreta += str(input(f"Unesite kolicinu djubreta u {y + 1}. kontejneru opstine {imeOpstine}: "))
                kolicinaDjubreta += ',' if y != velicina - 1 else ''
            fw.write(imeOpstine + ':' + kolicinaDjubreta + '\n')

def maxVelicina():
    with open('Podaci.txt', 'r') as fr:
        return len(fr.readlines())

def procitajFajl():
    with open('Podaci.txt', 'r') as fr:
        podaci = []
        for red in fr.readlines():
            podaci.append(red.strip())
        return podaci

def vratiImenaOpstina(podaci):
    imena = []
    for x in podaci:
        imena.append((x.split(':'))[0].strip())
    return imena

def vratiKolicinuDjubreta(podaci):
    zbir = []
    for x in range(len(podaci)):
        suma = 0
        for y in range(len(podaci[x])):
            suma += podaci[x][y]
        zbir.append(suma)
    return zbir

def generisiMatricu(podaci):
    maxbroj = maxVelicina()
    velicinaMat = int(input(f"Unesite broj opstina za prikaz podataka (Maksimalna velicina {maxbroj}): "))
    zeljenaImena = []
    matrica = []

    if velicinaMat == maxbroj:
        for x in vratiImenaOpstina(procitajFajl()):
            zeljenaImena.append(x)

        for x in range(velicinaMat):
            trenutniRed = []
            kontejner = podaci[x].split(':')
            for kolicina in kontejner[1].split(','):
                trenutniRed.append(int(kolicina))
            matrica.append(trenutniRed)

        return vratiKolicinuDjubreta(matrica), zeljenaImena

    while velicinaMat > maxbroj or velicinaMat < 0:
        print("Morate uneti ispravnu vrednost!")
        velicinaMat = int(input(f"Unesite broj opstina za prikaz podataka (Maksimalna velicina {maxbroj}): "))
    
    imenaOpstina = vratiImenaOpstina(procitajFajl())

    print(f"\nZa koje opstine zelite da vidite podatke? (Izaberite sa liste {velicinaMat}. opstine/u unosom broja)")
    for x in range(len(imenaOpstina)):
        print(f"{x + 1}. Opstina {imenaOpstina[x]}")

    zeljeneOpstine = []
    zeljenaImena = []

    for x in range(velicinaMat):
        brojOpstine = int(input(f"Unesite broj {x + 1}. opstine za koju zelite da vidite podatke: "))

        while brojOpstine > len(imenaOpstina) or brojOpstine < 0 or brojOpstine in zeljeneOpstine:
            print("Unesite ispravan broj opstine!\n")
            brojOpstine = int(input(f"Unesite broj {x + 1}. opstine: "))

        zeljeneOpstine.append(brojOpstine)
        zeljenaImena.append(imenaOpstina[brojOpstine - 1])

    for x in range(velicinaMat):
        trenutniRed = []
        kontejner = podaci[zeljeneOpstine[x] - 1].split(':')
        for kolicina in kontejner[1].split(','):
            trenutniRed.append(int(kolicina))
        matrica.append(trenutniRed)
    
    return vratiKolicinuDjubreta(matrica), zeljenaImena

try:
    opcija = str(input("Da li zelite da unesete nove podatke ili radite sa trenutnim (odgovorite da ili ne): "))
    while opcija.lower() not in ['da', 'ne']:
        print("Unesite ispravnu opciju!")
        print(opcija.lower())
        opcija = str(input("Da li zelite da unesete nove podatke ili radite sa trenutnim (odgovorite da ili ne): "))

    if opcija.lower() == 'da':
        unosOpstinaIKolicine()

    kolicina, imena = generisiMatricu(procitajFajl())

    colors = ['r', 'g', 'b', 'c', 'y', 'm', 'k']
    median = max(kolicina) / 4

    for x in range(len(kolicina)):
        if kolicina[x] == max(kolicina):
            plt.bar(imena[x], kolicina[x], color='red')
        elif kolicina[x] >= 0 and kolicina[x] <= 2*median:
            plt.bar(imena[x], kolicina[x], color='green')
        elif kolicina[x] > 2*median and kolicina[x] <= 3* median:
            plt.bar(imena[x], kolicina[x], color='olive')
        elif kolicina[x] > 3*median and kolicina[x] <= 4*median:
            plt.bar(imena[x], kolicina[x], color='orange')

    plt.bar
    plt.xlabel("Ime opstine")
    plt.ylabel("Kolicina djubreta (u tonama)")
    plt.title("Kolicina djubreta po opstinama u tonama (Svi kontejneri)")
    plt.grid(b = True, color ='grey',
            linestyle ='-.', linewidth = 0.5,
            alpha = 0.6)
    plt.show()

except Exception as err:
    print("Doslo je do greske")