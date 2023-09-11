# nosaukums = vērtība
y = 20
x = str(10) + "10" + ' ' + str(y)
#print("11-1")
# Izvade
print(x)
print(f"{str(10)}10 {y}") # Formatēts teksts 

# Vairāku rindu izvade
print("""rinda1
      rinda2
      rinda3""")
print("rinda1\nrinda2\nrinda3")

# Ievade
n = input("Ievade: ")
print(n)
#if <> :
#    <>
if not n == "10":
   print("Pareizi")

# Loģika
#log = True # False
log = 1 == 1
if log:
    print("Vajadzētu būt true")
if not "" is "1":
    print("Not is -- True")
x = [ "123", "234", "456" ]
print(x[2])

"""
Kā piekļūst atmiņai:
y = 2
x[y]
# size(str) == 4
1ae + size(str) * y
1ae: 0000 0100 0001
"""