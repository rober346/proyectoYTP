def lecturacsv():
    import csv
    suma_total_acumulado = 0
    for i in range(0,21):
        numero_formateado = str(i).zfill(1)
        csvfile = open(f'C:/Users/Tere Parra/Downloads/comision/Mis movimientos Enero - 2024 ({numero_formateado}).csv')
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
    print(f"Suma total acumulada de Comisiones: {suma_total_acumulado}")
    print("----------------------------------------")
           

def send_comisiones_database():
    import csv
    from datetime import datetime
    from DB_YTP import conector_DBYTP
    import mysql.connector

    connecting = conector_DBYTP.connect()
    database = connecting[0]
    cursor = connecting[1]

    # Dictionary for storing the sum of commissions by date
    suma_comisiones_por_fecha = {}

    for i in range(0, 21):
        numero_formateado = str(i).zfill(1)
        csvfile = open(f'C:/Users/Tere Parra/Downloads/comision/Mis movimientos Enero - 2024 ({numero_formateado}).csv')
        file = csv.reader(csvfile, delimiter=',')

        next(file, None)
        for f in file:
            print(f[4])

            comisiones = float(f[4])
            date_hour_str = (f[2])
            format_date_hour = "%d/%m/%Y %I:%M %p"

            # Convert the string to an object of type date and time
            date_hour_obj = datetime.strptime(date_hour_str, format_date_hour)

            # Get only the part of the date in year-month-day format
            date_only = date_hour_obj.strftime("%Y-%m-%d")

            # Check if we have already seen this date before (to add up several commission amounts for the same day).
            if date_only in suma_comisiones_por_fecha:
                # add interes to total
                suma_comisiones_por_fecha[date_only] += comisiones
            else:
                # init the sum to this date
                suma_comisiones_por_fecha[date_only] = comisiones

            print(date_only)

    # Insert sums in database
    for fecha, suma_comisiones in suma_comisiones_por_fecha.items():
        sql = "UPDATE isr_semestral SET comision = %s WHERE fecha = %s"
        values = (suma_comisiones, fecha)
        cursor.execute(sql, values)

    database.commit()

# lecturacsv()
send_comisiones_database()
