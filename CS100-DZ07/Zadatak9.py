# Napisati program koji predstavlja jednostavni digitron. 
# Korsinik unosi dva broja i operaciju +, - ,* , / koju želi da izvrši nad uneta dva broja. 
# Voditi računa o deljenju dva broja. Ukoliko korisnik ne izvrši korektan unos treba izbaciti izuzetak.

try:
    broj1 = int(input("Unesite prvi broj -> "))
    broj2 = int(input("Unesite drugi broj -> "))
    if broj1 == 0 or broj2 == 0:
        raise Exception("Brojevi ne smeju biti 0")
    else:
        try:
            match str(input("Unesite operaciju koju zelite (+, -, *, /) -> ")):
                case "+":
                    print(f"Zbir {broj1} i {broj2} je: {broj1 + broj2}")
                case "-":
                    print(f"Razlika {broj1} i {broj2} je: {broj1 - broj2}")
                case "*":
                    print(f"Proizvod {broj1} i {broj2} je: {broj1 * broj2}")
                case "/":
                    print(f"Kolicnik {broj1} i {broj2} je: {broj1 / broj2}")
                case _:
                    raise Exception("Unesite ispravnu operaciju!")
        except Exception as eroor:
            print(eroor)
                    
except Exception as error:
    print(error)

