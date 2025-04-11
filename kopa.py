import random
print("Labdien, laipni lūgti lidostas lidO2 programmā.")
class Dati:    

    def datums():
        import datetime
        datums_ar_laiku = datetime.datetime.now()
        datums = datums_ar_laiku.strftime('%d-%m-%Y')

        from datetime import datetime

        datetime_datums = datetime.strptime(datums,'%d-%m-%Y')
        izveletais_datums = datetime.strptime(input('Ieraksti datumu kurā gribi lidot dd-mm-gggg: '),'%d-%m-%Y')
        while True:
            if izveletais_datums <= datetime_datums:
                izveletais_datums = datetime.strptime(input('Kļūda! Datums nedrīkst būt agrāks par rītdienu: '),'%d-%m-%Y')
            else:
                print('===================')
                datums1,nevajadzigs = str(izveletais_datums).split(' ')
                return datums1                  


    def reisa_izvele():
        saraksts = []
        #4 saraksti ar vajadzīgo informāciju sastāvā
        reisa_numurs = [234, 156, 780, 356, 987, 404, 342, 764, 900, 135]
        reisa_galamerkis = ["Vācija", "Francija", "Nīderlande", "Polija", "Spānija", "Itālija", "Portugāle", "Grieķija", "Dānija", "Zviedrija"]
        reisa_laiks = ["10-10", "18-35", "09-15", "05-30", "12-00", "15-00", "23-30", "22-10", "13-00", "05-20"]
        reisa_cena = ["47 EUR", "150 EUR", "3734 EUR", "10000 EUR", "265 EUR", "354 EUR", "1200 EUR", "570 EUR", "988 EUR", "155 EUR"]
        print("="*20)
        print("Reisa izvēle: ")
        #For cikls, kas iziet cauri sarakstiem izprintējot random teikumus
        for n in range(1,11):
            saraksts.append(reiss(reisa_numurs, reisa_galamerkis, reisa_laiks, reisa_cena))
            print(n,saraksts[n-1]) 
        while True:
            try:    
                while True:
                    izvele = int(input("=> "))
                    if izvele in range(1,11):
                        print("="*20)
                        print("Sēdvietas izvēle: ")
                        print("Pieejamas šādas sēdvietas: ")
                        return saraksts[izvele-1]
                    else:
                        print("Kļūda! Šāds reiss neeksistē! ")
            except ValueError:
                print('Skaitlim jābūt no 1 līdz 10!!')

   

    def sedvietas():
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
                return izveleta_sedvieta

    


    #KLASE reiss?
def reiss(reisa_numurs, reisa_galamerkis, reisa_laiks, reisa_cena):
    reiss = random.choice(reisa_numurs)
    galamerkis = random.choice(reisa_galamerkis)
    laiks = random.choice(reisa_laiks)
    cena = random.choice(reisa_cena)
    return f"{reiss} - {galamerkis} - {laiks} - {cena}"




class Saglaba:
    def __init__(self,datums,reiss,sedvieta):
        self.datums = datums
        self.reiss = reiss
        self.sedvieta = sedvieta
    
    def saglabat(self,dati):
        dati1,nummurs = dati.split('+++')
        nosaukums = f'Bilete_{nummurs}'
        with open(nosaukums+'.txt',)as file:

    def biletes_parbaude(self):
        print('Vai šī ir jūsu biļete? (J/N)')
        print('Datums - Galapunkts - Laiks - Reiss - Sēdvieta - Cena')
        nummurs,valsts,laiks,cena = self.reiss.split(' - ')
        dati = f'{self.datums} - {valsts} - {laiks} - {nummurs} - {self.sedvieta} - {cena}'
        print(dati)
        while True:
            izvele = input('=> ')
            if izvele == 'J' or izvele == 'j':
                return f'{dati}+++{nummurs}' 
            elif izvele == 'N' or izvele == 'n':
                exit('Atvainojos par traucēšanu bet viss jāsāk no sākuma!!')
            else:
                print('jūs ievadijāt nepareizi ievadiet vēlreiz (J/N)')



#Vai šī ir jūsu biļete? (J/N)
#Datums - Galapunkts - Laiks - Reiss - Sēdvieta - Cena
#13-04-2025 - Vācija - 12:00 - 156 - B4 - 150 EUR
#=> J
#Biļete ir saglabāta failā bilete_156 un aizsūtīta uz jūsu e-pastu!


objekts2 = Saglaba(Dati.datums(),Dati.reisa_izvele(),Dati.sedvietas())
objekts2.saglabat(objekts2.biletes_parbaude())