# from pathlib import Path
# Path.absolute()
# import sys
# print(sys.argv[0])
import os

# Faila atrašanās vieta
#print(os.path.realpath(__file__))
currentPath = os.path.dirname(__file__)
print(currentPath)
# Mapes izveide
# try:
#     os.mkdir("mapes_nosaukums")
# except:
#     print("Mape jau eksistē")
# 
if not os.path.isdir(f"{currentPath}\\mapes_nosaukums"):
    os.mkdir(f"{currentPath}\\mapes_nosaukums")
else:
    print("Mape jau eksistē")
print()
fileName = f'{currentPath}\\mapes_nosaukums\\failanosaukums.txt'
with open(fileName, 'w') as f:
    f.writelines("123")
print(os.path.exists(f"{currentPath}\\mapes_nosaukums\\failanosaukums.txt"))
# Izdzēst mapi ar visiem failiem
# 1. var
#import shutil
#shutil.rmtree(f'{currentPath}\\mapes_nosaukums\\')
# 2. var
# for file in os.listdir(f"{currentPath}\\mapes_nosaukums"):
#     os.remove(f"{currentPath}\\mapes_nosaukums\\{file}")
# os.rmdir(f"{currentPath}\\mapes_nosaukums")
# Dzēst failu
# os.remove(fileName)