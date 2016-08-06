# [Tarea 1](https://github.com/ICDRepository-I-2016/preprocesamiento-de-datos-josemalvarezg1)

## Tabla de contenido

* [Implementación](#implementación)
* [Archivos que contiene el repositorio](#archivos-que-contiene-el-repositorio)
* [Herramientas](#herramientas)
* [Datasets](#datasets)
* [Inicialización](#inicialización)	
* [Importante](#importante)	
* [Creador](#creador)


# Implementación

En esta tarea se obtiene un dataset relacionado a la venta de laptops realizando la extracción de datos crudos a la página web www.pcel.com. Se utilizará la herramienta Scrapy para generar la vista minable en un archivo .csv que contendrá las especificaciones de las laptops (ver databook.txt). Este archivo será trabajado posteriormente para su limpieza. Los datos correspondientes al modelo y marca de las laptops serán considerados con el tipo de dato string, mientras que los datos correspondientes a los precios de las laptops serán considerados con el tipo de dato flotante. Como se explica en el archivo databook.txt, no siempre las columnas correspondientes a los precios contienen información en caso de que se haya realizado una rebaja o no, por lo que se debe replicar el precio actual en las columnas que estén vacías por si se desea trabajar con ellas.

# Archivos que contiene el repositorio

El siguiente repositorio contiene las siguientes carpetas con los diversos archivos:

```
preprocesamiento-de-datos-josemalvarezg1/
├── README.md
├── src/
│   ├── preproc.py
│   ├── scrapy.cfg   
│   └── scraper 
│		├──__init__.py
│		├── items.py
│		├── pipelines.py
│		├── settings.py
│		├── vista-minable.csv
│		└── spiders
│			├── __init__.py
│			└── pcel.py
└── doc/
    └── databook.txt
```

# Herramientas

En la presente tarea se utilizaron las siguientes herramientas con respectivas versiones:

| Herramienta                         	 | Versión   													   |                            
|----------------------------------------|-----------------------------------------------------------------|
| Spyder.        			        	 | 2.3.8.														   |
| Python.					             | 2.7.12.  													   |
| Pandas.					             | 0.17.1.  													   |
| Scrapy.					             | 1.0.3.	  													   |

# Datasets
Los conjuntos de datos generados al realizar el scraping fueron los siguientes:

| Dataset                        		 |            Resumen                            									  | Elementos |
|----------------------------------------|------------------------------------------------------------------------------------|-----------|
| vista-minable.csv                  	 | Representa a todas las laptops en venta en la página www.pcel.com				  |    306*   |

*La cantidad de elementos del dataset dependerá de la cantidad de laptops que se obtengan al realizar el scraping.


# Inicialización
Clonar el siguiente repositorio:
```sh
git clone https://github.com/ICDRepository-I-2016/preprocesamiento-de-datos-josemalvarezg1
```
Posicionarse en la capeta del repositorio clonado:
```sh
cd preprocesamiento-de-datos-josemalvarezg1/src
```

# Importante
Al ejecutar el script se debe modificar la ruta para leer el dataset. Si se desea generar de nuevo, se debe borrar el archivo vista-minable.csv y ejecutar el siguiente comando:
```sh
scrapy crawl pcel -o vista-minable.csv -t csv
```

# Creador

**José Manuel Alvarez García - CI 25038805**
