import matplotlib.pyplot as plt

def unosOpstina():
    with open('Podaci.txt', 'w') as fw:
        brojOpstina = int(input("Unesite broj opstina: "))
        imeOpstine = str(input("Unesite ime opstine: "))


def generisiMatricu(podaci):
    velicina = int(input("Unesite velicinu matrice (Maksimalno 3): "))
    while velicina > 3 or velicina < 0:
        print("Unesite ispravan broj!");
        velicina = int(input("Unesite velicinu matrice (Maksimalno 3): "))
    
    mat = []
    zbirElemenata = []
    zbir = 0
    
    for i in range(velicina):
        mat.append([])
        zbir = 0
        for j in range(velicina):
            mat[len(mat) - 1].append(podaci[j])
            zbir += int(podaci[j])
        
        zbirElemenata.append(zbir)

        for x in range(velicina):
            podaci.pop(0)
    
    return zbirElemenata

with open('Podaci.txt', 'r') as fr:
    redovi = fr.readlines()
    vrednosti = []

    for red in redovi:
        x = red.split(':')
        vrednosti.append(x[1].strip())

    zbir = generisiMatricu(vrednosti)
    opstine = ['Zona 1', 'Zona 2', 'Zona 3']

    plt.bar(opstine, zbir)
    plt.title("Djubre u tonama po zoni")
    plt.ylabel("Tone")
    plt.xlabel("Zona 1: Niska Banja, Pantelej, Palilula \nZona 2: Medijana, Trosarina, Durlan\nZona 3: Duvaniste, Crveni krst, Donja Vrezina") 
    plt.show()