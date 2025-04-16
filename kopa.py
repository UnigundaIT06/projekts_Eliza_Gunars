import random #lai vēlāk varētu izdzēst sēdvietas
print('\n')
print("Labdien, laipni lūgti lidostas lidO2 programmā. ")
class Dati: #iegūst visus vajadzīgos datus

    def datums(): #iegūst datumu
        import datetime
        datums_ar_laiku = datetime.datetime.now() #iegūst šodienu un laiku
        datums = datums_ar_laiku.strftime('%d-%m-%Y')
        from datetime import datetime
        datetime_datums = datetime.strptime(datums,'%d-%m-%Y')#noformē datumu
        izveletais_datums = datetime.strptime(input('Ieraksti datumu kurā gribi lidot dd-mm-gggg: '),'%d-%m-%Y')
        while True: #Ja datums neder
            if izveletais_datums <= datetime_datums:
                izveletais_datums = datetime.strptime(input('Kļūda! Datums nedrīkst būt agrāks par rītdienu: '),'%d-%m-%Y')
            else:
                print('====================')
                datums1,laiks = str(izveletais_datums).split(' ') #atdala laiku
                return datums1  #atgriež izvēlēto datumu          


    def reisa_izvele():
        saraksts = []
        #4 saraksti ar vajadzīgo informāciju sastāvā
        reisa_numurs = [234, 156, 780, 356, 987, 404, 342, 764, 900, 135]
        reisa_galamerkis = ["Vācija", "Francija", "Nīderlande", "Polija", "Spānija", "Itālija", "Portugāle", "Grieķija", "Dānija", "Zviedrija"]
        reisa_laiks = ["10-10", "18-35", "09-15", "05-30", "12-00", "15-00", "23-30", "22-10", "13-00", "05-20"]
        ieteicamais_laiks = ["08-10", "16-35", "07-15", "03-30", "10-00", "13-00", "21-30", "20-10", "11-00", "03-20"]
        reisa_cena = ["47 EUR", "150 EUR", "3734 EUR", "10000 EUR", "265 EUR", "354 EUR", "1200 EUR", "570 EUR", "988 EUR", "155 EUR"]
        print("Reisa izvēle: ")
        #For cikls, kas iziet cauri sarakstiem izprintējot random teikumus
        for n in range(1,11):
            saraksts.append(reiss(reisa_numurs, reisa_galamerkis, reisa_laiks, reisa_cena,ieteicamais_laiks)) #Lai vēlāk var izēlēties reisu
            bilete, ieteicamais_laiks_nesvarigs = saraksts[n-1].split('+++')#noņem ieteicamo ierašanās laiku
            print(n,bilete) 
        while True:
            try:    
                while True: #Reisa izvēle
                    izvele = int(input("=> "))
                    if izvele in range(1,11): #Ja izvēle der 
                        print("====================")
                        return saraksts[izvele-1]#tad atgriež
                    else:
                        print("Kļūda! Šāds reiss neeksistē! ") #Ja neder tad jāireraksta vēlreiz
            except ValueError:
                print('Skaitlim jābūt no 1 līdz 10!!')

   

    def sedvietas():
        print('Sēdvietas izvēle:\nPieejamas šādas sēdvietas:')
        visas_sedvietas = ['A1','A2','A3','A4','A5','A6','A7','A8','A9','A10',#Visas iespējamās sēdvietas
        'B1','B2','B3','B4','B5','B6','B7','B8','B9','B10',
        'C1','C2','C3','C4','C5','C6','C7','C8','C9','C10',
        'D1','D2','D3','D4','D5','D6','D7','D8','D9','D10',
        'E1','E2','E3','E4','E5','E6','E7','E8','E9','E10']

        skaits_ko_iznem = random.randint(0,49) #nejauši izvēlas kādu skaitu sēdvietas izņems
        for i in range(skaits_ko_iznem):
            kuru_sedvietu_izdzes = random.randint(0,len(visas_sedvietas)-1) #izvēlas nejaušu sēdvietu
            visas_sedvietas.remove(visas_sedvietas[kuru_sedvietu_izdzes])#izņem izvēlēto sēdvietu

        prieks_izdrukasanas = visas_sedvietas[0]
        for i in range(1,len(visas_sedvietas)):
            prieks_izdrukasanas = prieks_izdrukasanas +' / '+ str(visas_sedvietas[i])
        print(prieks_izdrukasanas)

        izveleta_sedvieta = input('=> ')

        while True:
            if izveleta_sedvieta not in visas_sedvietas:  #Nosaka sēdvietas eksistēšanu, aizņemtību vai rezervāciju
                print('Kļūda! Sēdvieta ir aizņemta vai neeksistē!')
                izveleta_sedvieta = input('=> ')
            else:
                print('Sēdvieta rezervēta!')
                print('====================')
                return izveleta_sedvieta


def reiss(reisa_numurs, reisa_galamerkis, reisa_laiks, reisa_cena,ieteicamais_reisa_laiks):#nejauši izvēlas no iepriiekšējiem sarakstiem
    reiss = random.choice(reisa_numurs)
    galamerkis = random.choice(reisa_galamerkis)
    laikscipars = random.choice(range(0,10))
    laiks = reisa_laiks[laikscipars]
    ieteicamais_laiks = ieteicamais_reisa_laiks[laikscipars]
    cena = random.choice(reisa_cena)
    return f"{reiss} - {galamerkis} - {laiks} - {cena}+++{ieteicamais_laiks}"


class Saglaba:#Tiek veikta datu saglabāšana
    def __init__(self,datums,reiss,sedvieta):
        self.datums = datums
        self.reiss = reiss
        self.sedvieta = sedvieta
    
    def saglabat(self,dati):
        dati1,nummurs,ieteicamais_laiks = dati.split('+++')
        nosaukums = f'Bilete_{nummurs}'
        with open(nosaukums+'.txt','a',encoding='utf8')as file:
            file.write('Datums - Galapunkts - Laiks - Reiss - Sēdvieta - Cena - ieteicamais ierašanās laiks\n')
            file.write(f'{dati1} - {ieteicamais_laiks}\n')#Izvēlētā biļete tiek ierakstīta failā
            print(f'Biļete ir saglabāta failā {nosaukums} un aizsūtīta uz jūsu e-pastu!')
            print('====================')
            exit("Paldies! Par lidojuma rezervēšanu!")

    def biletes_parbaude(self):
        print('Vai šī ir jūsu biļete? (J/N)')
        print('Datums - Galapunkts - Laiks - Reiss - Sēdvieta - Cena')
        nummurs,valsts,laiks,cena = self.reiss.split(' - ')
        cena,ieteicamais_laiks = cena.split('+++')
        dati = f'{self.datums} - {valsts} - {laiks} - {nummurs} - {self.sedvieta} - {cena}'
        print(dati)
        while True:
            izvele = input('=> ')#Lietotājs izvēlas vai biļete viņam der vai neder
            if izvele == 'J' or izvele == 'j':
                return f'{dati}+++{nummurs}+++{ieteicamais_laiks}' 
            elif izvele == 'N' or izvele == 'n':
                print('Atvainojos par traucēšanu bet viss jāsāk no sākuma!!')
                print('====================')
                break
            else:
                print('jūs ievadijāt nepareizi ievadiet vēlreiz (J/N)')
        return ''
        

while True:
    bilete = Saglaba(Dati.datums(),Dati.reisa_izvele(),Dati.sedvietas())
    dati = bilete.biletes_parbaude()
    if dati == '':
        print()
    else:
        bilete.saglabat(dati)
     #Dati tiek saglabāti failā 
