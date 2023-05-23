# Beautiful Soap

## Este trabajo consiste en dos aplicaciones:

1. En los archivos `WScrap_BS.ipynb` y `WScrap_BS.py` se utiliza la librería para extraer, desde una página web de películas, el título y el guión del film ‘Titanic’

2. En el archivo `mundiales.ipynb` se utiliza la librería para obtener:

	a) información de todos los partidos de fútbol de un Mundial en particular, obteniendo todos los equipos que hicieron de local, de visitante y los resultados
	
	b) información de todos los partidos de fútbol de todos los Mundiales, obteniendo todos los equipos que hicieron de local, de visitante y los resultados, guardando todo en un archivo .csv
	
### Desarrollado en python

-------

<img width="1000" alt="image" src=https://i0.wp.com/thedukh.com/wp-content/uploads/2022/10/webscrapingwithpythonandbeautifulsoup.png>

-------

#### Los pasos que se realizaron:

1-	Crear el directorio de trabajo --> 1-Beautiful_Soap

2-	Desde la Terminal, entrar a la carpeta y crear el entorno virtual --> WebScrap_BS (`python3 -m venv WebScrap_BS`)

3-	Activar el entorno virtual (`source WebScrap_BS/bin/activate`)

4-	Instalar librería -->  Beautiful Soap (`pip install bs4`). Es la herramienta de extracción de datos web

5-	Instalar librería --> Requests (`pip install requests`). Manda las solicitudes a la página web

6-	Instalar librería --> Pandas (`pip install pandas`). Generar dataframes para su tratamiento y presentación

7-	Instalar librería --> Ipykernel (`pip install ipykernel`). Para el kernel en VSC

8-	Como parser se usará el que viene por defecto con python (‘html.parser’). El parser lo necesita BS para extraer datos de html. Hay varios parsers y se podría necesitar otro, en cuyo caso habría que instalarlo

9-	Con esto concluye el detalle de librerias instaladas

10-	Crear el archivo requirements.txt (`pip freeze > requirements.txt`)

11-	Crear archivos para el código de la 'aplicación 1' (`touch WScrap_BS.ipynb` que incluirá explicación de los pasos que se realizan, y `touch WScrap_BS.py`)

12-	Crear archivo para el código de la 'aplicación 2' (`touch mundiales.ipynb`)

13-	Abrir con el IDE VSC (`code .`)

14-	Ya en VSC seleccionar la versión de python relacionada con el nombre del entorno

15-	A partir de acá se realizó lo que está en los archivos .ipynb y .py

-------

<img width="1000" alt="image" src=https://www.grid.cl/blog/wp-content/uploads/2019/03/001-efficient-web-scraping.png>

-------

#### Para ejecutarlo en otro equipo:

1.	Clonar el repositorio

2.	Moverse a la carpeta 1-Beautiful_Soap
	
3.	Crear un entorno virtual
	
4.	Activar el entorno virtual
	
5.	Ejecutar pip install -r requirements.txt
	
6.	Ejecutar el archivo correspondiente a la aplicación deseada (`WScrap_BS.ipynb` o `mundiales.ipynb`)
	
7.	Al terminar la ejecución se habrá creado una carpeta ‘Files’ donde se encontrarán los archivos generados

-------

### Autor:

--> Alejandro Busquet
* Linkedin: [Acá](https://www.linkedin.com/in/alejandro-busquet/ "Acá")
* Linkedin: [Acá](https://www.linkedin.com/in/alejandro-busquet/ "Acá"){:target="_blank"}
* Mail: algabu00@gmail.com
* Mail: [algabu00@gmail.com](mailto:algabu00@gmail.com){:target="_blank"}

