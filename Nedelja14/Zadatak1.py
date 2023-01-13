class vozilo:
    ime = ''
    max_brzina = 0
    kilometraza = 0

class bus(vozilo):
    kapacitet = 50

    def printstuff(self):
        print(f"{self.ime}, {self.max_brzina}, {self.kilometraza}, {self.kapacitet}")

a = bus()
a.printstuff()