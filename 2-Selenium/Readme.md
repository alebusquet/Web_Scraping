# Selenium

### Uso de la librería ‘Selenium’ para extraer, desde una página web, los partidos de fútbol de 'La Liga'
### Desarrollado en python

-------

<img width="1000" alt="image" src=https://www.devopsschool.com/blog/wp-content/uploads/2022/03/banner-selenium.png>

-------

#### Los pasos que se realizaron:

1-	Crear el directorio de trabajo --> 2-Selenium
	
2-	Desde la Terminal, entrar a la carpeta y crear el entorno virtual --> WebScrap_Sel (`python3 -m venv WebScrap_Sel`)

3-	Activar el entorno virtual (`source WebScrap_Sel/bin/actívate`)

4-	Se necesita descargar e instalar 'Selenium WebDriver'. Para esto:

  *	Crear una carpeta ‘ChromeDriver’ en la raíz del entorno virtual

  *	Ir a la página https://chromedriver.chromium.org/downloads

  *	En los ‘Current Releases’, ubicar la versión que se corresponda con la versión propia de Chrome, que es el navegador que se abrirá (ir a 3 puntitos, Help, About Google Chrome, Versión) y dar click

  *	Seleccionar el SO (mac64.zip), descargar en la nueva carpeta, y descomprimir

5-	Instalar librería --> Selenium (`pip install selenium`)

6-	Instalar librería --> Pandas (`pip install pandas`). Sólo para convertir todo a un df al final

7-	Instalar librería --> Ipykernel (`pip install ipykernel`). Para el kernel de VSC

8-	Con esto ya esta instalado todo lo previo

9-	Crear el archivo requirements.txt (`pip freeze > requirements.txt`)

10-	Crear archivo para el código (`touch WScrap_Sel.ipynb`). Este archivo incluirá una explicación de los pasos que se realizan

11-	Crear archivo para el código (`touch WScrap_Sel.py`)

12-	Abrir con el IDE VSC (`code .`)

13-	Ya en VSC seleccionar la versión de python relacionada con el nombre del entorno

14-	A partir de acá se realizó lo que está en los archivos .ipynb y .py

-------

<img width="1000" alt="image" src=https://kinsta.com/wp-content/uploads/2022/07/Types-of-web-data.png>

-------
#### Para ejecutarlo en otro equipo:

1.	Clonar el repositorio

2.	Moverse a la carpeta 2-Selenium

3.	Crear un entorno virtual

4.	Activar el entorno virtual

5.	Ejecutar `pip install -r requirements.txt`

6.	Ejecutar el archivo ‘WScrap_Sel.ipynb’ o ‘WScrap_Sel.py’

7.	Al terminar la ejecución se habrá creado una carpeta ‘Files’ donde se encuentra el archivo generado

-------

### Autor:

--> Alejandro Busquet

* Linkedin: [Acá](https://www.linkedin.com/in/alejandro-busquet/ "Acá")

* Mail: <a href="mailto:algabu00@gmail.com" target="_blank">algabu00@gmail.com</a>
