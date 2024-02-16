
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
#  Determine which is the argument when instantiating options
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

#driver.get('https://investor.yotepresto.com/dashboard')
# -------------------------------------------------------------------

boton = WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.XPATH, '//div[@data-testid="Mis movimientos"]'))
)
boton = driver.find_element(By.XPATH, '//div[@data-testid="Mis movimientos"]')
boton.click()


# Get dates for the first semester:
fecha_completa = datetime.date.today()
fecha_personalizada_año = fecha_completa.strftime("%Y")
fecha_inicial = "01/01/2023"
fecha_final = "06/30/2023"


# Enter initial date:
input_fecha_inicio = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, '//input[@name="min_date"]'))
)
input_fecha_inicio = driver.find_element(By.XPATH, '//input[@name="min_date"]')
input_fecha_inicio.click()
input_fecha_inicio.send_keys(fecha_inicial)


# Enter end date:
input_fecha_final = WebDriverWait(driver,20).until(
    EC.presence_of_element_located((By.XPATH, '//input[@name="max_date"]'))
)
input_fecha_final = driver.find_element(By.XPATH, '//input[@name="max_date"]')
input_fecha_final.click()
input_fecha_final.send_keys(fecha_final)


# ---- SIMULATION CLICK ON EMPTY AREA TO CONTINUE ---------------

# Element representing the "empty" area of the page:
area_vacia = driver.find_element(By.XPATH, '//p[@class="titleFilter"]')
# Instance of ActionChains
actions = ActionChains(driver)
# Simulates a click in the empty area
actions.click(area_vacia).perform()
# -------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------
# Comision (Importe)
# ----------------------------------------------------------------------------------------------------

# Select Comision
boton = WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.XPATH, '//option[@value="Comisión"]'))
)
boton = driver.find_element(By.XPATH, '//option[@value="Comisión"]')
boton.click()

# click on the blue filter button 
boton_filtrar = WebDriverWait(driver,20).until(
    EC.presence_of_element_located((By.XPATH, '//button[@type="submit"][contains(.,"Filtrar")]'))
)
boton_filtrar = driver.find_element(By.XPATH, '//button[@type="submit"][contains(.,"Filtrar")]')
boton_filtrar.click()


# Identify the last page button
boton_siguiente = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, '//div[contains(text(), ">>")]')))
boton_siguiente.click()
sleep(10)

# Locates the parent class
pagination_list = WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "paginationList"))
)

# Finds the number of children and stores in variable
num_children = len(pagination_list.find_elements(By.XPATH, "./*"))
children = pagination_list.find_elements(By.XPATH, "./*")
print(num_children)

# Prints the last position of the children
print(children[-1].text)
num = children[-1].text


# Scroll through all tabs:

for i in range (1, int(num)):
    
    # Extract data from the page, downloading excel
    boton_siguiente_archivo = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="Layer_1"]')))
    boton_siguiente_archivo.click()
    

    try:
        # click next button (reverse)
        boton_siguiente = WebDriverWait(driver, 6).until(
                    EC.visibility_of_element_located((By.XPATH, '(//div[contains(.,"<")])[10]')))
        boton_siguiente.click()
        sleep(2)

    except Exception as e:
        print(f"Caught an exception of type: {type(e)}")
        # If 'Next' button not found, exit the loop
        break


# ----------------------------------------------------------------------------------------------------
# Select Pago (Intereses Nominal)
# ----------------------------------------------------------------------------------------------------

boton = WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.XPATH, '//option[@value="Pago"]'))
)
boton = driver.find_element(By.XPATH, '//option[@value="Pago"]')
boton.click()

# click on the blue filter button 
boton_filtrar = WebDriverWait(driver,20).until(
    EC.presence_of_element_located((By.XPATH, '//button[@type="submit"][contains(.,"Filtrar")]'))
)
boton_filtrar = driver.find_element(By.XPATH, '//button[@type="submit"][contains(.,"Filtrar")]')
boton_filtrar.click()

# Waiting for the element to be present in the DOM
elemento_intereses = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//div[@class="info-widget__category"][contains(text(),"Intereses")]/following-sibling::div[@class="info-widget__data"]'))
)

# Get the text of the element and save it in a list
lista_intereses = [elemento_intereses.text]

# Print the list
print(lista_intereses)
# ----------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------
# Retiro
# ----------------------------------------------------------------------------------------------------
# Select Retiro
boton = WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.XPATH, '//option[@value="Retiro"]'))
)
boton = driver.find_element(By.XPATH, '//option[@value="Retiro"]')
boton.click()


# click on the blue filter button
boton_filtrar = WebDriverWait(driver,20).until(
    EC.presence_of_element_located((By.XPATH, '//button[@type="submit"][contains(.,"Filtrar")]'))
)
boton_filtrar = driver.find_element(By.XPATH, '//button[@type="submit"][contains(.,"Filtrar")]')
boton_filtrar.click()


# Click on the download excel button
boton_descargar = WebDriverWait(driver,20).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="Layer_1"]'))
)
#boton_descargar = driver.find_element(By.XPATH, '//*[@id="Layer_1"]')
boton_descargar.click()
sleep(2)

# ----------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------
# FONDOS AGREGADOS (Abono)
# ----------------------------------------------------------------------------------------------------
fecha_inicial_abono = "01/01/2020"
fecha_final_abono = "06/30/2023"

# Enter initial date:
input_fecha_inicio = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, '//input[@name="min_date"]'))
)
input_fecha_inicio = driver.find_element(By.XPATH, '//input[@name="min_date"]')

#input_fecha_inicio.clear()
#input_fecha_inicio.click()
sleep(3)
input_fecha_inicio.send_keys(Keys.CONTROL + "a")
input_fecha_inicio.send_keys(Keys.BACK_SPACE)
sleep(2)
input_fecha_inicio.send_keys(fecha_inicial_abono)
sleep(3)

# Enter end date:
input_fecha_final = WebDriverWait(driver,20).until(
    EC.presence_of_element_located((By.XPATH, '//input[@name="max_date"]'))
)
input_fecha_final = driver.find_element(By.XPATH, '//input[@name="max_date"]')

#input_fecha_final.clear()
#input_fecha_final.click()
sleep(3)
input_fecha_final.send_keys(Keys.CONTROL + "a")
input_fecha_final.send_keys(Keys.BACK_SPACE)
sleep(2)
input_fecha_final.send_keys(fecha_final_abono)
sleep(3)

# Select Fondos Agregados
boton = WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.XPATH, '//option[@value="Abono"]'))
)
boton = driver.find_element(By.XPATH, '//option[@value="Abono"]')
boton.click()

# ---- SIMULATION CLICK ON EMPTY AREA TO CONTINUE ---------------
# Element representing the "empty" area of the page:
area_vacia = driver.find_element(By.XPATH, '//p[@class="titleFilter"]')
# Instance de ActionChains:
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


# Click on the download excel button
botoncsv = WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="Layer_1"]'))
)
#botoncsv = driver.find_element(By.XPATH, '//*[@id="Layer_1"]')
botoncsv.click()

# busca_inpc()

sleep(10)

