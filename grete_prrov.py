import random

def challenges(fail):
    mitu_rida = 0
    andmed = []
    f = open(fail, encoding='UTF-8')
    for rida in f:
        uus = rida.strip().split(': ')
        mitu_rida += 1
        andmed.append([int(uus[0]),uus[1:]])
    f.close()
    number = random.randint(1, mitu_rida)
    print(number)
    for paar in andmed:
        if number == paar[0]:
            küsimus = paar[1:]
    return küsimus

def tiles(position):
    if position == 1 or position == 10 or position == 16:
        valjakutse = challenges('truthordrink.txt')
    elif position == 4 or position == 11 or position == 18:
        valjakutse = challenges('generalknowledgeq.txt')
    elif position == 2 or position == 20:
        valjakutse = "EVERYBODY DRINKS!"
    elif position == 3 or position == 9:
        valjakutse = "Astu korra seadmega teistest eemale, et järgnevat küsimust näeksid ainult sina!"
        valjakutse = challenges('paranoia.txt')
    elif position == 5 or position == 15 or position == 19:
        valjakutse = challenges('dareordrink.txt')
    elif position == 6 or position == 14:
        valjakutse = challenges('neverhaveiever.txt')
    elif position == 7 or position == 12 or position == 17:
        valjakutse = challenges('baila.txt')
    elif position == 8:
        valjakutse = "LUCKY YOU! You can rest right now and not drink."
    elif position == 13:
        valjakutse = "Down your drink right this second and go make yourself a new one."
    return valjakutse

x = tiles(7)
print(x)


