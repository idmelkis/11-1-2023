# Polimorfisms - Bez mantošanas
# class Tramvajs:
#     krasa :str = "Balta"
#     def print_something(self) -> None:
#         print(f"Krāsa: {self.krasa}")
# class Auto:
#     brends :str = "BMW"
#     def print_something(self) -> None:
#         print(f"Brends: {self.brends}")
# tramvajs = Tramvajs()
# auto = Auto()
# for i in (tramvajs, auto):
#     # Vienāda funkcija abām klasēm, bet atšķiras tās rezultāts
#     i.print_something()

class Transportlidzeklis:
    krasa :str = "Melna"
    marka :str = "Bāzes transportlīdzeklis"
    atrums :float = 0.0
    def __init__(self) -> None:
        print("Transportlīdzeklis")
    def nokraso(self, krasa :str) -> None:
        self.krasa = krasa
    def paatrinasana(self):
        self.atrums += 0.5
    def bremzesana(self):
        if (self.atrums >= 0.5):
            self.atrums -= 0.5
class Tramvajs(Transportlidzeklis):
    marka = "Skoda"
    def __init__(self) -> None:
        print("jauns tramvajs")
        print(self.krasa)
    def paatrinasana(self):
        print("Tramvajs brauc ātrāk...")
        self.atrums += 1
class Auto(Transportlidzeklis):
    marka = "BMW"
    def paatrinasana(self):
        self.atrums += 3
    def print_bazes_marka(self):
        print(super().marka)
        
auto = Auto()
auto.print_bazes_marka()

# jauns_tramvajs = Tramvajs()
# jauns_tramvajs.nokraso("Zala")
# print(jauns_tramvajs.krasa)
# jauns_tramvajs.paatrinasana()
# print(jauns_tramvajs.atrums)

# transports = Transportlidzeklis()
# print(transports.mainigais)

# Uzdevums: Izstrādāt 3 klases (1 bāzes, 2 apakšklases (mantojošās klases))
# Bāzes klasei - vismaz 2 mainīgie, 1 funkcija (ne predefinēt, t.i. __init__, __str__)
# Apakšklasēm - izmantot polimorfismu lai pārrakstītu funkciju tā, lai tā katrai klasei
# darītu dažādas lietas (pietiek ar to, ka izmanto print() un atšķiras izvade).

# Uzdevums i/ni: Izveidot programmu un klašu grafiku
# Jāizveido klase "Banka Kontss". 
# * Šai klasei jāglabā informācija par lietotājam pieejamajiem naudas līdzekļiem.
# * Izveidojat funkcijas, kas ļauj ieskaitīt vai izņemt naudu no konta
# * Neļaut lietotājam izņemt naudu, ja ir zem €50, vai, ja izņemot paliktu zem €30
# Izveidojat apakšklasi "Krājkonts".
# * Izmantot polimorfismu lai pārrakstītu izņemšanas funkciju, 
#   lai tā kopā ar izņemto naudu izņem vēl 10%
#   (t.i. izņemot €100, izņems €110)
#   Neļaujat izņemt lietotājam naudu, ja ir zem €50, vai, ja izņemot paliktu zem €30
# Izveidojat objektus no šīm klasēm
# Izsaucat pirmās klases ieskaitīšanas funkciju (€100), 
#   izsaucat izņemšanas funkciju €60.
#   izsaucat izņemšanas funkciju €80.
# Izsaucat otrās klases ieskaitīšanas funkciju (€100), 
#   un izsaucat izņemšanas funkciju €30