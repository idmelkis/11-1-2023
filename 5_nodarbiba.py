# Uzdevums:
# 1. Funkcija, kas atrod saraksta maksimālo vērtību
# 2. Funkcija, kas atrod saraksta minimālo vērtību
# Neizmantot builtin, math funkcijas
x = [ 8, 4, 4, 6, 123, 55, 4]
def a_min(x):
    mazakais = None
    for i in x:
        if mazakais == None:
            mazakais = i
        elif i < mazakais:
            mazakais = i
    return mazakais
print(a_min(x))

def a_max(x):
    lielakais = None
    for i in x:
        if lielakais == None:
            lielakais = i
        elif i > lielakais:
            lielakais = i
    return lielakais
print(a_max(x))
print()

a = 10
def fun():
    global a
    a = 14
    print(a)
fun()
print(a)

# Uzdevums: Apmainat vietām mainīgo a un b vērtības
import random
a = int(random.random()*100)
b = int(random.random()*100)
print(a, b)
def swap():
    global a, b
    c = a
    a = b
    b = c
swap()
print(a, b) # Vajadzētu izvadīt iepriekšējās vērtības, bet otrādi.
