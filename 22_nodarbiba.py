import sqlite3
db = sqlite3.connect("22_nodarbiba.db")
cur = db.cursor()

# cur.execute("DROP TABLE atzime")
# cur.execute("CREATE TABLE IF NOT EXISTS atzime (\
#             id INTEGER UNIQUE,\
#             prieksmets STRING,\
#             skolens STRING,\
#             atzime INTEGER,\
#             PRIMARY KEY (id AUTOINCREMENT)\
# )")

# Ievietojam vairākas rindas
# cur.execute('INSERT INTO atzime (prieksmets, skolens, atzime) VALUES\
#             ("Matemātika", "Jānis", 6), ("Lat. valoda", "Pēteris", 9),\
#             ("Matemātika", "Māris", 2), ("Vācu Valoda", "Jana", 4),\
#             ("Krievu Valoda", "Anna", 9)')

# cur.execute('SELECT skolens, atzime FROM atzime')
# cur.execute('SELECT prieksmets,skolens,max(atzime) FROM atzime') # min/max
# cur.execute('SELECT prieksmets,skolens,max(atzime) FROM atzime GROUP by prieksmets') # min/max
# Operatori: https://www.sqlite.org/lang_expr.html#operators_and_parse_affecting_attributes
# https://www.sqlitetutorial.net/sqlite-where/
#cur.execute('SELECT * FROM atzime WHERE atzime > 6')
#cur.execute('SELECT * FROM atzime WHERE atzime = 6')
#cur.execute('SELECT * FROM atzime WHERE atzime IS 6') # =, !=, >, <, ...
#cur.execute('SELECT * FROM atzime WHERE atzime <= 6')
#cur.execute('SELECT * FROM atzime WHERE atzime > 4 AND atzime < 8') # AND/OR
#cur.execute('SELECT * FROM atzime WHERE atzime BETWEEN 4 and 8')
#cur.execute('SELECT * FROM atzime WHERE id = 1 AND atzime = 6')
#cur.execute("SELECT * FROM atzime WHERE prieksmets LIKE 'mat%'")
#cur.execute("SELECT * FROM atzime WHERE prieksmets LIKE '%valoda'")
#cur.execute("SELECT * FROM atzime WHERE prieksmets LIKE '____ valoda'")
#cur.execute('SELECT atzime FROM atzime ORDER BY atzime, prieksmets') # DESC = Descending, ASC = Ascending
# cur.execute('SELECT atzime FROM atzime')
# results = cur.fetchmany(3)
# print(results)
# results = cur.fetchmany(3)
# print(results)
# cur.execute('SELECT atzime FROM atzime LIMIT 5')
# results = cur.fetchall()
# cur.execute('SELECT atzime FROM atzime WHERE id = 1')
# results = cur.fetchall()
# print(results)
# cur.execute("DELETE FROM atzime WHERE id = 1") # Strādā tie paši vaicājumi kas ar SELECT
cur.execute("PRAGMA foreign_keys = ON")
cur.execute("DROP TABLE atzime")
cur.execute("DROP TABLE skolens")
cur.execute("CREATE TABLE IF NOT EXISTS skolens (\
            id INTEGER UNIQUE,\
            vards STRING,\
            PRIMARY KEY (id AUTOINCREMENT)\
)")
cur.execute("CREATE TABLE IF NOT EXISTS atzime (\
            id INTEGER UNIQUE,\
            prieksmets STRING,\
            skolens integer,\
            atzime INTEGER,\
            PRIMARY KEY (id AUTOINCREMENT)\
            FOREIGN KEY (skolens) REFERENCES skolens(id) ON DELETE CASCADE\
)")
# ON DELETE RESTRICT - Neļauj dzēst, ja ir saistītas rindas
# ON DELETE CASCADE - dzēšot datus izdzēš saistītās rindas
cur.execute('INSERT INTO skolens (vards) VALUES\
            ("Jānis"), ("Pēteris"), ("Māris"), ("Anna")')
cur.execute('INSERT INTO atzime (prieksmets, skolens, atzime) VALUES\
            ("Matemātika", 1, 6), ("Lat. valoda", 2, 9),\
            ("Matemātika", 3, 2), ("Vācu Valoda", 3, 4),\
            ("Krievu Valoda", 4, 9)')

#cur.execute("DELETE FROM atzime WHERE id = 1")
cur.execute("DELETE FROM skolens WHERE id = 3")
cur.execute("SELECT * FROM atzime")
results = cur.fetchall()
print(results)

cur.close()
db.commit()
db.close()