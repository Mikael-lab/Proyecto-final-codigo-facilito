# Importacion de librerias
import streamlit as st
import pandas as pd
import plotly.express as px

# Set page config
st.set_page_config(
    page_title='Proyecto Final', # Titulo de la pagina
    page_icon='📊', # Icono de la pagina
    layout='centered', # Ancho de la pagina (wide, center)
    initial_sidebar_state='expanded', # Estado inicial del sidebar (expanded, collapsed)
    menu_items={'Get Help': 'https://twitter.com/DSandovalFlavio',
                'Report a bug': 'https://github.com/DSandovalFlavio/CF-Dashboarding-Streamlit',
                'About': 'Taller de Dashboarding con Streamlit para el Bootcamp de Ciencia de Datos de CodigoFacilito.'}
)


# Sidebar
st.sidebar.title("Poryecto final Bootcamp de Ciencia de Datos")


# Intro section
st.title("Exploración de datos de créditos Bancarios en su proceso de cobranza en el año 2010 - segundo semestre.")
st.write(
    """
     Bienvenid@, este es mi proyecto final del bootcamp de ciencia de datos en código facilito. Primeramente agradecer a la empresa SCORE que me proporciono datos reales de su operación, datos que nos servirán para el desarrollo y análisis de los mismos.
    """
)

# Context
st.header("Contexto")
st.markdown(
    """
La empresa SCORE es una agencia de cobranza con más de 15 años en el mercado, teniendo a diferentes clientes de distintos giros pero con una caracteristica en común, que cada empresa tiene la posibilidad de otrogar créditos, créditos de los cuales SCORE realiza el proceso de cobranza.

Cobranza: La cobranza es el acto o procedimiento por el cual se consigue la contraprestación por un bien o servicio o la cancelación de una deuda.

Referencia: https://economipedia.com/definiciones/cobranza.html

Para este proyecto nos enfocaremos en analizar la información de contacto con el deudor, dicho de otra manera, la gestión de la cuenta.

El objetivo final de cada gestión realizada a una cuenta es conseguir una promesa de pago por parte del titular.

Una promesa de pago es el registro de la fecha en que el titular se compromete a realizar el pago solicitado.

Dados estos escenarios, las preguntas que buscamos responder son las siguientes:

¿Que cantidad de Gestiones se realizan en periodos de 1 mes?

¿Que cantidad de promesas de pago se consiguieron en periodos de 1 mes?

¿Hay relación entre el volumen de Gestiones y la cantidad de promesas de pago?

Palabras clave: gestión, promesa de pago
    """
)


# Load data
data = pd.read_csv('data/gestiones_bnx_filtradas.csv')

st.header("Cargando los datos")
st.markdown(
    """
    A continuación cargamos los datos (originales) a utilizar. Dichos datos pueden ser encontrados en la carpeta de datos como `data/gestiones_bnx_filtradas.csv`.

>**Nota**: Los datos y el código fuente de esta aplicación web pueden 
>ser encontrados en el repositorio de GitHub https://github.com/Mikael-lab/Proyecto-final-codigo-facilito.

>Los datos pueden ser cargados utilizando pandas con las líneas:

```python
import pandas as pd
data = pd.read_csv('data/gestiones_bnx_filtradas.csv')
```

> **Nota:** Para desplegar los datos en pantalla, puedes llamar directamente a la variable
> desde una celda si usas  Google Colab que fue en donde trabaje el proyecto.
> ```python
># Desde un notebook
>data
>```

Al desplegar los datos deberías ver una tabla como la siguiente:
""")

st.dataframe(data)
st.markdown(
    """
    Podemos ver que nuestros datos tiene en total `10 columnas y 1,028,398 registros de gestiones`.

    Para este análisis solamente utilizaremos los campos: `Fecha, IdCodResultado`.

    | Campo       | Descripción    |
    |    :----:   |          :---: |
    | Fecha       | Fecha en que se realizo la gestión   |
    | IdCodResultado       | Id que identifica el resultado de una gestión      |

    En el sistema que recopila la información existe un catalogo de resultados de gestión, por ejemplo: 
    - No contesta
    - Ausente
    El que utilizaré para este análisis es el IdCodResultado=49,`el Id 49 pertenece a Promesa de pago`.

    """
)