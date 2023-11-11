import random

mitu_mängijat = input('Sisesta mängijate arv: ')
#genereeri igale mängijale nupp ja oma muutuja
for mängija in range(1, mitu_mängijat + 1):
    player[mängija] = 0
    






mitu_rida = 0
andmed = []
f = open(fail, encoding='UTF-8')
for rida in f:
    uus = rida.strip().split(': ')
    mitu_rida += 1
    andmed.append([int(uus[0]),uus[1]])
f.close()
number = random.randint(1, mitu_rida)
print(number)
for paar in andmed:
    if number == paar[0]:
        print(paar[1])


