# Kreirajte klasu Person sa atributima: ime i starost string tipa.
# Kreirajte display() metod koji prikazuje ime i starost objekta kreiranog preko
# klase Person.
# Kreirajte podređenu klasu Student koja nasleđuje klasu Person i koja takođe ima
# atribut sekcije.
# Kreirajte metod displayStudent() koji prikazuje ime, starost i odeljak objekta
# kreiranog putem klase Student.
# Kreirajte studentski objekat putem instanciranja u klasi Student, a zatim
# testirajte metod displayStudent.

class Person:
    def __init__(self, ime: str, starost: str) -> None:
        self.ime = ime
        self.starost = starost
    
    def Display(self) -> str:
        return f"Ime studenta -> {self.ime}, Starost: {self.starost}"

class Student(Person):
    def __init__(self, ime: str, starost: str, sekcije) -> None:
        super().__init__(ime, starost)
        self.sekcije = sekcije
    
    def displayStudent(self) -> str:
        print(f"{self.Display()}, Sekcije: {self.sekcije}")

student = Student('Petar', '30', 'neka, sekcija')
student.displayStudent()