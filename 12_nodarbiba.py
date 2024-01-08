# Auto
# + Krāsa
# + Piedziņa
# + Marka
# + Degvielas tips
# + Ātrums
# + ...
# - Taurēt
# - Paātrināšana
# - Bremzēšana
# - Bremzēšana ar rokas bremzi
# - ...

def testFun(self):
    print("Test!")

# Nākošā stunda: Mantošana
# class Transportlidzeklis:
class Tramvajs:
    krasa :str = "Balta"
class Auto:
    krasa :str = "Melna"
    marka :str = ""
    atrums :float
    # Labāk šādi nedarīt (!)
    # a = testFun

    def __init__(self, marka :str) -> None:
        self.marka = marka
        self.atrums = 0
    def __str__(self) -> str:
        return f"Marka: {self.marka}, Atrums: {self.atrums}, Krāsa: {self.krasa}"

    def nokraso(self, krasa :str) -> None:
        self.krasa = krasa
    def paatrinasana(self):
        self.atrums += 0.5
    def bremzesana(self):
        if (self.atrums >= 0.5):
            self.atrums -= 0.5
    # Statiska funkcija - nevajag izveidot objektu
    def status(auto):
        print(auto)

# Objekta izveide
masina = Auto("Audi")
masina.paatrinasana()
masina.paatrinasana()
print(masina.atrums)
masina.nokraso("Sarkana")
# masina.a()
Auto.status(masina)

masina2 = Auto("Skoda")
masina2.paatrinasana()
Auto.status(masina2)


