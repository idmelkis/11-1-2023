# 1. Uzdevums
# Nolasiet datus no dotā faila 
# Formāts
# {Date: {year: 2024, date: 25, month: 03}, ...}
# Un saglabājiet tos vārdnīcā.
# Izvadat šo vārdnīcu
# Fails:
# http://s.ayy.lv/11-1
# konfiguracija = {}
# with open('20_nodarbiba.ini', 'r') as f:
#     galvene = ""
#     for line in f:
#         if line.startswith('['):
#             galvene = line[line.index('[') + 1 : line.index(']')]
#             konfiguracija[galvene] = {}
#         else:
#             ieraksts = line.split('=')
#             konfiguracija[galvene][ieraksts[0].strip()] = ieraksts[1].strip()
# print(konfiguracija)

# Šis fails ir .ini fails - to var nolasīt arī citādāk
# https://en.wikipedia.org/wiki/INI_file
import configparser
from pathlib import Path
# Nestrādā -- ar file strādās tikai parser.write()
# with open('20_nodarbiba.ini', 'r', encoding='utf-8') as f:
#     parser = configparser.ConfigParser()
#     parser.read(f, encoding='utf-8')
#     print(parser.sections())
#     print('date' in parser)
fails = Path('20_nodarbiba.ini')
parser = configparser.ConfigParser()
parser.read(fails)
print(parser.sections())
print(parser['date'].get('year'))

# Rakstīšana
conf = configparser.ConfigParser()
conf['HEADER'] = {}
conf['HEADER']['key'] = 'value'
conf['HEADER']['key2'] = 'value'
# ==
#conf_var = { 'HEADER': { 'key': 'value', 'key2': 'value' }}
fails2 = Path('20_nodarbiba_.ini')
with open(fails2, 'w', encoding='utf-8') as f:
    conf.write(f)