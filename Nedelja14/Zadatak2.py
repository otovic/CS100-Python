class student:
    def __init__(self, ime):
        self.ime = ime

class marks(student):
    def __init__(self, ime, ocena):
        super().__init__(ime)
        self.ocena = ocena

std = marks('Petar', 5)
print(f"{std.ime}, {std.ocena}")