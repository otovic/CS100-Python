# Napišite klasu Rectangle, koja vam omogućava da napravite pravougaonik sa
# atributima dužine i širine.
# Kreirajte metodu Perimeter() da biste izračunali obim pravougaonika i Area() metodu
# da biste izračunali površinu pravougaonika.
# Kreirajte metod display() koji prikazuje dužinu, širinu, perimetar i površinu
# objekta kreiranog korišćenjem instanciranja klase pravougaonika.
# Kreirajte podređenu klasu Parallelepipede koja će naslediti klasu Rectangle i sa
# atributom visine i drugom Volume() metodom da biste izračunali zapreminu
# paralelepipeda.


class Rectangle:
    def __init__(self, duzina, sirina):
        self.duzina = duzina
        self.sirina = sirina
    
    def Perimeter(self) -> int:
        return (2 * self.duzina) + (2 * self.sirina)

    def Area(self) -> int:
        return self.duzina * self.sirina
    
    def Display(self) -> str:
        print(f"Sirina: {self.sirina}, Duzina: {self.duzina}, Obim pravougaonika: {self.Perimeter}, Povrsina pravougaonika: {self.Area}")

class Parallelopipede(Rectangle):
    def __init__(self, duzina, sirina, visina):
        super().__init__(duzina, sirina)
        self.visina = visina

    def Volume(self):
        print(f"Zapremina paralelopipeda: {self.Area() * self.visina}")

paral = Parallelopipede(5, 2, 5)
paral.Volume()