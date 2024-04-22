import sqlite3
db = sqlite3.connect("23_nodarbiba.db")
cur = db.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS piegadatajs (\
            id INTEGER UNIQUE,\
            nosaukums STRING,\
            adrese STRING,\
            kontakti STRING,\
            PRIMARY KEY (id AUTOINCREMENT)\
)")
cur.execute("PRAGMA foreign_keys = ON")
cur.execute("CREATE TABLE IF NOT EXISTS produkts (\
            id INTEGER UNIQUE,\
            nosaukums STRING,\
            piegadatajs INTEGER,\
            cena FLOAT,\
            PRIMARY KEY (id AUTOINCREMENT)\
            FOREIGN KEY (piegadatajs) REFERENCES piegadatajs(id) ON DELETE RESTRICT\
)")
# cur.execute("INSERT INTO piegadatajs (nosaukums, adrese, kontakti)\
#             VALUES\
#             (\"KKAS\", \"NEKURIENE\", \"+3710000000\")")
# cur.execute("INSERT INTO piegadatajs (nosaukums, adrese)\
#             VALUES\
#             (\"CITS\", \"LATVIJA\")")
# cur.execute("INSERT INTO produkts (nosaukums, piegadatajs, cena) VALUES\
#             (\"Telefons\", 1, 1000.0),\
#             (\"Dators\", 1, 2500.0),\
#             (\"Burtnica\", 2, 2.0),\
#             (\"Soma\", 2, 50.0)")
# cur.execute("SELECT * FROM produkts")
# cur.execute("DELETE FROM piegadatajs WHERE id = 1")
# print(cur.fetchall())
cur.close()
db.commit()
db.close()