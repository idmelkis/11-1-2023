# For cikls, kas izvada skaitļus no 0 līdz 10, bet izlaiž skaitļus 4 un 6.
#for x in range(0, 11):
    #if x != 4 or x != 6:
    #    print(x)
    # if x == 4 or x == 6:
    #     continue
    #break
    #print(x)

# Izvada katru n elementu (pirmais::otrais el).
x = [ 123, 456, 678, 895 ]
for y in x[0::1]:
    print(y)

# FizzBuzz
# Cikls - 0, 100
# Jāizvada skaitlis, bet ja skaitlis dalās ar 3 - Izvadam Fizz, ja ar 5 - Buzz
# Ja dalās ar 3 un 5 - izvada FizzBuzz. Jāizmanto: % operators (dalījuma atlikums)
# Piem. izvade:
# 1
# 2 
# Fizz
# 4
# Buzz
# 6
# [..]
# 14
# FizzBuzz
# 16

# Izveidot programmu ar sekojošu izvadi:
# Hint: Cikls ciklā
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# Spēle: Uzmini skaitli
# Spēle uzģenerē nejaušu skaitli:
#import random
#x = int(random.random() * 100)
# Ciklā: Lietotājs ievada skaitli (input).
# Programma pārbauda vai skaitlis ir uzminēts, ja nav pasaka vai ievadītais
# skaitlis ir lielāks, vai mazāks par nejaušo skaitli.
# Visas lietotāja ievades (minējumus) jāsaglabā sarakstā
# Kad lietotājs ir uzminējis skaitli - 
# Izvadīt 'Uzvara'
# Izvadīt minējumu skaitu (len(...)), lietotāja minējumus
