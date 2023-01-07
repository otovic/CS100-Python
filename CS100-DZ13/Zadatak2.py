import getpass

def unesiPass():
    username = 'Sundjer Bob'
    password = 'Lignjoslav'

    ent_username = input('Unesite korisnicko ime -> ')
    ent_password = getpass.getpass('Unesite loznku -> ')

    if ent_username == username and ent_password == password:
        print('Uspesno logovanje!')
    else:
        print('Pogresna kombinacija!')

unesiPass()

    