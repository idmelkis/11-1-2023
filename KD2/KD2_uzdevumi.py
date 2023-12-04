# Var pildīt mājās. Termiņš līdz nākošajai nedēļai. Par katru uzdevumu ir līdz 3 punktiem - 3 ir perfekti izpildīts, 2 ir izpildīts bet ar mazām kļūdām, 1 ir 'iesākts', un 0 ir 'neiesākts'.
# Dotos koda piemērus nemainīt - tikai papildināt

# 1. Uzdevums - piekļuve vārdnīcu vērtībām
# Ir dota sekojoša programma. Papildinat to, lai izvadītu atslēgu un vērtību pāri lielākajai un mazākajai dict1 vērtībai.
# piemēram vārdnīcai { 0: 100, 1: 2, 3: 400 } rezultāts būtu - "Lielākā - 3: 400, mazākā 1: 2".
import random
dict1 = {}
for i in range(0,100):
    dict1.update({i: random.randint(0, 1000)})
# ...

# 2. Uzdevums - vārdnīcu izveide
# Ir doti divi saraksti. Izveidojat vārdnīcu (izmantojot ciklus) no šiem sarakstiem, kur atslēgas ir šo sarakstu individuālu vērtību kombinācijas, un vērtības ir gadījumskaitļi no 1 līdz 10.
# Piemēram, ja 
# a = [ 'a', 'b' ] un b = [ 'c', 'd' ], tad
# vardnica = { 'ac': 10, 'ad': 4, 'bc': 6, 'bd': 1 }
a = [ 'a', 'b', 'e', 'f' ]
b = [ 'c', 'g', 'h', 'z' ]
vardnica = {}
# ...

# 3. Uzdevums - Vērtību dzēšana
# Ir dota sekojoša programma, kas izveido vārdnīcu dict1. Papildinat šo programmu tā,
# lai šī programma izveidotu _izdzēstu_ vērtības no dict1, kas ir mazākas par 500.
# Nedrīkst veidot atsevišķu vārdnīcu vai papildus mainīgos - visām darbībām jānotiek ar dict1.
import random
dict1 = {}
for i in range(0,100):
    dict1.update({i: random.randint(0, 1000)})
# ...

# 4. Uzdevums - Vērtību ielāde un apstrāde
# Ir dots fails 'uzdevums.json'. Šis fails satur vārdnīcu json formātā. Atverat šo failu un izvadat šīs vārdnīcas vērtības formātā 
# "Atslēga: <atslēga>, Vērtība: <vērtība>" (ieskaitot leņķa iekavas - <>).
import json
# ...

# 5. Uzdevums - Vērtību glabāšana
# Izveidot programmu, kas nodrošina -
# Vairāku (! - saraksts) cilvēku informācijas ievadi - vārdu, uzvārdu, vecumu. Informāciju par individuālu cilvēku glabāt vārdnīcā ar atslēgām "vards", "uzvards" un "vecums".
# Šīs informācijas izvadi failā ar nosaukumu 'dati.json'.
import json
# ...