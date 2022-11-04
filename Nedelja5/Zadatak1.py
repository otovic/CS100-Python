def thirdString(*text):
    print("Unesite najmanje 3 argumenata") if len(text) < 3 else print(text[2])

thirdString("petar1", "petar2", "petar3")