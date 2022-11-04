# Napisati funkciju koja vraća broj BLT (bacon, tomatoes, lettuce) sendviča, možete napraviti
# na osnovu broja sastojaka, gde se brojevni parametri koji se prosleđuju funkciji.
# Pretpostaviti da je potrebno sledeće da napravite 1 sendvič:
# ● 10 traka slanine
# ● 3 lista zelene salate
# ● 6 kriški paradajza
# Imajte na umu da broj sendviča mora biti ceo broj; ne možete imati 1 1/2 a sendvič. Na
# primer, ako imate 12 kriški slanine, 20 listova zelene salate i 5000 paradajza kriške, možete
# napraviti samo 1 sendvič (uprkos činjenici da imate dovoljno zelene salate i paradajz za
# pravljenje 6 sendviča).

def numOfBLT(bacon, tomatoes, lettuce):
    return int(min((bacon / 10), (lettuce / 3), (tomatoes / 6)))


bacon = int(input("Bacon -> "))
lettuce = int(input("Lettuce -> "))
tomatoes = int(input("Tomatoes -> "))

print("Mozete napraviti ukupno " + str(numOfBLT(bacon, tomatoes, lettuce)) + " sendvic/vica!")