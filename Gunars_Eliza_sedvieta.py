import random

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




#Sēdvietas izvēle:
#Pieejamas šādas sēdvietas:
#B2 / B4 / A9 / C7 / E3
#=> F1
#Kļūda! Sēdvieta ir aizņemta vai neeksistē!
#=> B4
#Sēdvieta rezervēta!
#===================