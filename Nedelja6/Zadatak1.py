# Napisati funkciju za kopiranje tekstualne datoteke. 
# Parametri funkcije jesu ime ulazne datoteke i ime izlazne datoteke.

def copyFile(ulaznaDatoteka, izlaznaDatoteka):
    ulaznaDatoteka = open(ulaznaDatoteka, "r")
    izlaznaDatoteka = open(izlaznaDatoteka, "w")
    for line in ulaznaDatoteka:
        izlaznaDatoteka.write(line)
    ulaznaDatoteka.close()
    izlaznaDatoteka.close()

copyFile("text.txt", "izlaz.txt")