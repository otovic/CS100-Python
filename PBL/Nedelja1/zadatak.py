# Napisati funkciju koja okreće redosled elementima liste. 
# Funkcija kao parametar prima listu i vraća je izmenjenu. 
# Lista se kreira tako što se u nju upišu svi elementi iz fajla. 
# Fajl treba da sadrži podatke vezane za temu koju ste odabrali i
# treba da bude prilagođen zadatku. 
# Nakon što funkcija okrene redosled elementima
# liste upisuje izmenjenu listu u fajl.

def zadatak_nedelja1():
    lista = []

    with open("Nedelja1/KontejneriPoOpstini.txt", "r") as f:
        
        lines = f.readlines()

        for line in lines:
            lista.append(line.strip())

    lista.reverse()

    with open("Nedelja1/KontejneriPoOpstini.txt", "w") as f:

        for x in range(len(lista)):
            f.write(lista[x] + "\n")