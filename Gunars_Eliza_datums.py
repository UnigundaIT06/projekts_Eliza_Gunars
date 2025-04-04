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