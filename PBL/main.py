from Nedelja1.zadatak import zadatak_nedelja1 as zn1
from Nedelja2.zadatak import zadatak_nedelja2 as zn2
from Nedelja3.zadatak import zadatak_nedelja3 as zn3
from Nedelja4.zadatak import zadatak_nedelja4 as zn4
from Nedelja5.zadatak import zadatak_nedelja5 as zn5

print("********** MET12 Team **********")
tekstovi_zadataka = {
    "nedelja1":  "Napisati funkciju koja okreće redosled elementima liste. Funkcija kao parametar prima listu i vraća je izmenjenu. Lista se kreira tako što se u nju upišu svi elementi iz fajla. Fajl treba da sadrži podatke vezane za temu koju ste odabrali itreba da bude prilagođen zadatku. Nakon što funkcija okrene redosled elementima liste upisuje izmenjenu listu u fajl.",
    "nedelja2": "Napisati funkciju koja pravi matricu određenog broja koji unosi korisnik i popunjava je šablonom šahovnice. Funkcija kao parametar prima listu i vraća niz koji je zbir elemenata po redovima matrice. Fajl treba da sadrži podatke vezane za temu koju ste odabrali i treba da bude prilagođen zadatku. Nakon što funkcija uradi svoje, prikažite niz u dijagramu pomoću matplotlib biblioteke.",
    "nedelja3": "Napisati funkciju koja čita izveštaj u vidu stringa iz datoteke i zamenjuje svaki znak jedne ključne reči po izboru, kao i sve reči od tačno 5 karaktera znakom taraba (#). Funkcija kao parametar prima ime datoteke i vraća rezultirajući string. Datoteka treba da sadrži podatke vezane za temu koju ste odabrali i treba da bude prilagođena zadatku",
    "nedelja4": "Napisati program koji od reči koje je uneo korisnik izdvaja samo one koje su se jednom pojavile. b) Napraviti rečnik u kom ćete smestiti podatke, ali tako da je vrednost u parovima ključvrednost broj. Nađite prosečnu i minimalnu i maksimalnu vrednost svih vrednosti iz rečnika.",
    "nedelja5": "Napisati rekurzivnu funkciju koja stepenuje broj na zadati stepen (ne koristiti operator **), a kao parametre ima broj koji treba da stepenuje i stepen. Koristiti ovu funkciju da stepenujete sve brojeve koje koristite u projektu. Ukoliko ne radite projekat, stepenovati niz brojeva koji sami kreirate. Zaglavlje funkcije: stepenuj(broj, stepen) Ne koristiti globalne promenljive!"
}

opcija = 1
print('Unesite broj nedelje za koju zelite da pokrenete zadatak: ')

while opcija in [1, 2, 3, 4, 5]:
    opcija = int(input('Broj nedelje -> '))

    if opcija == 1:
        print("Tekst zadatka za 1. nedelju: \n")
        print(tekstovi_zadataka["nedelja1"] + "\n")
        print("Ideja za resenje: \n")
        print("Napravili smo listu pametnih kontejnera sa nazivima opstina. Zadatak okrece listu i upisuje je u fajl.")
        zn1()
    
    elif opcija == 2:
        print("Tekst zadatka za 2. nedelju: \n")
        print(tekstovi_zadataka["nedelja2"] + "\n")
        print("Ideja za resenje: \n")
        print("U fajlu su upisane kolicine djubreta u tonama po opstini. Matrica se popunjava unosom sa tastature i prikazuje se grafik sa kolicinom djubreta po opstini.")
        zn2()

    elif opcija == 3:
        print("Tekst zadatka za 3. nedelju: \n")
        print(tekstovi_zadataka["nedelja3"] + "\n")
        print("Ideja za resenje: \n")
        print("U fajlu su upisani serijski brojevi pametnih kontejnera. Korisnik bira serijski broj kontejnera koji ce biti zamenjem.")
        zn3()

    elif opcija == 4:
        print("Tekst zadatka za 4. nedelju: \n")
        print(tekstovi_zadataka["nedelja4"] + "\n")
        print("Ideja za resenje: \n")
        print("Nismo uspeli da nadjemo resenje kako da prilagodimo ovaj zadatak nasem resenju pametnih kontajnera.\n")
        zn4()
    
    elif opcija == 5:
        print("Tekst zadatka za 5. nedelju: \n")
        print(tekstovi_zadataka["nedelja5"] + "\n")
        print("Ideja za resenje: \n")
        print("Rekurzivnom funkcijom se baca djubre u kontejneru.\n")
        zn5()

print("********* MET12 Team Signing off **********")