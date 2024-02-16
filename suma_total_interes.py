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
           

def send_pagos_database():
    import csv
    from datetime import datetime
    from DB_YTP import conector_DBYTP
    import mysql.connector

    connecting = conector_DBYTP.connect()
    database = connecting[0]
    cursor = connecting[1]

    # Diccionario para almacenar la suma de intereses por fecha
    suma_intereses_por_fecha = {}

    for i in range(0, 21):
        numero_formateado = str(i).zfill(1)
        csvfile = open(f'C:/Users/Tere Parra/Downloads/pago/Mis movimientos Enero - 2024 ({numero_formateado}).csv')
        file = csv.reader(csvfile, delimiter=',')

        next(file, None)
        for f in file:
            print(f[4])

            intereses = float(f[4])
            date_hour_str = (f[2])
            format_date_hour = "%d/%m/%Y %I:%M %p"

            # Convert the string to an object of type date and time
            date_hour_obj = datetime.strptime(date_hour_str, format_date_hour)

            # Obtener solo la parte de la fecha en formato año-mes-día
            date_only = date_hour_obj.strftime("%Y-%m-%d")

            # Verificar si ya hemos visto esta fecha antes (para sumar varias cantidades de intereses del mismo dia)
            if date_only in suma_intereses_por_fecha:
                # Si sí, agregar los intereses al total existente
                suma_intereses_por_fecha[date_only] += intereses
            else:
                # Si no, inicializar la suma para esta fecha
                suma_intereses_por_fecha[date_only] = intereses
            
            
            print(date_only)

    # Insertar las sumas totales en la base de datos
    for fecha, suma_intereses in suma_intereses_por_fecha.items():
        sql = "UPDATE isr_semestral SET interes_nominal = %s WHERE fecha = %s"
        values = (suma_intereses, fecha)
        cursor.execute(sql, values)

    database.commit()

# lecturacsv_pagos()
send_pagos_database()



'''
def send_retiros_database():
    import csv
    from datetime import datetime
    from DB_YTP import conector_DBYTP
    import mysql.connector

    connecting = conector_DBYTP.connect()
    database = connecting[0]
    cursor = connecting[1]

    for i in range(0,21):
        numero_formateado = str(i).zfill(1)
        csvfile = open(f'C:/Users/Tere Parra/Downloads/pago/Mis movimientos Enero - 2024 ({numero_formateado}).csv')
        file = csv.reader(csvfile, delimiter=',')

        next(file, None)
        for f in file:
            print(f[4])

            intereses = float(f[4])
            date_hour_str = (f[2])
            format_date_hour = "%d/%m/%Y %I:%M %p"

            # Convert the string to an object of type date and time
            date_hour_obj = datetime.strptime(date_hour_str, format_date_hour)

            # Get only the part of the date in year-month-day format
            date_only = date_hour_obj.strftime("%Y-%m-%d")

            sql = "UPDATE isr_semestral SET interes_nominal = %s WHERE fecha = %s"
            values = (intereses, date_only)

            cursor.execute(sql, values)

            print(date_only)
    
        database.commit()


# lecturacsv_pagos()
send_retiros_database()
'''