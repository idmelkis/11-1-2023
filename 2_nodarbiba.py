x = [ "123", "234", "456" ]
print(x[2])
print(x[:2])
print(x[:-2])
#print("".join(x))

y = [ "T", str(2) ,"k" ]
print(y[:2])
print(",".join(y))

x = "Teksts"
print(x[4])
print(x[3:5])
print(x[:5])

# Ievade: Cilvēka vārds
# Izvade: "Sveiks vārd!" 
# piem. Jānis -> Sveiks Jāni!
#x=input("Vārds: ")
#print(f"Sveiks {x[:-1]}!")

x = ( "123", "3123", "432" )
#x[2] = "sada" # Kļūda
print(len(x))

"""
x = True
while x:
    ...
    x = False
"""
print("\n")
x = [ 123, 456, 678 ]
for y in x:
    print(y+400)

idx = 0
while idx < len(x):
    print(x[idx]+400)
    idx+=1

# Ievadat cik skaitļus ievadīt
# Ievadat ciklā vairākus skaitļus
# Izvadat šo skaitļu summu
#list.append("...")
# For cikls
"""
x = int(input("Skaitļu skaits"))
y = []
for z in range(0, x):
    y.append(int(input(f"Skaitlis {z}: ")))
result = 0
for z in range(0, len(y)):
    result += y[z]
print(result)
"""
"""
x = int(input("Skaitļu skaits"))
result = 0
for z in range(0, x):
    result += int(input(f"Skaitlis {z}: "))
print(result)
"""

# While cikls
x = int(input("Skaitļu skaits"))
idx = 0
y = []
#result = 0
while idx < x:
    y.append(int(input(f"Skaitlis {idx}: ")))
    idx += 1
print(y)

