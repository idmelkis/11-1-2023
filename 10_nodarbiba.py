# Uzdevums: 
# Uzrakstīt programmu, kas izveido vārdnīcu kurai:
# * Atslēgas ir skaitļi no 1 - 10
# * Vērtības ir gadījumskaitlis (random)
# un izvada šo vārdnīcu.
import random
vardnica = {}
for x in range(1, 11):
    # vardnica[x] = random.randint(0, 99)
    vardnica.update({x: random.randint(0, 99)})

# Uzdevums:
# Apvienot vārdnīcas. Šai vārdnīcai jābūt atsevišķai.
dict1 = {
    1: 10,
    2: 20,
    3: 30
}
dict2 = {
    4: 40,
    5: 50,
    6: 60
}
dict3 = { 
    # ...
}

# Ar for ciklu
for i,j in dict1.items():
    dict3[i] = j
for i,j in dict2.items():
    dict3[i] = j
# VAI
# for i in (dict1, dict2):
#     dict3.update(i)
print(dict3)

# Uzdevums
# Apvienot abus sarakstus lai izveidotu vārdnīcu
# Garantēts, ka abi saraksti būs vienāda garuma
keys = [ "atslēga1", "atslēga2", 456 ]
values = [ 123, "342", [2, 3, 4] ]

# dict = {}
# for i in range(0, len(keys)):
#     # print(keys[i])
#     # print(values[i])
#     dict[keys[i]] = values[i]
#     # dict.update({keys[i]: values[i]})
# print(dict)

print(dict(zip(keys, values)))

# Uzdevums (i/ni):
import random
dict1 = {}
for i in range(0, 20):
    dict1[i] = random.randint(0, 1000)
# Izveidot vārdnīcu, kurā atrodas atslēgas un vērtības no dict1, 
# tām atslēgām kurām vērtības ir > 500, un izprintēt to.
# Piem, ja
# dict1 = {
#   1: 100,
#   2: 600,
#   3: 200,
#   4: 800
# }, tad
# dict2 = {
#   2: 600,
#   4: 800
# }
# Iesniegt e-klasē pie MD uzdevumu iesniegšanas.