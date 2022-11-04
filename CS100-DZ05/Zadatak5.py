# Napisati funkciju koja proverava da li je uneti pozitivan ceo broj (minimalno trocifreni)
# palindrom. Uraditi verifikaciju ulaza.

def palindrom(broj):
    return f"Broj {broj} je palindrom!" if list(str(broj)) == (list(reversed(str(broj)))) else f"Broj {broj} nije palindrom!"

broj = int(input("Unesite minimalno trocifreni broj -> "))
print("Unesite ispravan broj!") if broj < 100 else print(palindrom(broj))

