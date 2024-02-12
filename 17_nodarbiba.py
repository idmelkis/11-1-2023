import os
import csv

currentPath = os.path.dirname(__file__)
tempDir = f"{currentPath}\\temp"
if not os.path.isdir(tempDir):
    os.mkdir(tempDir)

# with open(f'{tempDir}\\fails.txt', 'w') as f:
#     f.writelines("123 312\n")
#     f.writelines("444 555\n")
# Uzdevums: Atvērt failu ar saturu:
# 10 + 2
# 9 - 4
# 10 / 2
# 15 * 3
# with open(f'{tempDir}\\uzdevums.txt', 'r') as f:
#     for line in f.readlines():
#         strippedLine = line.strip()
#         print(strippedLine, end="")
#         # match: https://stackoverflow.com/a/11479840 (Python > 3.10)
#         splitLine = line.split(' ')
#         # TODO: Pārbaudīt vai elementi ir skaitļi
#         if splitLine[1] == "+":
#             print(f" == {int(splitLine[0]) + int(splitLine[2])}")
#         elif splitLine[1] == "-":
#             print(f" == {int(splitLine[0]) - int(splitLine[2])}")
#         elif splitLine[1] == "/":
#             print(f" == {int(splitLine[0]) / int(splitLine[2])}")
#         elif splitLine[1] == "*":
#             print(f" == {int(splitLine[0]) * int(splitLine[2])}")

with open(f'{tempDir}\\uzdevums_2.txt', 'w+') as f:
    csv_writer = csv.writer(f, delimiter=" ")
    csv_writer.writerow(["1", "2", "3"])
    csv_file = csv.reader(f, delimiter=' ')
    for row in csv_file:
        print(row)