from random import randint

def baci_kockicu(broj_bacanja, zbir):
    broj = randint(1, 6)
    if zbir + broj > 21:
        return {'pokusaja': broj_bacanja, 'zbir': zbir}
    return baci_kockicu(broj_bacanja + 1, zbir + broj)

try:
    igrac1 = baci_kockicu(0, 0)
    igrac2 = baci_kockicu(0, 0)

    if igrac1['zbir'] > igrac2['zbir']:
        print('Pobedio je igrac 1. Zbir igraca 1 je ' + str(igrac1['zbir']) + ', Zbir igraca 2 je ' + str(igrac2['zbir']))
    elif igrac2['zbir'] > igrac1['zbir']:
        print('Pobedio je igrac 2. Zbir igraca 2 je ' + str(igrac2['zbir']) + ', Zbir igraca 1 je ' + str(igrac1['zbir']))
    elif igrac1['pokusaja'] > igrac2['pokusaja']:
        print('Poeni su jednaki. Pobedio je igrac 1 sa brojem pokusaja ' + str(igrac1['pokusaja']) + ', broj pokusaja igraca 2 je ' + str(igrac2['pokusaja']))
    elif igrac2['pokusaja'] > igrac1['pokusaja']:
        print('Poeni su jednaki. Pobedio je igrac 2 sa brojem pokusaja ' + str(igrac2['pokusaja']) + ', broj pokusaja igraca 1 je ' + str(igrac1['pokusaja']))
    else:
        print('Rezultat neresen. Igrac 1 zbir: ' + str(igrac1['zbir']) + ', igrac 1 pokusaja ' + str(igrac1['pokusaja']) + '. Igrac 2 zbir: ' + str(igrac2['zbir']) + ', igrac 2 pokusaja: ' + str(igrac2['pokusaja']))
except Exception as err:
    print(err)