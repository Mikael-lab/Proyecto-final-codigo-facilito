# Importacion de librerias
import streamlit as st
import pandas as pd
import altair as alt

from funpymodeling.exploratory import status


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
st.sidebar.markdown(
    """
    Puedes utilizar el selector de esta barra para cambiar en tiempo real
    los valores a utilizar de uno o más meses.
    >**Nota:** El dataset contiene datos del segundo semestre del año 2010
    """
)

# Intro section
st.title("Exploración de datos de créditos Bancarios en su proceso de cobranza en el año 2010.")
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

    Para poder filtrar los datos a visualizar por mes, le agregamos la columna `Mes` al dataset original

    ```python
    # Crear columna de mes para poder filtrar la informacion
    data['Fecha'] = pd.to_datetime(data['Fecha'])
    data.insert(0,'Mes', (data['Fecha'].dt.month).astype(int) )

    # Creacion de list para el selector
    list_meses = data['Mes'].unique()
    list_meses.sort()

    mes = st.sidebar.multiselect('Seleccione el Mes', list_meses, list_meses[0])

    # dataframe filtrado 
    data_filter = data[
        (data['Mes'].isin(mes))
    ]

    Lo ponemos en la primer columna para visualizar el cambio de seleccion
    ```
    """
)
# Crear columna de mes para poder filtrar la informacion
data['Fecha'] = pd.to_datetime(data['Fecha'])
data.insert(0,'Mes', (data['Fecha'].dt.month).astype(int) )

# Creacion de list para el selector
list_meses = data['Mes'].unique()
list_meses.sort()

mes = st.sidebar.multiselect('Seleccione el Mes', list_meses, list_meses[0])

# dataframe filtrado 
data_filter = data[
    (data['Mes'].isin(mes))
]

st.write(data_filter)

# Imputación de datos
st.header("Imputación de datos")
st.markdown(
    """
    Dadas las reglas de negocio que están implementadas en el software que se utiliza
    para el proceso de cobranza, las columnas que utilizaremos no contienen valores nulos o vacios.

    **Regla de registro de gestion:** Una gestión siempre deberá tener fecha y un resultado.
    """    
)


# Gráficas Containner principal
with st.container():
    # Titulo
    st.title('Visualización de datos')
    st.markdown(
        """
        Para poder grágicar las `promesas de pago` por mes vamos a crear un nuevo dataframe que solo contenga la fecha y el resultado.
        """
    )

df_fecha_codResultado = data_filter[['Fecha','IdCodResultado']]

st.write(df_fecha_codResultado)

st.markdown(
    """
    Despues hacemos un crosstab para agruparlo por mes, en donde las columnas pasan a ser los IdCodResultado
    """
)


df_fecha_codResultado.Fecha = pd.to_datetime(df_fecha_codResultado.Fecha,dayfirst=True)
df_fecha_codResultado.IdCodResultado = df_fecha_codResultado['IdCodResultado'].astype('string')

# Filtramos para solo tener las promesas de pago
df_promesas = df_fecha_codResultado[df_fecha_codResultado.IdCodResultado.isin(['49'])]



if df_promesas.empty == False:

    df_promesas_group = pd.crosstab(df_promesas.Fecha, df_promesas.IdCodResultado).resample("M").sum().reset_index()

    st.write(df_promesas_group)
    c = alt.Chart(df_promesas_group).mark_bar(size=90).encode(
        y= alt.Y("49", title="Promesas"),
        x= alt.X("Fecha", title = "",timeUnit='month'),
        color = alt.Color("49", title = "Volumen", scale = alt.Scale( scheme = "blues")),
        tooltip=[alt.Tooltip('49',title='Promesas')]
    ).interactive().properties(
        title="Promesas de pago en el segundo semestre del año 2010"
    )
    st.altair_chart(c, use_container_width=True)
else:
    st.markdown(
        """
        >**El mes o meses seleccionados no contiene promesas de pago para gráficar**
        """
        )

st.markdown(
    """
    Con el trabajo que hemos realizado hasta este punto ya pudimos identificar el `mes en el que se registraron más promesas de pago`, que fue `Agosto con un total de 5,402`.

    El paso siguiente es saber el volumen de gestiones totales en comparacion con la cantidad de promesas de pago
    """
)

# Obtenemos los totales por mes de todos los codigos de resultado

df_totales = pd.crosstab(df_fecha_codResultado.Fecha,df_fecha_codResultado.IdCodResultado,dropna=True).resample("M").sum().reset_index()
df_totales.loc['total_gestiones', :] = df_totales.sum(numeric_only=True)
df_totales['total_gestiones'] = df_totales.sum(axis=1, numeric_only=True)

df_totales_filter = df_totales[['Fecha','total_gestiones']].query('total_gestiones > 0')
st.write(df_totales_filter)


# Creamos los objetos para graficar
scale = alt.Scale(domain=["Promesas","Gestiones"], range=['red','lightblue'])

if df_promesas.empty == False:
    base = alt.Chart(df_totales).transform_calculate(
        line="'Promesas'",
        bar="'Gestiones'"
    ).encode(
        alt.X("Fecha",title="",timeUnit='month'),
    ).properties(
        title="Volumen de gestiones y cantidad de promesas conseguidas"
    )

    bar = base.mark_bar().encode(
        alt.Y('total_gestiones',title="Gestiones"),
        tooltip=[alt.Tooltip("total_gestiones", title='Gestiones')],
        color=alt.Color('bar:N', scale=scale, title=''),
    )

    line = base.mark_line(point=alt.OverlayMarkDef(color="red")).encode(
        alt.Y("49",title=""),
        tooltip=[alt.Tooltip('49',title='Promesas')],
        color=alt.Color('line:N', scale=scale, title='')
    )

    text_line = line.mark_text(
        align='right',
        baseline='bottom',
        dx=3
    ).encode( 
        text='49'
    )

    c = bar+(line+text_line).interactive()

    st.altair_chart(c,use_container_width=True)

    st.markdown(
        """
        Con la siguiente gráfica podemos observar lo siguiente:

        El volumen de gestiones es abismalmente superior a la cantidad de promesas de pago generadas en cada mes.

        El volumen de gestiones no siempre es proporcional a la cantidad de promesas de pago obtenidas. En el mes de Septiembre se obtuvieron un total de 3,952 promesas de pago con un `volumen de gestiones de 217,595`, en el mes de `Octubre se obtuvieron 4,296 con un volumen de 192,522`.

        ## Conclusiones ##
        En este punto ya podemos contestar las preguntas que planteamos al principio.

        1. ¿Que cantidad de Gestiones se realizan en periodos de 1 mes?

        1. ¿Que cantidad de promesas de pago se consiguieron en periodos de 1 mes? 
        >**R= se puede visualizar en la gráfica "Volumen de gestiones y cantidad de promesas conseguidas"**

        1. ¿Hay relación entre el volumen de Gestiones y la cantidad de promesas de pago? 
        >**R= con los datos que se tienen hasta el momento no se observa una relación que nos indique que a mayor volumen de gestiones mayor cantidad de promesas de pago se van a obtener, claro que esto es forma general.**
        """
        )
else:
    st.markdown(
        """
        >**El mes o meses seleccionados no contiene promesas de pago para gráficar**
        """
        )