godina = int(input("Unesite godinu: "));

if godina % 100 == 0 or godina % 4 == 0:
    print(f"{godina} je prestupna godina!")
else:
    print(f"{godina} nije prestupna godina!")