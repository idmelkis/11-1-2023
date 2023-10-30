# 1. Uzdevums
# Uzrakstīt funkciju, kas ar cikla palīdzību izvada noteikta burta
# atrašanās vietu vārdā
# Piem. vārds Siers - 1,5
def findLetter(text):
    y = 0
    while y < len(text):
        if text[y] == 's' or text[y] == 'S':
            print(y+1, end=' ')
        y += 1
    #for y in range(0, len(text)):
        # ...
findLetter("siers")
print()
findLetter("skurstenis")
print()
findLetter("kautkādS vārds")
print()

# 2. Uzdevums
# Neizmantojot replace funkcijas - Uzrakstīt ciklu, kas noņem garumzīmes
# patskaņiem (ā, ī, ū, ē) vārdā
# Piem. Māja -> Maja
# Vējš -> Vejš
def changeLetter(text):
    """
    newWord = ""
    y = 0
    while y < len(text):
        if text[y] == 'ā':
            newWord += 'a'
        elif text[y] == 'ī':
            newWord += 'i'
        elif text[y] == 'ū':
            newWord += 'u'
        elif text[y] == 'ē':
            newWord += 'e'
        else:
            newWord += text[y]
        y += 1
    return newWord
    """
    y = 0
    while y < len(text):
        if text[y] == 'ā':
            text = text[:y] + 'a' + text[y+1:]
        elif text[y] == 'ī':
            text = text[:y] + 'i' + text[y+1:]
        elif text[y] == 'ū':
            text = text[:y] + 'u' + text[y+1:]
        elif text[y] == 'ē':
            text = text[:y] + 'e' + text[y+1:]
        y+=1
    return text
print(changeLetter("Māja"))
print(changeLetter("Mašīna"))
print(changeLetter("Vējš"))
print()

# 3. Uzdevums
# Uzrakstīt funkciju, kas apvieno (nevis pievieno galā, t.i. append) sarakstus
# x1 = [ 10, 20, 30 ], x2 = [ 50, 60, 70 ]
# Rezultāts = [ 10, 50, 20, 60, 30, 70 ]
def mergeLists(x1, x2):
    result = []
    # Mājās varat padomāt: Kā rīkoties, ja abi saraksti nav vienāda garuma
    y = 0
    while y < len(x1):
        result.append(x1[y])
        result.append(x2[y])
        y += 1
    return result
print(mergeLists([10, 20, 30], [50, 60, 70]))

# 4. Uzdevums
# Uzrakstīt programmu - spēli 'Uzmini skaitli', kurā spēlētājam ir 5 dzīvības
# Uzzīmēt blokshēmu šai programmai.
import random
skaitlis = int(random.random()*100)
dzivibas = 5
while dzivibas > 0:
    minejums = int(input("Minējums: "))
    if minejums==skaitlis:
        break
    elif minejums > skaitlis:
        print("Skaitlis ir mazaks")
    else:
        print("Skaitlis ir lielaks")
    dzivibas = dzivibas - 1

if dzivibas > 0:
    print("Uzvara")
else:
    print("Zaudejat")
print(f"skaitlis bija '{skaitlis}'!")