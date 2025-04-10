import streamlit as st
import pandas as pd
import numpy as np
from pycaret.classification import load_model, predict_model
import os
import io
from PIL import Image


st.markdown('<h1 class="title-text">V I A J E &nbsp; &nbsp; A &nbsp; &nbsp; L O S &nbsp; &nbsp; A L P E S &nbsp; &nbsp; E N &nbsp; &nbsp; C O M P A Ñ Í A</h1>', unsafe_allow_html=True)


st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Merriweather:wght@700&display=swap');

    .title-text {
        font-family: 'Merriweather', serif;
        font-size: 44px;
        color: #221166;
        background-color: #eeffdd;
        text-align: center;
        border-radius: 10px;
    }

    </style>
    """, unsafe_allow_html=True)

#dejar un espacio
st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")

st.markdown("""# Encuéntranos el mejor sitio""")
st.markdown("")
st.markdown("")

st.write('**Presentado por: Estevo Arias García**')

imagen = Image.open('img/planning.jpg')
st.image(imagen, caption='Así se planeaban antes los viajes | Fuente:pxhere.com: https://pxhere.com/es/photo/1622940', use_container_width=True)

st.markdown("""### ¿Y si un grupo de colegas te encomendase un análisis de datos para escoger alojamiento en Vaud?""")


st.sidebar.title('Menú de la Aplicación')

icono = Image.open('img/abn3.png')
# Cargar el icono en el menu de aplicacion
st.sidebar.image(icono, use_container_width=True)


st.markdown("""## En el presente trabajo...""")

st.markdown("""
- Plantearemos **TRES casos** de personas que quieren encontrar el mejor alojamiento.
- Cada uno con sus criterios, trataremos de ofrecerle la mejor opción.
- Podremos descubrir qué apartamentos están **libres en el período** que elijamos.
""")

st.markdown("""## Y además...""")

st.markdown("""
- Crearemos **dashboards INTERACTIVOS** con los que cualquiera pueda juguetear.
- Descubriremos en qué comunas y distritos están los alojamientos más caros y más baratos.""")






