#Importēts random
import random


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
    

