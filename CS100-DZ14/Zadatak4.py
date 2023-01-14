# Kreirajte Račun klasu sa podrazumevanim konstruktorom (bez parametara) koji
# omogućava izvođenje različitih proračuna na celim brojevima.
# Kreirajte metod pod nazivom Factorial() koji vam omogućava da izračunate faktorijel
# celog broja. Testirajte metod tako što ćete instancirati klasu.
# Kreirajte metod pod nazivom Sum() koji vam omogućava da izračunate zbir prvih n
# celih brojeva 1 + 2 + 3 + .. + n. Testirajte ovaj metod.
# Kreirajte metod pod nazivom testPrim() u klasi Calculation da biste testirali
# primarnost datog celog broja. Testirajte ovaj metod.
# Kreirajte metod pod nazivom testPrims() koji omogućava testiranje da li su dva
# broja prosta između njih.
# Kreirajte metod tableMult() koji kreira i prikazuje tabelu množenja datog celog
# broja. Zatim kreirajte metod allTablesMult() da prikažete sve tabele množenja celih
# brojeva 1, 2, 3, ..., 9.
# Kreirajte statičku metodu listDiv() koja dobija sve delioce datog celog broja na
# novoj listi koja se zove Ldiv.

class Racun:
    def __init__(self) -> None:
        pass

    def Factorial(self, number):
        if number == 1:
            return 1
        else:
            return number * self.Factorial(number - 1)
    
    def Sum(self, number):
        if number == 1:
            return 1
        else:
            return number + self.Sum(number - 1)
    
class Calculation():
    def __init__(self) -> None:
        pass
    
    #testira da li je broj prost ???
    def testPrim(self, number: int):
        if not any(number % x == 0 and number != x for x in range(2, 10)):
            print(f'Broj {number} je prost!')

    #??????? Testira da li postoje dva prosta broja izmedju dva zadata ????????????
    def testPrims(self, num1, num2):
        counter = 0
        for x in range(num1, num2):
            if not any(x % y == 0 and x != y for y in range(2, 10)):
                counter += 1
            if counter == 2:
                print(f'Postoje dva prosta broja izmedju {num1}, {num2}')
                return
        
        print(f"Ne postoje dva prosta broja izmedju brojeva {num1} i {num2}")
    
    def tabelMult(self, num):
        for x in range(1, 11):
            print(f"{num} * {x} = {num * x}")
    
    def allTablesMult(self):
        out = []
        curr = []
        for x in range(1, 11):
            for y in range(1, 11):
                curr.append(f"{x}*{y}={x * y}")
            out.append(curr)
            curr = []
        for x in out:
            print(x)

    @staticmethod
    def listDiv(num):
        lDiv = []
        for x in range(1, num + 1):
            if num % x == 0:
                lDiv.append(x)
        
        print(lDiv)

q = Racun()
print(q.Factorial(5))
print(q.Sum(5))

w = Calculation()
w.testPrim(10)
w.testPrims(47, 58)
# w.tabelMult(10)
w.allTablesMult()

Calculation.listDiv(10)