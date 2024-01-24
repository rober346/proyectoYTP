
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
import datetime
from selenium.webdriver.common.action_chains import ActionChains
#from inpc import busca_inpc

opts = Options()
# Determinar cual es el argumento al instanciar options
opts.add_experimental_option("detach", True)

#driver = webdriver.Chrome("./chromedriver.exe", chrome_options=opts)
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://app.yotepresto.com/sign-in/')


# ------------------------ LOGIN ----------------------------------

user = open("user.txt").readline().strip()
password = open("password.txt").readline().strip()

input_user = WebDriverWait(driver,20).until(
    EC.presence_of_element_located((By.XPATH, '//input[@name="email"]'))
)
input_user = driver.find_element(By.XPATH, '//input[@name="email"]')
# Introduce el nombre de usuario:
input_user.send_keys(user)

# Click boton "siguiente" de usuario:
boton = driver.find_element(By.XPATH, '//button[@data-testid="email-submit"]')
boton.click()

input_pass = WebDriverWait(driver,20).until(
    EC.presence_of_element_located((By.XPATH, '//input[@name="password"]'))
)
input_pass = driver.find_element(By.XPATH, '//input[@name="password"]')

# Introduce el password:
input_pass.send_keys(password)

# Click boton "siguiente" del password
boton = driver.find_element(By.XPATH, '//button[@data-testid="password-submit"]')
boton.click()

#driver.get('https://investor.yotepresto.com/dashboard')
# -------------------------------------------------------------------


boton = WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.XPATH, '//div[@data-testid="Mis movimientos"]'))
)
boton = driver.find_element(By.XPATH, '//div[@data-testid="Mis movimientos"]')
boton.click()

# Obtener fechas del primer semestre:
fecha_completa = datetime.date.today()
fecha_personalizada_año = fecha_completa.strftime("%Y")
fecha_inicial = "01/01/2023"
fecha_final = "06/30/2023"


# Introducir fecha inicial:
input_fecha_inicio = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, '//input[@name="min_date"]'))
)
input_fecha_inicio = driver.find_element(By.XPATH, '//input[@name="min_date"]')
input_fecha_inicio.click()
input_fecha_inicio.send_keys(fecha_inicial)


# Introducir fecha final:
input_fecha_final = WebDriverWait(driver,20).until(
    EC.presence_of_element_located((By.XPATH, '//input[@name="max_date"]'))
)
input_fecha_final = driver.find_element(By.XPATH, '//input[@name="max_date"]')
input_fecha_final.click()
input_fecha_final.send_keys(fecha_final)


# ---- SIMULACION DE CLIC EN AREA VACÍA PARA CONTINUAR ---------------

# Elemento que representa el área "vacía" de la página
area_vacia = driver.find_element(By.XPATH, '//p[@class="titleFilter"]')
# Instancia de ActionChains
actions = ActionChains(driver)
# Simula un clic en el área vacía
actions.click(area_vacia).perform()
# -------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------
# Selecciona Pago (Intereses Nominal)
# ----------------------------------------------------------------------------------------------------

boton = WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.XPATH, '//option[@value="Pago"]'))
)
boton = driver.find_element(By.XPATH, '//option[@value="Pago"]')
boton.click()

# clic en boton azul de filtrar 
boton_filtrar = WebDriverWait(driver,20).until(
    EC.presence_of_element_located((By.XPATH, '//button[@type="submit"][contains(.,"Filtrar")]'))
)
boton_filtrar = driver.find_element(By.XPATH, '//button[@type="submit"][contains(.,"Filtrar")]')
boton_filtrar.click()

# ----------------------------------------

# Identificar el boton de ultima pagina
boton_siguiente = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, '//div[contains(text(), ">>")]')))
boton_siguiente.click()
sleep(10)

# localiza la clase padre
pagination_list = WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "paginationList"))
)

# Encuentra el numero de hijos y guarda en variable
num_children = len(pagination_list.find_elements(By.XPATH, "./*"))
children = pagination_list.find_elements(By.XPATH, "./*")
print(num_children)

# Imprime la ultima posicion de los hijos
print(children[-1].text)
num = children[-1].text


# Recorrer todas las pestañas:

for i in range (1, int(num)):
    
    # Extract data from the page, downloading excel
    boton_siguiente_archivo = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="Layer_1"]')))
    boton_siguiente_archivo.click()
    

    try:
        # clic boton siguiente (inverso)
        boton_siguiente = WebDriverWait(driver, 6).until(
                    EC.visibility_of_element_located((By.XPATH, '(//div[contains(.,"<")])[10]')))
        boton_siguiente.click()
        sleep(2)

    except Exception as e:
        print(f"Caught an exception of type: {type(e)}")
        # If 'Next' button not found, exit the loop
        break


# --------------------------------------------------
'''
# Esperar a que el elemento esté presente en el DOM
elemento_intereses = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//div[@class="info-widget__category"][contains(text(),"Intereses")]/following-sibling::div[@class="info-widget__data"]'))
)

# Obtener el texto del elemento y guardarlo en una lista
lista_intereses = [elemento_intereses.text]

# Imprimir la lista (puedes hacer lo que quieras con ella)
print(lista_intereses)
'''
# ----------------------------------------------------------------------------------------------------