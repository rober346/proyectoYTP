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
           

def send_retiros_database():
    import csv
    from datetime import datetime
    from DB_YTP import conector_DBYTP
    import mysql.connector

    connecting = conector_DBYTP.connect()
    database = connecting[0]
    cursor = connecting[1]
        
    csvfile = open(f'C:/Users/Tere Parra/Downloads/retiro/Mis movimientos Enero - 2024.csv')
    file = csv.reader(csvfile, delimiter=',')

        
    next(file, None)
    for f in file:
        print(f[4]) # retiros .....
        print(f[2]) # dates .....
        
        retiros = float(f[4])
        date_hour_str = (f[2])
        format_date_hour = "%d/%m/%Y %I:%M %p"

        # Convert the string to an object of type date and time
        date_hour_obj = datetime.strptime(date_hour_str, format_date_hour)

        # Get only the part of the date in year-month-day format
        date_only = date_hour_obj.strftime("%Y-%m-%d")

        sql = "UPDATE isr_semestral SET retiro = %s WHERE fecha = %s"
        values = (retiros, date_only)

        cursor.execute(sql, values)

        print(date_only)
    
    database.commit()


# lecturacsv_retiros()
send_retiros_database()

