def zadatak_nedelja2():
    
    vrsta = int(input("Unesite duzinu vrste matrice:\n"))
    kolona = int(input("Unesite duzinu kolone matrice:\n"))


    def citanje_i_upopunjavanje_liste(fajl, v, k):

        with open(fajl, "r") as fin:
            lista = fin.read().splitlines()
            lista = [int(x) for x in lista]

        if len(lista) < v * k:
            for i in range(v * k - len(lista)):
                lista.append(0)

        return lista


    def crtaj_matricu(lista, v, k):
        
        x = 0

        if len(lista) > v * k:
            raise Exception

        for i in range(k):
            while x < v * k:
                print(lista[x:x + v])
                x += v
            

    def sabiranje_vrsta(v, k):

        x = 0
        lista_suma = []
        
        for i in range(k):
            while x < v * k:
                lista_suma.append(sum(lista[x:x + v]))
                x += v       

        return lista_suma


    def crtanje_grafa():

        import matplotlib.pyplot as plt

        plt.bar(lista_suma)
        plt.title("Količina đubreta po tonoma.")
        plt.xlabel("Opštine")
        plt.ylabel("Tone")
        plt.show()


    try:
        lista = citanje_i_upopunjavanje_liste("Nedelja2/podaci.txt", vrsta, kolona)
        crtaj_matricu(lista, vrsta, kolona)
        print("-" * 15)
        lista_suma = sabiranje_vrsta(vrsta, kolona)
        print(lista_suma)
        crtanje_grafa()
    except Exception:
        print("Matrica ne može biti manja od broja elemenata!")
