import mysql.connector
from decimal import Decimal

database = mysql.connector.connect(
    host="192.168.52.247",
    user="root", 
    passwd=open("password_mysql.txt").readline().strip(), 
    database="yotepresto", 
    port=33061
)

cursor = database.cursor()

# ----- SUMA TOTAL INTERES NOMINAL -----------------
sql = 'SELECT interes_nominal FROM isr_semestral'
cursor.execute(sql)
results = cursor.fetchall()

total_sum_interes = 0
# print(results)
for tupla in results:
    valor = tupla[0]  # Extraer el valor de la tupla
    if valor is not None:
        total_sum_interes += valor

print(f"Suma total de interes nominal: {total_sum_interes}")


# ----- SUMA TOTAL ABONOS -----------------
sql = 'SELECT abono FROM isr_semestral'
cursor.execute(sql)
results = cursor.fetchall()

total_sum_abonos = 0
for tupla in results:
    valor = tupla[0]  
    if valor is not None:
        total_sum_abonos += valor

print(f"Suma total de abonos: {total_sum_abonos}")


# ----- SUMA TOTAL COMISIONES -----------------
sql = 'SELECT comision FROM isr_semestral'
cursor.execute(sql)
results = cursor.fetchall()

total_sum_comisiones = 0
for tupla in results:
    valor = tupla[0]  
    if valor is not None:
        total_sum_comisiones += valor

print(f"Suma total comisiones: {total_sum_comisiones}")


# ----- SUMA TOTAL RETIROS -----------------
sql = 'SELECT retiro FROM isr_semestral'
cursor.execute(sql)
results = cursor.fetchall()

total_sum_retiros = 0
for tupla in results:
    valor = tupla[0]  
    if valor is not None:
        total_sum_retiros += valor

print(f"Suma total de retiros: {total_sum_retiros}")



# ----- SALDO PROMEDIO DIARIO -----------------
sql = 'SELECT suma_diaria FROM isr_semestral'
cursor.execute(sql)
results = cursor.fetchall()

total_sum_saldos = 0
num_tuplas = len(results) 

for tupla in results:
    valor = tupla[0]  
    if valor is not None:
        total_sum_saldos += valor

saldo_promedio = total_sum_saldos / num_tuplas if num_tuplas > 0 else 0
average_balance = Decimal(saldo_promedio)
saldo_promedio_diario = round(average_balance, 3)

print(f"Saldo promedio diario: {saldo_promedio_diario}")


# ----- INPC -----------------
sql = 'SELECT inpc_inicial FROM inpc'
cursor.execute(sql)
results = cursor.fetchall()

value_init = 0
for tupla in results:
    value_init = tupla[0]  

print(f"\nEl INPC de inicio de inversion es: {value_init}")


sql = 'SELECT inpc_final FROM inpc'
cursor.execute(sql)
results = cursor.fetchall()

value_end = 0
for tupla in results:
    value_end = tupla[0]  

print(f"El INPC de final de inversion es: {value_end}")


# Factor de inflacion
inflation_factor = ((value_end / value_init) - 1)
inflation_factor_round = round(inflation_factor, 4)
print(f"\nEl factor de inflacion es: {inflation_factor_round}")


# Ajuste por Inflacion = Factor de Inflacion * saldo promedio diario
inflation_adjustment = round((inflation_factor_round * saldo_promedio_diario), 3)

print(f"Ajuste por inflacion: {inflation_adjustment}")

# Interes Real
interes_real = total_sum_interes - inflation_adjustment
print(f"Interes Real: {interes_real}")

# CALCULO ISR SEMESTRAL

# Limite inferior = obtener del diario oficial (en pagina del sat) = (=0.01) -- pag 15 de RESOLUCIÓN Miscelánea Fiscal para 2023
lower_limit = Decimal(.01)

# Excedente sobre limite inferior = interes real - limite inferior
excess_lower_limit = round(interes_real - lower_limit, 3)
print(f"\nExcedente sobre limite inferior: {excess_lower_limit}")

# Impuesto Marginal = excedente limite inferior * Tasa
tasa = Decimal(1.92)
marginal_tax = round(excess_lower_limit * tasa, 3)
print(f"Impuesto Marginal: {marginal_tax}")

# Cuota fija = obtener del diario oficial (en pagina del sat) = (0.00)
fixed_fee = Decimal(0.00)
print(f"Cuota Fija: {fixed_fee}")

# ISR a cargo = Impuesto Marginal + cuota fija
isr_paid = marginal_tax + fixed_fee
print(f"ISR a cargo: {isr_paid}")


database.close()


