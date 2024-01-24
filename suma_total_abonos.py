def lecturacsv_abonos():
    import csv
    suma_total_acumulado = 0
    
    csvfile = open(f'C:/Users/Tere Parra/Downloads/abono/Mis movimientos Enero - 2024.csv')
    file = csv.reader(csvfile, delimiter=',')

    acumulado = 0
    
    next(file, None)
    for f in file:
        print(f[4])
        d = float(f[4])
        acumulado += d
    
    print("Acumulado de Abonos: ", acumulado)
    suma_total_acumulado += acumulado
    
    print("----------------------------------------")
    print(f"Suma total acumulada de Abonos: {suma_total_acumulado}")
    print("----------------------------------------")
           

lecturacsv_abonos()
