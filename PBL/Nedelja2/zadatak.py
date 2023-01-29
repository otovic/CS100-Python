def zadtak_nedelja2():
    def citanje_i_upopunjavanje_liste(fajl, v, k):

        #Čita podatke iz fajla, pretvara u int tip podataka, piše u listu
        with open(fajl, "r") as fin:
            lista = fin.read().splitlines()
            lista = [int(x) for x in lista]

        #Ako lista ima manje elemenata nego matrica, popunjava ostatak matrice sa nulama
        for i in range(v * k - len(lista)):
            lista.append(0)

        return lista


    def crtaj_matricu(lista, v, k):
        
        x = 0

        if len(lista) > (v * k):
            raise Exception

        #Popunjava matricu sa elementima iz liste. Pravi redove u zavisnosti od broja vrsta/kolona.
        for i in range(k):
            print(lista[x:x + v])
            x += v
                

    def sabiranje_vrsta(v, k):

        x = 0
        lista_suma = []
        
        #Računa sumu svake vrste u matrici, skladišti ih u novu listu.
        for i in range(k):
            lista_suma.append(sum(lista[x:x + v]))
            x += v       

        return lista_suma


    def crtanje_grafa(y, x):

        plt.bar(y, x)
        plt.title("Količina đubreta u tonima.")
        plt.xlabel("Opštine")
        plt.ylabel("Tone")
        plt.show()


    import matplotlib.pyplot as plt

    vrsta = int(input("Unesite koliko elemenata ima jedna vrsta matrice:\n"))
    kolona = int(input("Unesite koliko ima vrsta u matrici:\n"))

    lista = citanje_i_upopunjavanje_liste(r"Nedelja2/podaci.txt", vrsta, kolona)

    try:
        crtaj_matricu(lista, vrsta, kolona)

    except Exception:
        print("Dužina liste ne može biti veća od veličine matrice!")
        
    else:
        print("-" * 15)

        lista_suma = sabiranje_vrsta(vrsta, kolona)
        print(lista_suma)

        #Korisnik unosi opštine po željenom redosledu koje se koriste u grafu.
        lista_opstina = []
        for i in range(kolona):
            opstina = input(f"Unesite ime {i + 1}. opstine:\n")
            lista_opstina.append(opstina)

        crtanje_grafa(lista_opstina, lista_suma)

