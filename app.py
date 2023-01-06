# Importacion de librerias
import streamlit as st
import pandas as pd
import plotly.express as px

# Set page config
st.set_page_config(
    page_title='Dashboard', # Titulo de la pagina
    page_icon='📊', # Icono de la pagina
    layout='wide', # Ancho de la pagina (wide, center)
    initial_sidebar_state='expanded', # Estado inicial del sidebar (expanded, collapsed)
    menu_items={'Get Help': 'https://twitter.com/DSandovalFlavio',
                'Report a bug': 'https://github.com/DSandovalFlavio/CF-Dashboarding-Streamlit',
                'About': 'Taller de Dashboarding con Streamlit para el Bootcamp de Ciencia de Datos de CodigoFacilito.'}
)

# Exploración de datos de créditos Bancarios en su proceso de cobranza en el año 2010 - segundo semestre.
# Bienvenid@, este es mi proyecto final del bootcamp de ciencia de datos en código facilito. Primeramente agradecer a la empresa SCORE que me proporciono datos reales de su operación, datos que nos servirán para el desarrollo y análisis de los mismos.

# Contexto
# La empresa SCORE es una agencia de cobranza con más de 15 años en el mercado, teniendo a diferentes clientes de distintos giros pero con una caracteristica en común, que cada empresa tiene la posibilidad de otrogar créditos, créditos de los cuales SCORE realiza el proceso de cobranza.

# Cobranza: La cobranza es el acto o procedimiento por el cual se consigue la contraprestación por un bien o servicio o la cancelación de una deuda.

# Referencia: https://economipedia.com/definiciones/cobranza.html

# Para este proyecto nos enfocaremos en analizar la información de contacto con el deudor, dicho de otra manera, la gestión de la cuenta.

# El objetivo final de cada gestión realizada a una cuenta es conseguir una promesa de pago por parte del titular.

# Una promesa de pago es el registro de la fecha en que el titular se compromete a realizar el pago solicitado.

# Dados estos escenarios, las preguntas que buscamos responder son las siguientes:

# ¿Que cantidad de Gestiones se realizan en periodos de 1 mes?

# ¿Que cantidad de promesas de pago se consiguieron en periodos de 1 mes?

# ¿Hay relación entre el volumen de Gestiones y la cantidad de promesas de pago?

# Palabras clave: gestión, promesa de pago

# Cargando los datos
# A continuación cargamos los datos (originales) a utilizar. Dichos datos pueden ser encontrados en la carpeta de datos como data/gestiones_bnx_filtradas.csv.

# Nota: Los datos y el código fuente de esta aplicación web pueden ser encontrados en el repositorio de GitHub https://github.com/RodolfoFerro/proyecto-ejemplo.

# Los datos pueden ser cargados utilizando pandas con las líneas:


# import pandas as pd
# data = pd.read_csv('data/datos_ventas.csv')
# Nota: Para desplegar los datos en pantalla, puedes llamar directamente a la variable desde una celda si usas Jupyter Notebooks/Lab o Google Colab o imprimir los datos con la función print.


# # Desde un notebook
# data
# # Desde un script
# print(data)
# Al desplegar los datos deberías ver una tabla como la siguiente: