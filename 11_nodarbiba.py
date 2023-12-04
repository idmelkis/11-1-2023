# pop
# vardnica = {
#     "elements1": 0,
#     "elements2": 1,
# }
# print(vardnica)
# vardnica.pop("elements1")
# print(vardnica)

# saraksts = [ 0, 1, 2 ]
# print(saraksts)
# saraksts.pop(1)
# print(saraksts)

# # Uzdevums
# # Izņemiet katru otro vērtību (pāra skaitļa atslēgas)
# # no vārdnīcas vardnica
# import random
# vardnica = {}
# for i in range(0, 100):
#     vardnica[i] = random.randint(0, 100)
# #print(vardnica)
# sar = list(vardnica.keys())
# #i = 0
# # while i <= len(vardnica.keys()):
# #     vardnica.pop(sar[i])
# #     i += 2
# # for i in range(0, 100):
# #     if i % 2 == 0:
# #         vardnica.pop(i)
# for i in range(0, len(vardnica.keys())-1, 2):
#     vardnica.pop(sar[i])
# print(vardnica)

# json
# vardnica = {
#     "123": 213,
#     "Var": False,
#     2: True,
#     "Ok": -1
# }
import json
# jsontxt = json.dumps(vardnica)
# print(jsontxt)
# print(type(jsontxt))
# jsontxt = '{"123": 213, "Var": false, "2": true, "Ok": -1}'
# vardnica = json.loads(jsontxt)
# print(vardnica)

# Faila atvēršanas tipi (modes) -
# https://www.w3schools.com/python/ref_func_open.asp
# with open('nosaukums.txt', "w") as f:
#     f.write("tests")

# Vecāka sintakse - obligāti jaatceras, ka failu vajag aizvērt ar .close()!
#file = open('nosaukums.txt', "w")
#file.close()

# Uzdevums: Izvadīt skaitļus 1 līdz 100 failā nosaukums.txt
# with open('nosaukums.txt', "w") as f:
#     for i in range(0, 100):
#         f.write(str(i) + "\n")

# Lasīšana
# lines = ""
# with open('nosaukums.txt', "r") as f:
#     curLine = f.readline() # Ielasa pirmo rindu
#     # Ielasa pārējās rindas:
#     while curLine:
#         lines += curLine
#         curLine = f.readline()
# print(lines)

# vardnica = {
#     "123": 213,
#     "Var": False,
#     2: True,
#     "Ok": -5
# }
# #json.dump()
# with open('nosaukums.txt', "w") as f:
#     json.dump(vardnica, f)
# with open('nosaukums.txt', "r") as f:
#     vardnica = json.load(f)
#     print(vardnica)
#json.loads()