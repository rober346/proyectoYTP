def busca_inpc():
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from time import sleep

    # Inicializar el navegador
    driver = webdriver.Chrome()
    driver.get('https://www.elcontribuyente.mx/inpc/')
    driver.maximize_window()

    # Encontrar la tabla por su ID (reemplaza 'miTabla' con el ID de tu tabla)
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

    ''' +
    # Obtener la primera fila de la tabla
    primera_fila = tabla.find_element(By.TAG_NAME, 'tr')
    print(primera_fila)
    print("-------------")

    # Obtener las celdas de la primera fila
    celdas = primera_fila.find_elements(By.TAG_NAME, 'td')
    print(celdas)

    # Obtener los datos de la primera y sexta columna
    primer_dato = celdas[1].text  # Datos de la primera columna
    sexto_dato = celdas[6].text   # Datos de la sexta columna

    # Imprimir los datos
    print("Datos de la primera columna:", primer_dato)
    print("Datos de la sexta columna:", sexto_dato)
    '''



'''
def busca_inpc():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from time import sleep

    # Inicializar el navegador
    driver = webdriver.Chrome()
    driver.get('https://www.elcontribuyente.mx/inpc/')

    driver.execute_script("window.scrollTo(0,300)")
    sleep(2)

    # Encontrar la tabla por su ID (reemplaza 'miTabla' con el ID de tu tabla)
    tabla = driver.find_element(By.ID, 'tableizer-table')

    # Obtener la primera fila de la tabla
    primera_fila = tabla.find_element(By.TAG_NAME, 'tr')
    print(primera_fila)
    print("-------------")

    # Obtener las celdas de la primera fila
    celdas = primera_fila.find_elements(By.TAG_NAME, 'td')
    print(celdas)

    # Obtener los datos de la primera y sexta columna
    primer_dato = celdas[1].text  # Datos de la primera columna
    sexto_dato = celdas[6].text   # Datos de la sexta columna

    # Imprimir los datos
    print("Datos de la primera columna:", primer_dato)
    print("Datos de la sexta columna:", sexto_dato)
'''
