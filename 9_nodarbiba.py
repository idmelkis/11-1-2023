a = "123"

b = {
    "a": "123",
    "b": "312",
    4: True,
    "cookie": "A small, usually flat and crisp cake made from sweetened dough"
}
print(b["a"])

burti = {
    "ā": "a",
    "ē": "e",
    "ū": "u",
    "ī": "i",
    "š": "s",
    "č": "c",
    "M": "K"
}
#saraksts = [ "ā", "ē", "ū" ]
#if "M" in saraksts:
def changeLetter(text):
    newWord = ""
    y = 0
    while y < len(text):
        print(f"Burts: {text[y]} (tiek izmantota kā atslēga)")
        if text[y] in burti:
            newWord += burti[text[y]]
            print(f"No vārdnīcas iegūts burts: {burti[text[y]]} (iegūtā vērtība)")
        else:
            newWord += text[y]
        y += 1
    return newWord
print(changeLetter("Māja"))
print(changeLetter("Mašīna"))
print(changeLetter("Vējš"))
print()

saraksts = [0, 1]
saraksts.append(2)
saraksts[2] = 3

vardnica = {
}
print(vardnica)
vardnica["23"] = 3
vardnica[4] = ":)"
vardnica[True] = 2
print(vardnica)
print(vardnica[True])
vardnica.update({"atslega": "vertiba", "atslega2": "vertiba"})
print(vardnica)

# Uzdevums
# Uzrakstīt programmu, kas izveido vārdnīcu, kurā atslēgas ir skaitļi no 1 līdz n (lietotāja ievadīts skaitlis) 
# un vērtības ir šis skaitlis kvadrātā.
# Piemērs:
# Ievade: 5
# Izvade: 
# {
#   1: 1
#   2: 4
#   3: 9
#   4: 16
#   5: 25
# }
# skaitlis = int(input("Ievadiet skaitli: "))
# vardnica = {}
# vardnica2 = {}
# y = 1
# while y <= skaitlis:
#     vardnica[y] = y*y
#     vardnica2.update({y: y*y})
#     y += 1
# print(vardnica)
# print(vardnica2)

# Uzdevums: Pacelt vērtības iekš vārdnīcas kvadrātā
vardnica = {
    1: 1,
    "a": 2,
    3: 3
}
# Rezultāta piemērs:
# {
#    1: 1,
#    2: 4,
#    3: 9
# }
for key in vardnica.keys():
    vardnica[key] = vardnica[key] * vardnica[key]
print(vardnica)

print('-'*10)
for key in vardnica.keys(): # vardnica.keys() == [ 1, 2, 3 ] no vārdnīcas
    print(f"Atslēgas: {key}")
print('-'*10)
for value in vardnica.values(): # vardnica.keys() == [ 1, 4, 9 ] no vārdnīcas
    print(f"Vērtības: {value}")
print('-'*10)
for key, value in vardnica.items():
    print(f"Atslēgas {key} vērtība ir {value}")
print('-'*10)