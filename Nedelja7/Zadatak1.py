#izracunati povrsinu i obim pravougaonika

def povrsinaPravougaonika(a, b):
    if any(vrednost < 1 for vrednost in [a, b]):
        raise Exception("Unesite ispravne vrednosti!")
    else:
            return a * b
try:
    print("Povrsina je: " + str(povrsinaPravougaonika(int(input("Prva stranica: ")), int(input("Druga stranica: ")))))
except Exception as error:
    print(error)