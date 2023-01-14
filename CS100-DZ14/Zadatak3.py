# Kreirajte klasu pod nazivom BankAccount koja predstavlja bankovni račun, koji ima
# kao atribute: accountNumber (numerički tip), name (ime vlasnika naloga kao string
# tip), stanje.
# 37
# Napravite konstruktor sa parametrima: accountNumber, name, balance. Kreirajte
# metodu Deposit() koja upravlja radnjama depozita.
# Kreirajte metodu Withdrawal() koja upravlja akcijama povlačenja.
# Kreirajte metod bankFees() da biste primenili bankarske naknade sa procentom od 5%
# bilansnog računa.
# Kreirajte display() metod za prikaz detalja naloga.
# Napišite kompletan kod za klasu BankAccount.

class BankAccount:
    def __init__(self, accountNumber: int, name: str, balance: int) -> None:
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance

    def Deposit(self, ammount):
        self.balance += ammount

    def Withdrawal(self, ammount):
        if self.balance < (ammount + self.bankFees(ammount)):
            print('Nemate dovoljno sredstava na racunu!')
            return
        self.balance -= ammount + self.bankFees(ammount)
    
    def bankFees(self, ammount):
        return ammount * 0.05

    def Display(self):
        print(f"Racun: {self.accountNumber}, Ime: {self.name}, Stanje na racunu je: {self.balance}")

num = BankAccount('200-225246-24', 'Petar', 200)
num.Deposit(1000)
num.Withdrawal(300)
num.Display()