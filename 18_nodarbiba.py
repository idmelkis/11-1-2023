# 1. Uzdevums
# import os
# import random

# if not os.path.isdir(f"faili"):
#     os.mkdir(f"faili")
# else:
#     print("Mape jau eksistē")

# for num in range(0, 101):
#     with open(f"faili/{num}", 'w') as f:
#         f.writelines(f"{random.randint(0, 1000)}")

# rand_fails = random.randint(0, 100)
# print(f"Lūdzu atverat failu {rand_fails}")
# ievade = input(f"Atverat failu fails/{rand_fails} un ievadat tā vērtību: ")

# with open(f"faili/{rand_fails}") as f:
#     saturs = f.readline().strip()
#     print(f"Saturs: {saturs}")
#     if (ievade == saturs) :
#         print("Pareizi")
#     else:
#         print("Nepareizi")

# import shutil
# shutil.rmtree(f'faili')

# 2. Uzdevums
# Uzrakstat programmu, kas atver failu, un izvada vārdu skaitu failā.
# with open(f"teksta_fails.txt") as f:
#     teksts = f.readline().strip()
#     skaits = len(teksts.split(" "))
#     print(f"Vārdu skaits: {skaits}")

# 3. Uzdevums
#* atver šo failu
# * izveido failu ar to pašu nosaukumu + "_uppercase"
# (piem. fails.txt -> fails_uppercase.txt). Ja fails jau eksistē izvadat kļūdu.
# * otrajā failā saglabājat pirmā faila saturu pārveidojot visus burtus par lielajiem.
import os
with open(f"teksta_fails.txt") as f1:
    nosaukums = f"teksta_fails_uppercase.txt"
    if not os.path.exists(nosaukums):
        with open(nosaukums, 'w') as f2:
            for line in f1:
                f2.writelines(f"{line.upper()}")
    else:
        print("Fails jau eksistē...")

# Eksistē fails ar sekojošu saturu:
# Izveidojat programmu, kas atver šo failu, un pievieno visas 3 C vērtības pēc darbībām.
# Nomainot vērtības failā, un palaižot programmu vajadzētu redzēt jaunās vērtības.
# Pieņemt, ka programmā VIENMĒR būs šāds formāts, un tikai 3 šādas darbības.

# 4. Uzdevums
# TODO: Šeit vēl vajag ielikt ciklā lai nolasītu VISAS rindas, ne tikai pirmās 3.
with open("fails.txt", 'r') as f:
    saturs = []
    for line in f:
        saturs.append(line)
    # max 3, 3 rindas
    # A = 5
    # B = 10
    # C = A - B
    A = int(saturs[0].split(" ")[2])
    B = int(saturs[1].split(" ")[2])
    darb = saturs[2].split(" ")[3]
    C = 0
    if darb == "-":
        C = A - B
    elif darb == "/":
        C = A / B
    elif darb == "*":
        C = A * B
    saturs.insert(3, f"C = {C}\n")
with open("fails.txt", 'w') as f:
    f.writelines(saturs)
