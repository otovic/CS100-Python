# Napisati korisničku interaktivnu funkciju koja će korisniku reći koji novčići su potrebni da bi
# napravio dato iznos novca sa najmanje utrošenih novčića.
# Na primer, recimo da pokušavamo da napravimo 45 centi za kusur koristeći četvrtine,
# novčiće, nikle i penije koristeći najmanje mogući broj novčića. Rešenje bi bilo korišćenje 
# kovanog novca najveće vrednosti moguće u svakom koraku rešiti problem, tako da bismo
# prvo koristili četvrtinu, ostavljajući 20centi. Zatim bismo koristili novčić, ostavljajući 10 centi.
# Onda bismo koristili još jedan novčić ostavljajući 0 centi i čineći ukupno 45 centi. U ovom
# primeru smo kreirali 45 centi koristeći 3 novčića, što je optimalno rešenje za problem
def povracajNovca(iznos):
    outputStr = "Potrebno je: "

    novcici = int(iznos / 25) #racunamo broj novcica
    outputStr += f"{novcici} novcic/a, " if novcici != 0 else "" #ako imamo bar 1 novcic to dodajemo u string koji se stampa

    nikli = int((iznos - (novcici * 25)) / 10) #racunamo broj nikla
    outputStr += f"{nikli} nikl/a, " if nikli != 0 else "" #ako imamo bar 1 nikl to dodajemo u string koji se stampa

    peniji = int((iznos - (novcici * 25 + nikli * 10))) #racunamo broj penija
    outputStr += f"{peniji} peni/ja, " if peniji != 0 else "" #ako imamo bar 1 peni to dodajemo u string koji se stampa

    print(outputStr + f"To je ukupno {novcici + nikli + peniji} novcica") #Stampamo string potrebnih novcica

povracajNovca(int(input("Unesite iznos -> ")))