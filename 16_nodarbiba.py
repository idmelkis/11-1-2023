# class Klase:
#     def __init__(self) -> None:
#         self.test = 0
#     def kautkadaFunkc(self):
#         c = 10
#         def kautkasVel():
#             print(self.test)
#         kautkasVel()

# a = Klase()
# a.kautkadaFunkc()

# a = 10
# import math
# math.floor(a)

# # traceback
# # stack trace

# def funkc():
#     global a
#     b = 10
#     # print(a.test)
#     print(b)
#     return 0
# funkc()

# c = [ 10, 20, 30 ]

# a = 10
# a = a * 5
# a = a - 4
# print(a)

# i = 10
# j = 5
# k = i % j
# l = i/k

# Uzdevums: Kur ir kļūdas?
# Funkcijas uzdevums - izvadi mazāko vērtību sarakstā
# def min(list):
#     a = list[0] # Šeit bija 0, ielikām pirmo vērtību.
#     for x in range(1, len(list)):
#         if list[x] < a:
#             a = list[x]
#     return a
# print(min([20, 10, 30]))

# Exception tipi: https://docs.python.org/3/library/exceptions.html
# import traceback
# class Klase:
#     def __init__(self) -> None:
#         self.test = 0
#     def kautkadaFunkc(self):
#         c = 10
#         def kautkasVel():
#             traceback.print_stack()
#             ievade = input("Ievadat")
#             rezultats = ievade / 10
#         kautkasVel()

# a = Klase()
# a.kautkadaFunkc()

class ManaKluda(Exception):
    def __init__(self, *args: object) -> None:
        for a in args:
            print(f"Atradām kļūdu: {a}")
        super().__init__(*args)
# raise ManaKluda("a", "b")

import traceback
class Klase:
    def __init__(self) -> None:
        #f = open("fails.txt")
        try:
            a = 10
            b = 20
            if b > a:
                pass
                #raise ValueError("B vajadzētu būt mazākam")
                #raise Exception("a")
            #raise NotImplementedError("Komentārs") # throw
            raise ManaKluda("asd", "sad")
        except ValueError as e: # catch
            print(f"Bija kļūda: {e}")
        except ZeroDivisionError as e:
            print(f"Bija kļūda: {e}")
        except ManaKluda as b:
            print(b)
            traceback.print_exc()
            raise b
        except:
            print("Nezināma kļūda")
        finally:
            #f.close()
            print("beidzās")

try:
    a = Klase()
except:
    print("Notika kļūda")

def ievaditSkaitli():
    while True:
        ievade = input("Ievadat")
        # if not type(ievade) == int:
        #     raise Exception("Lūdzu ievadat skaitli")
        try:
            ievade = int(ievade)
            return ievade
        except ValueError as e:
            print("Lūdzu ievadat skaitli")
rezultats = ievaditSkaitli() / 10
print(rezultats)