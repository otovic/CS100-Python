# Napisati program koji najpre učitava tekstualnu datoteku proizvoljnog sadržaja. 
# Zatim, preko standardnog ulaza uneti trenutnu poziciju sa kojeg korisnik želi da čita sadržaj 
# (trenutna pozicija je pozitivni ceo broj). U novu datoteku kopirati sav sadržaj od trenutne pozicije do kraja datoteke.
# Koristiti kontekstni menadžer.

with open("text.txt", "r") as fr:
    linije = fr.readlines()
    n = int(input("Unesite poziciju za upisivanje u novi fajl -> "))

    if n >= len(linije) + 1 or n < 1:
        print("Unesite ispravan broj! (Da nije veci od samog broja linija u fajlu i da nije manji ili jednak nuli)")
    else: 
        with open("noviFajl.txt", "w") as fw:
            for x in range(n - 1, len(linije)):
                fw.write(linije[x])
            fw.close()
fr.close()