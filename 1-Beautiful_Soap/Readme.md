# Beautiful Soap

### Uso de la librería ‘Beautiful Soup’ para extraer, desde una página web, el título y el guión de la película ‘Titanic’
### Desarrollado en python

-------

#### Los pasos que se realizaron:

1-	Crear el directorio de trabajo --> 1-Beautiful_Soap

2-	Desde la Terminal, entrar a la carpeta y crear el entorno virtual --> WebScrap_BS (python3 -m venv WebScrap_BS)

3-	Activar el entorno virtual (source WebScrap_BS/bin/activate)

4-	Instalar librería -->  Beautiful Soap (pip install bs4). Es la herramienta de extracción de datos web

5-	Instalar librería --> Requests (pip install requests). Manda las solicitudes a la página web

6-	Instalar librería --> Ipykernel (pip install ipykernel). Para el kernel en VSC

7-	Como parser se usará el que viene por defecto con python (‘html.parser’). El parser lo necesita BS para extraer datos de html. Hay varios parsers y se podría necesitar otro, en cuyo caso habría que instalarlo

8-	Con esto ya están las librerias instaladas

9-	Crear el archivo requirements.txt (pip freeze > requirements.txt)

10-	Crear archivo para el código (touch WScrap_BS.ipynb). Este archivo incluirá una explicación de los pasos que se realizan

11-	Crear archivo para el código ('touch WScrap_BS.py')

12-	Abrir con el IDE VSC (code .)

13-	Ya en VSC seleccionar la versión de python relacionada con el nombre del entorno

14-	A partir de acá se realizó lo que está en los archivos .ipynb y .py

-------

#### Para ejecutarlo en otro equipo:

1.	Clonar el repositorio

2.	Moverse a la carpeta 1-Beautiful_Soap
	
3.	Crear un entorno virtual
	
4.	Activar el entorno virtual
	
5.	Ejecutar pip install -r requirements.txt
	
6.	Ejecutar el archivo WScrap_BS.ipynb o WScrap_BS.py
	
7.	Al terminar la ejecución se habrá creado una carpeta ‘Files’ donde se encuentra el archivo generado

-------
