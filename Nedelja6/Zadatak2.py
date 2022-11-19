# Napisati funkciju za kopiranje binarne datoteke. 
# Parametri funkcije jesu ime ulazne datoteke i veličina bloka za kopiranje, 
# a izlazna datoteka uvek ima u imenu nastavak _copy

def copyBinary(ulDat, velBloka):
    fr = open(ulDat, "rb")
    fw = open(ulDat + "_copy", "wb")
    line = fr.read(velBloka)
    while len(line) > 0:
        fw.write(line)
        line = fr.read(velBloka)
    fr.close()
    fw.close()

copyBinary("text.txt", 1024)