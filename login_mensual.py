
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from time import sleep
import datetime

opts = Options()
# Determinar cual es el argumento al instanciar options
opts.add_experimental_option("detach", True)

#driver = webdriver.Chrome("./chromedriver.exe", chrome_options=opts)
driver = webdriver.Chrome()
driver.get('https://app.yotepresto.com/sign-in/')

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

boton = WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.XPATH, '//span[text()="Ajustes"]'))
)
boton = driver.find_element(By.XPATH, '//span[text()="Ajustes"]')
boton.click()


boton = WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.XPATH, '//a[text()="Estado de cuenta"]'))
)
boton = driver.find_element(By.XPATH, '//a[text()="Estado de cuenta"]')
boton.click()


boton = WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.XPATH, '//select[@data-testid="month-field-input"]'))
)
boton = driver.find_element(By.XPATH, '//select[@data-testid="month-field-input"]')
boton.click()

"""
boton = WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.XPATH, '//option[@value="2520389"]'))
)
boton = driver.find_element(By.XPATH, '//option[@value="2520389"]')
boton.click()
"""

fecha_completa = datetime.date.today()
fecha_personalizada_año = fecha_completa.strftime("%Y")
fecha_personalizada_mes = int(input("Digite el numero de mes: "))

meses={
    1: "Enero",
    2: "Febrero",
    3: "Marzo",
    4: "Abril",
    5: "Junio",
    7: "Julio",
    8: "Agosto",
    9: "Septiembre",
    10: "Octubre",
    11: "Noviembre",
    12: "Diciembre"
}
# print(meses[fecha_personalizada_mes])

boton = WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.XPATH, f'//option[text()="{meses[fecha_personalizada_mes]} - {fecha_personalizada_año}"]'))
)
boton = driver.find_element(By.XPATH, f'//option[text()="{meses[fecha_personalizada_mes]} - {fecha_personalizada_año}"]')
boton.click()


input_pass = WebDriverWait(driver,20).until(
    EC.presence_of_element_located((By.XPATH, '//input[@data-testid="password-field-input"]'))
)
input_pass = driver.find_element(By.XPATH, '//input[@data-testid="password-field-input"]')
# Introduce el password:
input_pass.send_keys(password)

boton = WebDriverWait(driver,20).until(
    EC.presence_of_element_located((By.XPATH, '//button[@data-testid="submit"]'))
)
boton = driver.find_element(By.XPATH, '//button[@data-testid="submit"]')
boton.click()

sleep(60)







