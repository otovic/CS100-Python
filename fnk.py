def isprazni_Kontejner(ime_Fajla: str, recnik: dict):
    print("Imena opstina:")
    for ime, kolicina in recnik.items():
        print(f"{ime}: {kolicina}")
    ime_isprazni = input("Unesite ime opstine za koju zelite da ispraznite kontejner: ")

    while ime_isprazni not in recnik.keys():
        print("Unesite ispravno ime opstine!")
        ime_isprazni = input("Unesite ime opstine za koju zelite da ispraznite kontejner: ")
    
    recnik[ime_isprazni] = 1

    upisi_Podatke(ime_Fajla, recnik)

    return recnik

def dodaj_Opstinu(ime_Fajla: str, recnik: dict):
    ime_opstine = input("Unesite ime opstine u koju dodajete pametni kontejner: ")
    recnik[ime_opstine] = 1
    upisi_Podatke(ime_Fajla, recnik)
    return recnik