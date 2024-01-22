# 1. Uzdevums
# Precēm var izveidot klasi "Prece" 
# (Šī klase satur preces nosaukumu un cenu -
#  abas vērtības uzstāda šīs klases init funkcijā)
class Prece:
    nosaukums :str = ""
    cena :float = 0.0
    def __init__(self, _nosaukums, _cena) -> None:
        self.nosaukums = _nosaukums
        self.cena = _cena

# Šī klase satur preces un to daudzumu. 
# Klasei jānodrošina funkcijas, kas ļauj pievienot preces, izņemt 
# preces un aprēķināt groza kopējo vērtību.
class Grozs:
    preces = {} # dict[Prece, int]
    # preces = []
    def pievienot(self, prece :Prece, skaits :int):
        self.preces[prece] = skaits
        # preces.append(prece)
    def iznemt(self, prece :Prece):
        for iii in self.preces.keys():
            if prece.nosaukums == iii.nosaukums:
                self.preces.pop(iii)
                break
    def vertiba(self) -> float:
        kopvertiba = 0.0
        for key, val in self.preces.items():
            kopvertiba += key.cena * val
        return kopvertiba
grozs = Grozs()

prece1 = Prece("Prece1", 10.0)
prece2 = Prece("Prece2", 20.0)
grozs.pievienot(prece1, 10)
grozs.pievienot(prece2, 5)
grozs.iznemt(prece1)
print(grozs.vertiba())

# 2. Uzdevums
class Darbinieks:
    id :int = 0
    vards :str = ""
    alga :float = 0.0
    amats :str = ""
    nostradatsMenesi :int = 0
    def __init__(self, _id, _vards, _alga, _amats, _nostradats) -> None:
        self.id = _id
        self.vards = _vards
        self.alga = _alga
        self.amats = _amats
        self.nostradatsMenesi = _nostradats
    def aprekinatAlgu(self):
        return self.nostradatsMenesi * self.alga
    def __str__(self):
        return f"{self.id}: {self.amats} {self.vards}. \
            Strādā uzņēmumā {self.nostradatsMenesi} mēn. ar algu {self.alga}. \
            Kopā izmaksāts: {self.aprekinatAlgu()}!"

janis = Darbinieks(1, "Janis", 1000, "Slotas operators", 24)
eriks = Darbinieks(2, "Ēriks", 2000, "Tirgotājs", 30)
anna = Darbinieks(3, "Anna", 500, "Laborante", 2)
karlis = Darbinieks(4, "Kārlis", 9001, "Direktors", 36)

print(janis)
print(eriks)
print(anna)
print(karlis)