from bs4 import BeautifulSoup
import requests
import os

# Definir la url del website.
website = 'https://subslikescript.com/movie/Titanic-120338'

# Enviar solicitud a la página.
response = requests.get(website)

# Obtener la respuesta.
content = response.text

# La variable soup nos permite localizar elementos en una página web.
soup = BeautifulSoup(content, 'html.parser')

# Ver lo que tenemos hasta acá, que es el código html de la página.
print(soup.prettify())

# Buscar primero el elemento raíz, que es el que abarca todo el contenido.
# Utilizamos el find con el nombre del tag y el atributo.
box = soup.find('article', class_='main-article')

# En este ejercicio vemos que el elemento del Título es un tag (no contiene clase ni ID).
# Entonces localizamos este elemento con el nombre del tag, que es 'h1'.
title = box.find('h1').get_text()

# Imprimir para verificar que con lo hecho hasta acá tenemos el Título
print(title)

# Se pasan parámetros al get_text():
transcript = box.find('div', class_='full-script').get_text(strip=True, separator=' ')

# Imprimir para ver que con lo hecho hasta acá tenemos el transcript
print(transcript)

# Crear la carpeta para guardar el archivo, si no existe.
path = "./Files"
if not os.path.exists(path):
    os.makedirs(path)
    
# Guardar el archivo en la carpeta
with open(f'./Files/{title}.txt', 'w', encoding='utf-8') as file:
    file.write(transcript)

