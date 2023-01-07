def brojevi(a, b, *c):
    if len(c) > 1:
        print("U jednoj promenljivi je smesteno vise od dva broja!")
    else:
        print("Svaka promenljiva ima samo jedan broj!")

brojevi(1, 2, 3, 4, 5)