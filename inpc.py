def busca_inpc():
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from time import sleep

    # Initialize the browser
    driver = webdriver.Chrome()
    driver.get('https://www.elcontribuyente.mx/inpc/')
    driver.maximize_window()

    # Find the table and rows
    tabla = WebDriverWait(driver,55).until(
        EC.presence_of_element_located((By.XPATH, '//table[@class="tableizer-table"]/tbody[1]/tr[1]/td[2]'))
    )
    tabla = driver.find_element(By.XPATH, '//table[@class="tableizer-table"]/tbody[1]/tr[1]/td[2]')
    inpc_inicial = tabla.text
    
    tabla2 = WebDriverWait(driver,55).until(
        EC.presence_of_element_located((By.XPATH, '//table[@class="tableizer-table"]/tbody[1]/tr[1]/td[8]'))
    )
    tabla2 = driver.find_element(By.XPATH, '//table[@class="tableizer-table"]/tbody[1]/tr[1]/td[8]')
    inpc_final = tabla2.text
        
    print ("INPC INICIAL: ", inpc_inicial)
    print("INPC FINAL: ", inpc_final)

    return {
        'inpc1': inpc_inicial,
        'inpc2': inpc_final
    } 

results_inpc = busca_inpc()
inpc1 = results_inpc['inpc1']
inpc2 = results_inpc['inpc2']

# ***** Sending values to Database: *****
from DB_YTP import conector_DBYTP

connecting = conector_DBYTP.connect()
database = connecting[0]
cursor = connecting[1]

sql = "INSERT INTO inpc VALUES(null, %s, %s, NOW())"
value = (inpc1, inpc2)

cursor.execute(sql, value)

database.commit()