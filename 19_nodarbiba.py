# import csv
# with open(f'17_nodarbiba.csv', 'r') as f:
#     csv_file = csv.reader(f, delimiter=' ')
#     next(csv_file) # !!!
#     for row in csv_file:
#         print(row)

rootDir = 'C:\\Users\\idmelkis\\Desktop\\0403uzd\\faili'
import csv

class Gene:
    HGNCID = ''
    Symbol = ''
    Name = ''
    EnsembleId = ''

    def __init__(self, hgnc, symbol, name) -> None:
        self.HGNCID = hgnc
        self.Symbol = symbol
        self.Name = name

    def __str__(self) -> str:
        return f"Nosaukums: {self.Name}\nSimbols:{self.Symbol}\nHGNC ID:{self.HGNCID}\nEnsemble ID:{self.EnsembleId}"
data = {} # Simbols - Objekts

with open(f'{rootDir}\\genenames_filtered.txt', 'r') as f:
    csv_file = csv.reader(f, delimiter='\t')
    next(csv_file) # !!!
    for row in csv_file:
        gene = Gene(row[0].strip(), row[1].strip(), row[2].strip())
        data[row[1].strip()] = gene

with open(f'{rootDir}\\mart_export_human_filtered.txt', 'r') as f:
    csv_file = csv.reader(f, delimiter='\t')
    next(csv_file) # !!!
    for row in csv_file:
        symbol = row[1].strip()
        if not symbol == '':
            if symbol in data.keys():
                data[symbol].EnsembleId = row[0].strip()

with open(f'{rootDir}\\export.txt', 'w') as f:
    for val in data.values():
        print(val)
        print()
        f.write(f"{val}\n\n")
