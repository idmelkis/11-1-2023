class Lietotajs:
    ID: int
    Lietotajvards: str
    Parole: str
    EPasts: str
    def __init__(self, id, lietotajvards, parole, epasts) -> None:
        self.ID = id
        self.Lietotajvards = lietotajvards
        self.Parole = parole
        self.EPasts = epasts
    def __str__(self) -> str:
        return f"{self.ID}: {self.Lietotajvards} -- {self.EPasts}"

lietotajs1 = Lietotajs(1, "Lietotajs", "****", "mail@mail.com")
lietotajs2 = Lietotajs(1, "Lietotajs2", "****", "mail@mail.com")

import sqlite3

db = sqlite3.connect("21_nodarbiba.db")
cur = db.cursor()

# https://www.sqlite.org/lang_createtable.html
# https://www.sqlite.org/datatype3.html
# Boolean
# 0 = False
# 1, Jebkas cits = True
# DROP TABLE <nosaukums>
create_table = f"CREATE TABLE IF NOT EXISTS lietotajs (\
    id INTEGER NOT NULL UNIQUE,\
    lietotajvards TEXT NOT NULL UNIQUE,\
    parole TEXT,\
    epasts TEXT UNIQUE,\
    PRIMARY KEY(id AUTOINCREMENT)\
)"
cur.execute(create_table)

create_table = f"CREATE TABLE IF NOT EXISTS ieraksts (\
    id INTEGER NOT NULL UNIQUE,\
    lietotajsID INTEGER NOT NULL UNIQUE,\
    virsraksts TEXT,\
    pamatteksts TEXT,\
    redzams INTEGER,\
    PRIMARY KEY(id AUTOINCREMENT)\
)"
cur.execute(create_table)

# https://www.sqlite.org/lang_insert.html
# insert_data = f'INSERT INTO lietotajs (lietotajvards, parole, epasts)\
#     VALUES ("{lietotajs1.Lietotajvards}3", NULL, "{lietotajs1.EPasts}3")'
# insert_data = f'INSERT INTO lietotajs (lietotajvards, parole, epasts)\
#     VALUES ("lietotajs", NULL, "pasts@mail.com")'
# cur.execute(insert_data)

# Ieraksts tabulā "ieraksts":
# lietotajsID: 1
# Virsraksts: "Sveika pasaule"
# Pamatteksts: "Sveika pasaule!!!!"
# Redzams: True (1)
# insert_data = f'INSERT INTO ieraksts (lietotajsID, virsraksts, pamatteksts, redzams)\
#     VALUES (1, "Sveika pasaule", "Sveika pasaule!!!!", 1)'
# cur.execute(insert_data)

# https://www.sqlite.org/lang_select.html
#get_data = 'SELECT (id, lietotajvards, parole, epasts) FROM ...' 
get_data = 'SELECT * FROM lietotajs'
cur.execute(get_data)
lietotaji = cur.fetchall()
for lietotajs in lietotaji:
    cl_lietotajs = Lietotajs(lietotajs[0], lietotajs[1], lietotajs[2], lietotajs[3])
    cl_lietotajs.Lietotajvards
    print(cl_lietotajs)

get_data = 'SELECT * FROM lietotajs WHERE (ID = 2)'
cur.execute(get_data)
lietotajs = cur.fetchone()
print(lietotajs)

cur.close()
db.commit()
db.close()

# with sqlite3.connect("21_nodarbiba.db") as db:
#     0_0
