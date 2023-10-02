def sum(param1, param2):
    return param1+param2
# sumSomething
# SumSomething
# sum_something

# Fun. pārrakstīšana
def vienkPrint(param1):
    print(param1)
def vienkPrint(param2):
    def kautkadaFun(param3):
        print("---")
    kautkadaFun(0)
    print("!!!")
y = vienkPrint(13) # !!!
print(y) # None

x = sum(10,2)
print(x)
print()

def vairakiParametri(param1, param2, *mainigais):
    print(param1)
    print(len(mainigais))
    print(mainigais[0])
    print(type(mainigais))
vairakiParametri(123,456,789)

def print2(*params):
    print(" ".join(str(params)))
print2("123", 213, 456)

def recurse(param1):
    print(param1)
    if param1 > 0:
        return recurse(param1-1)
    else:
        return
#recurse(10)

def factorial(n):
   if n == 1:
        return 1
   else:
        return n * factorial(n-1)
print(factorial(4)) # 4! = 4 * 3 * 2 * 1 (24)

# Uzdevums - Factoriālis kā while cikls?
skaititajs = 4
rezultats = 1
while True:
    rezultats *= skaititajs
    skaititajs -= 1
    if skaititajs == 1:
        break
print(rezultats)

#DefParam
def kFun(param1, darbibasTips = 1):
    if darbibasTips == 1:
        return param1 * param1
    elif darbibasTips == 2:
        return param1 * param1 * param1
print(kFun(2, 2))

#VS_Sintakse
def aprakstitaFun(param1 :int, param2: str = "asd")  -> int: # int, str
    """Kaut kāda dokumentācija"""
    print("kaut kas")
aprakstitaFun(0, 1)

#Faili
#import math
#math.ceil(2.3)
from mapeArFun.atseviskaFun import printSomething
printSomething("test")
# printSomething2("test2") # Nav definēts

# Uzdevums
# Lietotājs ievada vairākus skaitļus (potenciāli neierobežots skaits)
# Funkcija saskaita visus šos skaitļus
# Programma izvada šo skaitļu summu
def summa(lst):
    totalSum = 0
    for el in lst:
        totalSum += int(el)
    return totalSum
x = input()
print(summa(x.split(",")))
# x = [] 
# while True:
#     inp = input()
#     if inp != -1:
#         x.append(int(input))

# Uzdevums
def fun():
    x = []
    # Kā aizpildīt šo funkciju?
    return x
x = fun(6)
print(f"{x} == [ 2, 3, 5, 7, 11, 13 ]")
x = fun(7)
print(f"{x} == [ 2, 3, 5, 7, 11, 13, 17]")