import random

print("Labdien, laipni lūgti lidostas lidO2 programmā.")
def datums():
    import datetime
    datums_ar_laiku = datetime.datetime.now()
    datums = datums_ar_laiku.strftime('%d-%m-%Y')

    from datetime import datetime

    datetime_datums = datetime.strptime(datums,'%d-%m-%Y')
    izveletais_datums = datetime.strptime(input('Ieraksti datumu kurā gribi lidot dd-MM-gggg: '),'%d-%m-%Y')
    while True:
        if izveletais_datums <= datetime_datums:
            izveletais_datums = datetime.strptime(input('Kļūda! Datums nedrīkst būt agrāks par rītdienu: '),'%d-%m-%Y')
        else:
            break
        print('===================')
        return izveletais_datums

datums()
#4 saraksti ar vajadzīgo informāciju sastāvā
reisa_numurs = [234, 156, 780, 356, 987, 404, 342, 764, 900, 135]
reisa_galamerkis = ["Vācija", "Francija", "Nīderlande", "Polija", "Spānija", "Itālija", "Portugāle", "Grieķija", "Dānija", "Zviedrija"]
reisa_laiks = ["10-10", "18-35", "09-15", "05-30", "12-00", "15-00", "23-30", "22-10", "13-00", "05-20"]
reisa_cena = ["47 EUR", "150 EUR", "3734 EUR", "10000 EUR", "265 EUR", "354 EUR", "1200 EUR", "570 EUR", "988 EUR", "155 EUR"]

#KLASE reiss?
def reiss(reisa_numurs, reisa_galamerkis, reisa_laiks, reisa_cena):
    reiss = random.choice(reisa_numurs)
    galamerkis = random.choice(reisa_galamerkis)
    laiks = random.choice(reisa_laiks)
    cena = random.choice(reisa_cena)
    return f"{reiss} - {galamerkis} - {laiks} - {cena}"



print("="*20)
print("Reisa izvēle: ")
#For cikls, kas iziet cauri sarakstiem izprintējot random teikumus
for n in range(1,11):
    print(n,reiss(reisa_numurs, reisa_galamerkis, reisa_laiks, reisa_cena) ) 
    
izvele = int(input("=> "))
if izvele in range(1,11):
    print("="*20)
    print("Sēdvietas izvēle: ")
    print("Pieejamas šādas sēdvietas: ")
else:
    print("Kļūda! Šāds reiss neeksistē! ")


print('Sēdvietas izvēle:\nPieejamas šādas sēdvietas:')
visas_sedvietas = ['A1','A2','A3','A4','A5','A6','A7','A8','A9','A10',
'B1','B2','B3','B4','B5','B6','B7','B8','B9','B10',
'C1','C2','C3','C4','C5','C6','C7','C8','C9','C10',
'D1','D2','D3','D4','D5','D6','D7','D8','D9','D10',
'E1','E2','E3','E4','E5','E6','E7','E8','E9','E10']

skaits_ko_iznem = random.randint(0,49)
for i in range(skaits_ko_iznem):
    kuru_sedvietu_izdzes = random.randint(0,len(visas_sedvietas)-1)
    visas_sedvietas.remove(visas_sedvietas[kuru_sedvietu_izdzes])

prieks_izdrukasanas = visas_sedvietas[0]
for i in range(1,len(visas_sedvietas)):
    prieks_izdrukasanas = prieks_izdrukasanas +' / '+ str(visas_sedvietas[i])
print(prieks_izdrukasanas)

izveleta_sedvieta = input('=> ')

while True:
    if izveleta_sedvieta not in visas_sedvietas:
        print('Kļūda! Sēdvieta ir aizņemta vai neeksistē!')
        izveleta_sedvieta = input('=> ')
    else:
        print('Sēdvieta rezervēta!')
        print('===================')
        break
