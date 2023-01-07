dummy = {
    "Palilula":13,
    "Niska Banja":16,
    "Medijana":25
}

def pitaj_za_opstinu(recnik):

    print(recnik)

    ime_opstine = input("Unesite ime opštine čiju vrednost želite stepenovati:\n")
    kolicina_djubreta = recnik[ime_opstine] 
    eksponent = int(input("Unesite stepen kojim želite vršiti operaciju:\n"))
    recnik[ime_opstine] = stepenuj(kolicina_djubreta, eksponent)
    
    return recnik

def stepenuj(broj, stepen):

    if stepen == 0:
        return 1 #Bazni slučaj. Rekurzija prestaje ovde zato što bilo koji broj na nultom stepenu je jednak jedan.

    return broj * stepenuj(broj, stepen - 1) #Program smanjuje stepen dok ne stigne do nula.

print(pitaj_za_opstinu(dummy))