#izracunati povrsinu i obim pravougaonika

def povrsinaPravougaonika(a, b):
    try:
        if any(vrednost < 1 for vrednost in [a, b]):
            raise Exception("Unesite ispravne vrednosti!")
        else:
            return a * b
    except Exception as error:
        print(error)

print("Povrsina je: " + str(povrsinaPravougaonika(int(input("Prva stranica: ")), int(input("Druga stranica: ")))))