def thirdString(*text):
    if len(text) < 3:
        print("Unesite najmanje 3 argumenta!")
    else:
        print(text[2])

thirdString("petar1", "petar2", "petar3")