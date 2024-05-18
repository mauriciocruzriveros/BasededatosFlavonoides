# Screening Molecular : (Flavonoides - UCP-2)

Este repositorio contiene un notebook de análisis de datos de flavonoides, el cual puede ser ejecutado fácilmente desde Google Colab. 
La base de datos utilizada fue extraída del repositorio: [Freston1605/ucp_project](https://github.com/Freston1605/ucp_project) en donde se realiza la extracción de las moleculas y los resultados de un Screening Molecular con AutoDock Vina para evaluar afinidad de Flavonoides con UCP-2.

## Ejecución desde Google Colab

Puedes visualizar y ejecutar el notebook directamente desde Google Colab haciendo clic en el siguiente enlace:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mauriciocruzriveros/BasededatosFlavonoides/blob/main/flavonoids_collab.ipynb)

![Distribución de Tipos de Flavonoides](imgs/grafico_torta_flavonoides.png)


## Contenido del Repositorio
- /docking_ucp2_flavonoids : Carpeta que contiene resultados de screening molecular (Sacada de : https://github.com/Freston1605/ucp_project)
- /imgs : Carpeta que contiene las imagenes que se muestran en el notebook
- flavonoids_collab.ipynb : Este archivo contiene el notebook de Jupyter con el análisis de la base de datos de flavonoides.
- README.md : Archivo que contiene la sección que estas leyendo
- extraer_delta_g.py : Script hecho en python para extraer desde docking-ucp2-flavonoids a flavonoids_data.csv
- flavonoids_data.csv : Base de datos de Flavonoides (Sacada de : https://github.com/Freston1605/ucp_project)
- flavonoids_data_final.csv: Base de datos ocupada para analisis post-extracción.


## Ejecución Local (opcional)

Si deseas ejecutar el notebook de forma local en tu máquina, puedes hacerlo siguiendo estos pasos:

1. Clona este repositorio o descárgalo como ZIP.
2. Abre el archivo `flavonoids_collab.ipynb` en Jupyter Notebook o JupyterLab.
3. Ejecuta las celdas en orden para reproducir el análisis.

## Contribuciones

¡Se aceptan contribuciones! Si deseas mejorar este análisis, corregir errores o agregar nuevas funcionalidades, no dudes en enviar un pull request.
