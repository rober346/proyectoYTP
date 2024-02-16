from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from time import sleep
import datetime
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

opts = Options()
# Determine which is the argument when instantiating options
opts.add_experimental_option("detach", True)

#driver = webdriver.Chrome("./chromedriver.exe", chrome_options=opts)
driver = webdriver.Chrome()
driver.maximize_window()

def get_info_date(fecha_inicial, fecha_final):   

    driver.get('https://app.yotepresto.com/sign-in/')

    user = open("user.txt").readline().strip()
    password = open("password.txt").readline().strip()

    input_user = WebDriverWait(driver,20).until(
        EC.presence_of_element_located((By.XPATH, '//input[@name="email"]'))
    )
    input_user = driver.find_element(By.XPATH, '//input[@name="email"]')

    # Enter the username:
    input_user.send_keys(user)

    # Click button "siguiente" from username:
    boton = driver.find_element(By.XPATH, '//button[@data-testid="email-submit"]')
    boton.click()

    input_pass = WebDriverWait(driver,20).until(
        EC.presence_of_element_located((By.XPATH, '//input[@name="password"]'))
    )
    input_pass = driver.find_element(By.XPATH, '//input[@name="password"]')

    # Enter the password:
    input_pass.send_keys(password)

    # Click button "siguiente" from password
    boton = driver.find_element(By.XPATH, '//button[@data-testid="password-submit"]')
    boton.click()  

    boton = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, '//div[@data-testid="Mis movimientos"]'))
    )
    boton = driver.find_element(By.XPATH, '//div[@data-testid="Mis movimientos"]')
    boton.click()

    # ----------------------------------------------------------------------------------------------------
    # Select Pago (Intereses Nominal)
    # ----------------------------------------------------------------------------------------------------

    boton = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, '//option[@value="Pago"]'))
    )
    boton = driver.find_element(By.XPATH, '//option[@value="Pago"]')
    boton.click()

    # Enter initial date:
    input_fecha_inicio = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//input[@name="min_date"]'))
    )
    input_fecha_inicio = driver.find_element(By.XPATH, '//input[@name="min_date"]')
    
    sleep(2)
    input_fecha_inicio.send_keys(Keys.CONTROL + "a")
    input_fecha_inicio.send_keys(Keys.BACK_SPACE)
    sleep(1)
    input_fecha_inicio.send_keys(fecha_inicial)
    sleep(2)    

    # Enter end date:
    input_fecha_final = WebDriverWait(driver,20).until(
        EC.presence_of_element_located((By.XPATH, '//input[@name="max_date"]'))
    )
    input_fecha_final = driver.find_element(By.XPATH, '//input[@name="max_date"]')
    
    sleep(2)
    input_fecha_final.send_keys(Keys.CONTROL + "a")
    input_fecha_final.send_keys(Keys.BACK_SPACE)
    sleep(1)
    input_fecha_final.send_keys(fecha_final)
    sleep(2)

    # ---- SIMULATION CLICK ON EMPTY AREA TO CONTINUE ---------------

    # Element representing the "empty" area of the page:
    area_vacia = driver.find_element(By.XPATH, '//p[@class="titleFilter"]')
    # Instance of ActionChains
    actions = ActionChains(driver)
    # Simulates a click in the empty area
    actions.click(area_vacia).perform()
    # -------------------------------------------------------------------
    
    # click on the blue filter button 
    boton_filtrar = WebDriverWait(driver,20).until(
        EC.presence_of_element_located((By.XPATH, '//button[@type="submit"][contains(.,"Filtrar")]'))
    )
    boton_filtrar = driver.find_element(By.XPATH, '//button[@type="submit"][contains(.,"Filtrar")]')
    boton_filtrar.click()

    # Waiting for the element to be present in the DOM

    elemento_intereses = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '(//div[contains(@class,"data")])[3]'))
    )
    elemento_intereses = driver.find_element(By.XPATH, '(//div[contains(@class,"data")])[3]')
    
    intereses_valor = float(elemento_intereses.text.replace('$', '').replace(',', '').strip())
    sleep(3)

    # click on the button header
    boton_filtrar = WebDriverWait(driver,20).until(
        EC.presence_of_element_located((By.XPATH, '(//button[@data-testid="header-button"])[2]'))
    )
    boton_filtrar = driver.find_element(By.XPATH, '(//button[@data-testid="header-button"])[2]')
    boton_filtrar.click()

    # click on the button "cerrar sesion"
    boton_filtrar = WebDriverWait(driver,20).until(
        EC.presence_of_element_located((By.XPATH, '//button[@class="end__session"][contains(.,"Cerrar sesión")]'))
    )
    boton_filtrar = driver.find_element(By.XPATH, '//button[@class="end__session"][contains(.,"Cerrar sesión")]')
    boton_filtrar.click()  

    return intereses_valor


dates_per_month = [
    ("01/01/2023", "01/31/2023"),
    ("02/01/2023", "02/28/2023"),
    ("03/01/2023", "03/31/2023"),
    ("04/01/2023", "04/30/2023"),
    ("05/01/2023", "05/31/2023"),
    ("06/01/2023", "06/30/2023"),
]

lista_intereses = []
for fecha_inicial, fecha_final in dates_per_month:
    # Obtener la información para el mes actual
    informacion_mes = get_info_date(fecha_inicial, fecha_final)
    
    # Agregar la información a la lista
    lista_intereses.append(informacion_mes)
    
    print(lista_intereses)
    
print(lista_intereses)


sleep(5)

