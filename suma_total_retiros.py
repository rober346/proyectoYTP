def lecturacsv_retiros():
    import csv
    suma_total_acumulado = 0
    
    csvfile = open(f'C:/Users/Tere Parra/Downloads/retiro/Mis movimientos Enero - 2024.csv')
    file = csv.reader(csvfile, delimiter=',')

    acumulado = 0
    
    next(file, None)
    for f in file:
        print(f[4])
        d = float(f[4])
        acumulado += d
    
    print("Acumulado de Retiros: ", acumulado)
    suma_total_acumulado += acumulado
    
    print("----------------------------------------")
    print(f"Suma total acumulada de Retiros: {suma_total_acumulado}")
    print("----------------------------------------")
           

lecturacsv_retiros()
