# Zadatak 3. Napisati program koji za izlaz ima tekstualnu datoteku koja opisuje Vaš raspored časova za uneti dan. 
# Preko standardnog ulaza u posebnim ulazima unosite dan, broj predmeta toga dana, šifre predmeta, imena predmeta i početak i kraj predavanja/vežbi.
# #Ulazni podaci:
# >>> Ponedeljak
# >>> 1
# >>> CS100
# >>> Uvod u programiranje (Python)
# >>> 09:00
# >>> 10:30
# #Izlazna datoteka raspored.txt

fw = open("raspored.txt", "w")
dan = str(input("Unesite dan -> "))
fw.write(dan + "\n")
brojpredmeta = int(input("Broj predmeta -> "))
unetiPredmeti = 0
while unetiPredmeti < brojpredmeta:
    sifra = str(input("Sifra predmeta -> "))
    fw.write(sifra + "\n")
    ime = str(input("Ime predmeta -> "))
    fw.write(ime + "\n")
    pocetak = str(input("Unesite pocetak -> "))
    fw.write(pocetak)
    kraj = str(input("Unesite kraj -> "))
    fw.write(kraj + "\n")
    unetiPredmeti += 1
