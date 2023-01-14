def zadatak_nedelja5(): 
    import pickle

    def pitaj_za_opstinu(recnik):

        for ime, kolicina in recnik.items():
            print(f"{ime}: {kolicina}")

        ime_opstine = input("Unesite ime opštine čiju vrednost želite stepenovati:\n")
        kolicina_djubreta = recnik[ime_opstine] 
        eksponent = int(input("Unesite stepen kojim želite vršiti operaciju:\n"))
        recnik[ime_opstine] = stepenuj(kolicina_djubreta, eksponent)
        
        return recnik

    def stepenuj(broj, stepen):

        if stepen == 0:
            return 1 #Bazni slučaj. Rekurzija prestaje ovde zato što bilo koji broj na nultom stepenu je jednak jedan.

        return broj * stepenuj(broj, stepen - 1) #Program smanjuje stepen dok ne stigne do nula.

    def procitaj_Fajl(ime_Fajla: str):
        with open(ime_Fajla, 'rb') as frb:
            return pickle.loads(frb.read())

    def upisi_Podatke(ime_Fajla: str, recnik: dict):
        with open(ime_Fajla, 'wb') as fwb:
            pickle.dump(recnik, fwb)
            return recnik
    
    def isprazni_Kontejner(ime_Fajla: str, recnik: dict):
        print("Imena opstina:")

        for ime, kolicina in recnik.items():
            print(f"{ime}: {kolicina}")

        ime_isprazni = input("Unesite ime opstine za koju zelite da ispraznite kontejner: ")

        while ime_isprazni not in recnik.keys():
            print("Unesite ispravno ime opstine!")
            ime_isprazni = input("Unesite ime opstine za koju zelite da ispraznite kontejner: ")
        
        recnik[ime_isprazni] = 2

        upisi_Podatke(ime_Fajla, recnik)

        return recnik

    def dodaj_Opstinu(ime_Fajla: str, recnik: dict):
        ime_opstine = input("Unesite ime opstine u koju dodajete pametni kontejner: ")

        recnik[ime_opstine] = 2
        
        upisi_Podatke(ime_Fajla, recnik)

        return recnik

    def prikazi_Recnik(recnik: dict):
        for ime, kolicina in recnik.items():
            print(f"Opstina {ime}: {kolicina} kg djubreta")

    def izbrisi_Opstinu(ime_Fajla: str, recnik: dict):
        print("Opstine gde postoji pametni kontejner:")

        for ime in recnik.keys():
            print(f"{ime}")

        ime_opstine = input("Unesite ime opstine iz koje izbacujete pametni kontejner: ")

        while ime_opstine not in recnik.keys():
            print('Unesite ispravno ime opstine!')
            ime_opstine = input("Unesite ime opstine iz koje izbacujete pametni kontejner: ")

        del recnik[ime_opstine]
        upisi_Podatke(ime_Fajla, recnik)

        return recnik

    try:
        opcija = 10
        recnik = procitaj_Fajl('Nedelja5/opstine.metropolitan')
        while opcija != 0:
            print("Opcije:\n1. Prikazi opstine gde postoji pametni kontejner\n2. Dodaj opstinu\n3. Isprazni kontejner u opstini\n4. Izbrisi opstinu\n5. Baci djubre:\n6. Izadji iz programa")
            opcija = int(input("Izaberite opciju koju zelite (unesite broj): "))
            match opcija:
                case 1:
                    prikazi_Recnik(recnik)
                case 2:
                    recnik = dodaj_Opstinu('Nedelja5/opstine.metropolitan', recnik)
                    prikazi_Recnik(recnik)
                case 3:
                    recnik = isprazni_Kontejner('Nedelja5/opstine.metropolitan', recnik)
                    prikazi_Recnik(recnik)
                case 4:
                    recnik = izbrisi_Opstinu('Nedelja5/opstine.metropolitan', recnik)
                    prikazi_Recnik(recnik)
                case 5:
                    recnik = upisi_Podatke('Nedelja5/opstine.metropolitan', pitaj_za_opstinu(recnik))
                    prikazi_Recnik(recnik)
                case 6:
                    break
    except Exception as error:
        print(error)

