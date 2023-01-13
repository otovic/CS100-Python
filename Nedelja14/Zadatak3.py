class book:
    def __init__(self, naslov, autor, cena):
        self.naslov = naslov
        self.autor = autor
        self.cena = cena
    
    def view(self):
        print(f"Naslov knjige: {self.naslov}, Autor: {self.autor}, Cena: {self.cena}")

knjiga = book(input("Naslov -> "), input("Autor -> "), input("Cena -> "))
knjiga.view()