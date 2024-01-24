def lecturacsv_pagos():
    import csv
    suma_total_acumulado = 0
    for i in range(0,21):
        numero_formateado = str(i).zfill(1)
        csvfile = open(f'C:/Users/Tere Parra/Downloads/pago/Mis movimientos Enero - 2024 ({numero_formateado}).csv')
        file = csv.reader(csvfile, delimiter=',')

        acumulado = 0
        
        next(file, None)
        for f in file:
            print(f[4])
            d = float(f[4])
            acumulado += d
        
        print("Acumulado de Comisiones: ", acumulado)
        suma_total_acumulado += acumulado
    
    print("----------------------------------------")
    print(f"Suma total acumulada de Interes Nominal: {suma_total_acumulado}")
    print("----------------------------------------")
           

lecturacsv_pagos()
