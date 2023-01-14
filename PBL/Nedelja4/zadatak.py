def zadatak_nedelja4():
    def znakovi(rec):
        
        nova_rec = ""

        for slovo in rec:

            if slovo.isalpha() or slovo.isnumeric():
                nova_rec += slovo

        return nova_rec  


    def reci():

        y=[]
        recenica = input("Unesi recnicu:\n")
        x = recenica.split(" ")
        ponavljanje = {}

        for rec in x:
            rec = znakovi((rec.strip()).lower())
            ponavljanje.setdefault(rec,0)
            ponavljanje[rec] += 1

        for rec, pon in ponavljanje.items():
            if pon == 1:
                y.append(rec)

        return y


    def procitajFajl(imeFajla):
        import pickle

        with open(imeFajla, 'rb') as fr:
            return pickle.load(fr) #Putem pickle modula prevodi iskesiljen recnik iz fajla u promenljivu

    def prosek(niz):

        import numpy as np
        novi_niz = np.sum(niz) #Recnik koristi liste kao vrednosti, pa se putem numpy modula prevodi u jednu vecu listu
        prosek = sum(novi_niz) / len(novi_niz) 

        return prosek


    def minimum(niz):

        minimalna_vrednost = min([min(x) for x in niz]) #Dva puta koristi funkciju min zato sto radi sa dvodimenzionalnom listom
        return(minimalna_vrednost)


    def maksimum(niz):

        maksimalna_vrednost = max([max(x) for x in niz]) #Dva puta koristi funkciju max zato sto radi sa dvodimenzionalnom listom
        return maksimalna_vrednost


    def main():

        while True:

            print("Sta zelite da uradite? Ako zelite da izdvojite jedinstvene reci iz recenice, pritisnite 1.") 
            odgovor = int(input("Ako zelite da nadjete minimalnu i maksimalnu vrednost unetog recnika i njihovu prosecnu vrednost, ukucajte 2.\n"))
            
            if odgovor == 1:

                print(reci())

            elif odgovor == 2:

                podaci = procitajFajl(r"podaci.txt")
                vrednosti = podaci.values()
                lista = list(vrednosti)

                print(minimum(lista))
                print(maksimum(lista))
                print(prosek(lista))

            else:
                print("Unesite validan broj!")

            pitanje = input("Da li zelite prestati sa radom? 'D' ili 'd' za da.\n")

            if pitanje == 'd' or pitanje == 'D':
                break

    main()
