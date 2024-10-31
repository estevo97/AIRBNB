import streamlit as st
import pandas as pd
import numpy as np
from pycaret.classification import load_model, predict_model
import os
import io
from PIL import Image


# Configuración de la página en modo ancho
st.set_page_config(layout="wide")

# CSS para eliminar el margen izquierdo de toda la app
st.markdown(
    """
    <style>
    /* Aumenta el ancho de la columna principal de Streamlit */
    .main .block-container {
        padding-left: 1rem;  /* Ajusta este valor a 0 para eliminar el margen */
        padding-right: 1rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Título de la app
st.title("Mapas")

st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")

st.markdown("""Para analizar los mapas es preciso tener en mente la organización territorial suíza. 
En Suíza se constituye de **26 cantones**, siendo Vaud uno de ellos. Los cantones se dividen en **distritos**, y estos a su vez
están formados por **comunas**. 
            
En nuestra tabla 'listings', la variable '*neighbourhood*' hace referencia a las comunas de cada distrito de Vaud, mientras que 
la variable 'neighbourhood_group' hace referencia a los distritos de Vaud.
""")

st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")


# Contenido principal
st.markdown("### Mapa 1. Precio/noche promedio de los AIRBNB para cada comuna de Vaud")

st.markdown("")
st.markdown("")

# Ejemplo de un elemento como un mapa HTML centrado
mapa = 'mapa_vecindarios.html'
with open(mapa, 'r') as f:
    html = f.read()
st.components.v1.html(html, width=1000, height=600)

st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")


st.markdown("""Si nos fijamos en el primer mapa, podemos observar varios hechos que llaman la atención:
            
- Los alojamientos **más caros** se encuentran sobre todo en las comunas del **sureste**.
- Los alojamientos más baratos se encuentran en la zona central y no están en la zona del lago Leman.
- En general, en la zona de Lausanne y del **lago Leman** predominan los alojamientos **intermedios** y, en menor medida, los más caros.
""")

st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")

st.markdown("""Pero si pensamos en función del distrito en el que se encuentra, los
            distritos más caros son **Aigle, Riviera-Pays-d'Enhaut y Nyon** (este último situado en el suroeste),
mientras que los más baratos son Gros-de-Vaud, Broye-Vully y Jura Nord Vaudois (véase en el segundo mapa).
            
Una vez hecha esta aclaración, volvamos al informe a proseguir con el análisis exploratorio.""")

st.markdown("### Mapa 2. Distritos de Vaud")

st.markdown("")
st.markdown("")

imagen = Image.open('img/distritos_vaud.png')

st.image(imagen, caption='Distritos de Vaud (Suíza)| Autor: Tschubby. Fuente: https://commons.wikimedia.org/wiki/File:Karte_Kanton_Waadt_Bezirke_2013.png', use_column_width=True, width=600)










