from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pandas as pd
import time
import os


# --> Abrir el navegador web e ingresar a la página

# Establecer la pagina web a trabajar
website = 'https://www.adamchoi.co.uk/teamgoals/detailed'

# Estblecer la ruta del archibo ChromeDriver descargado
path = '/Users/mac/Desktop/Web_Scraping/2-Selenium/ChromeDriver/chromedriver'

# Definir la variable que abrira la web
driver = webdriver.Chrome(path)

# Dar la indicación para que abra la web
driver.get(website)


# --> Seleccionar el botón que dice "All Matches"

all_matches_button = driver.find_element(by='xpath', value='//label[@analytics-event="All matches"]') 
all_matches_button.click()


# --> Seleccionar el país 'Spain' (dentro del menú desplegable 'Select country')

dropdown = Select(driver.find_element(by='id', value='country'))
dropdown.select_by_visible_text('Spain')

# Establecer 5 segundos de espera por el tiempo de carga que tiene la página
time.sleep(5)


# --> Extracción de los datos de todos los partidos (desde la caja de los matches)

matches = driver.find_elements(by='xpath', value='//tr')

# En matches ya están cargados todos los partidos. Ahora va entrando en cada uno para mandarlos a una lista.
partidos = []
for match in matches:
    #print(match.text)
    partidos.append(match.text)


# --> Cerrar el navegador web

# Se cierra el driver (que se habia abierto con el 'get').
driver.quit()


# --> Pasar los datos a dataframe, mostrar por pantalla y guardar en disco

# Mediante pandas, se convierten los datos a dataframe.
df = pd.DataFrame({'Partidos de La Liga' : partidos})

# Mostrar por pantalla.
print(df)

# Crear la carpeta para guardar el archivo, si no existe.
path = "./Files"
if not os.path.exists(path):
    os.makedirs(path)

# Guardar los datos en archivo.
df.to_csv('./Files/partidos.csv', index=False)
