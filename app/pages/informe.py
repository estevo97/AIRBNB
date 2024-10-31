



import streamlit as st
import pandas as pd
import numpy as np
from pycaret.classification import load_model, predict_model
import os
from PIL import Image


st.markdown('<h1 class="title-text">V A U D</h1>', unsafe_allow_html=True)


st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Libre+Bodoni:wght@700&display=swap');

    .title-text {
        font-family: 'Libre Bodoni', serif;
        font-size: 50px;
        color: #221166;
        background-color: #eeffdd;
        text-align: center;
        border-radius: 10px;
    }

    </style>
    """, unsafe_allow_html=True)


st.title('**Análisis de los AIRBNB**')

st.markdown("""## Introducción al informe""")

st.markdown("""El otro día, hablando con un amigo sobre un viaje que estamos pensando de hacer en grupo a los Alpes Suízos, me 
vine un pelín arriba y le dije que tenía un método infalible para encontrar los mejores alojemientos posibles en AIRBNB.
            
A decir verdad, me comprometí a hacer un buen análisis de datos de los alojamientos del condado de Vaud, que es aquel al que 
supuestamente tenemos pensado ir. Es una suerte que haya encontrado datos en la web *insideairbnb.com* justamente para este condado (no había datos
de ninguna otra parte de Suíza)
            
Sin embargo, con el fin de practicar un poco mis habilidades de ingeniero y/o analista de datos, he decidido imaginarme que una agencia de 
viajes contrata mis servicios para que encuentre el mejor alojamiento posible en dos escenarios diferentes.
            
Así que, una vez me haya probado con estos dos ejemplos, me pondré manos a la obra con la tarea que me incumbe a mí y a mis amigos.""")


st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")

st.markdown("""## Trabajo""")


st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")

st.markdown("""El objetivo de este trabajo es encontrar el mejor alojamiento de AIRBNB de Vaud para tres casos diferentes (dos ficticios y uno real):
        
- 1. Un **esquiador** que busca el mejor alojamiento cerca de las pistas para enero.
- 2. Una **familia** de dos padres y un niño que buscan pasar la navidad en un sitio bien equipado y que esté cercano al lago Leman.
- 3. Un **grupo de amigos** con los que me iré de viaje en la próxima semana santa.""")





imagen = Image.open('img/chatillon.jpg')
st.image(imagen, caption='Chateau de Ouchy en Lausanne (Suíza)| Autor: Pablo Monteagudo. Fuente: https://www.flickr.com/photos/26528022@N07/8424500042', use_column_width=True)


st.markdown("""## **Análisis exploratorio de datos**""")

st.markdown("""Antes de empezar con la búsqueda de los alojamientos, es importante tener una **idea general de nuestras variables**
más importantes, por lo que tocará hacer un buen análisis exploratorio de datos.

En primer lugar, realizamos un histograma de la variable precio, que es nuestra variable objetivo. Como podemos observar,
hay un claro **sesgo** hacia la derecha, lo que significa que tenemos muchos alojamientos baratos y unos cuantos
que superan por mucho la media, que está en torno a los 180 dólares por noche (véase línea verde).""")


imagen = Image.open('img/densidad_precios.png')
st.image(imagen, caption='Densidad de precios de los alojamientos de Vaud', use_column_width=False, width=800, output_format='PNG')


st.markdown("""Sin embargo, es muy posible que haya zonas de este cantón con alojamientos mucho más caros que otras. ¿Y si mirásemos la media 
de precio por noche para cada uno de los vecindarios ('*neighbourhoods*' en nuestra tabla)?

Para ello, podemos **consultar el apartado 'mapa'** de esta aplicación.""")
            
st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")

st.markdown("""Otro análisis que podemos hacer es el de ver los precios en función de los tipos de propiedad que
se ofertan en AIRBNB. En esta tabla podemos ver que tenemos demasiados tipos. Con el fin de simplificar nuestro análisis,
nos centraremos únicamente en los 10 tipos de propiedad que más se repiten.""")
            

st.subheader('Tipos de propiedad y su frecuencia en los anuncios')

data = pd.read_csv('tablas/tabla_property_type.csv')
st.dataframe(data)

st.markdown("""En la siguiente gráfica podemos ver que los alojamientos más caros son aquellos que ofrecen la **vivienda completa**, 
mientras que en un segundo plano están las habitaciones privadas.
            
Cabe resaltar que el tipo de propiedad más habitual es el de *private room in rental unit*, es decir, habitaciones en unidades de alquiler.""")



st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")

imagen = Image.open('img/top_10_propiedades.png')
st.image(imagen, use_column_width=False, width=800, output_format='PNG')

st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")

st.markdown("""Por último, nos interesa también ver cómo puntúa la gente en función de lo cara que le sale la estancia por noche. Nos interesa
la puntuación general, pero también puede resultar interesante la puntuación respecto a la **calidad/precio**, es un aspecto que puede 
ser prioritario para muchos turistas.
            
Como podemos ver en la siguiente gráfica, la puntuación general va aumentando conforme aumenta el estatus del alojamiento, pero
**no sucede lo mismo** con la relación calidad/precio. Esto nos lleva a pensar que las personas que están dispuestas a pagar un precio
alto, si bien valoran la calidad de alojamiento en el que han estado, son conscientes de que han pagado un precio elevado por ella.
            
También llama la atención que los alojamientos del rango de precios bajos mejoran a los del rango bajísimo en los dos indicadores. Esto 
nos indica que debe haber un salto notable en calidad entre el grupo de alojamientos con precios inferiores a los 50 dólares por noche y los que están 
entre 50 y 100.""")

imagen = Image.open('img/puntuaciones.png')
st.image(imagen, use_column_width=False, width=800, output_format='PNG')

st.markdown("")
st.markdown("")
st.markdown("")

st.markdown("""Realizado el análisis exploratorio, entraremos de lleno en estos tres casos.""")

st.markdown("")
st.markdown("")

st.markdown("""## **Caso número 1: El esquiador**""")

st.markdown("""Las condiciones que impone este cliente son las siguientes:
- 1. Quiere ir entre el **6 y el 16 de enero** porque habrá mucha nieve y no estarán las pistas de esquí tan colapsadas como en navidades.
- 2. A poder ser, quiere un alojamiento **próximo a las estaciones** de esquí.
- 3. Quiere un alojamiento completo para el solo.
- 4. Está dispuesto a pagar hasta **150 dólares** por noche.
- 5. A poder ser, le gustaría que el alojamiento tuviese buenas **vistas**.
""")

st.markdown("""Tratándose de una persona interesada en desplazarse diariemente a una estación de esquí, lo primero es ver qué estaciones hay cerca de 
nuestra área. Encontramos bastantes estaciones en la cadena montañosa situada al sur del distrito de **Aigle**, así que es en este distrito 
en el que tendremos que centrar nuestra búsqueda.

El método que utilizaremos será análogo para los tres casos. 

Para el caso del esquiador, creamos un dashboard de Power BI en el que introducimos:
- Tablas de **Segmentación** para la Fecha de entrada y salida, para elegir un rango de precio, un tipo de propiedad
y una modalidad de arrendamiento (compartir apartamento, habitacion de hotel, casa completa o compartir habitación) 
- Tablas estándar para el nombre, precio y url del anuncio. La url es importante ponerla porque nos permite acceder al
portal donde se ha publicado el anuncio y obtener información adicional que pueda ayudarnos a tomar una determinación de
manera más rápida, así como ver las fotos.            
""")

st.markdown("""Llega el momento del filtrado. Lo primero es seleccionar las fechas desde el 6 de enero hasta el 16 de ese mes. Seguidamente,
fijamos un precio mínimo por noche de 100 y uno máximo de 150 dólares. Como nuestro cliente quiere una vivienda completa, escogemos la opción
*entire home/apt* y, por último, seleccionamos el distrito de Aigle.
            
Como vemos, seguimos teniendo muchas opciones, pero si hacemos click en la mayoría de ellas veremos que ya están ocupadas. Otra cosa que 
podríamos tener en cuenta es la preferencia del esquiador por alojarse en un lugar con buenas vistas. Haciendo un *scroll* por la tabla, o incluso
utilizando el cntrl+f, podemos buscar la palabra *view* o *views* en la columna 'nombre'. Con un poco de paciencia, 
encontramos un alojamiento que satisface todos los requisitos. 
            
Se trata del anuncio ***Beautiful Villars with a View***, que cuesta 130 dólares/noche y está libre en ese período. Podemos pinchar en el 
enlace y ver las fotos del anuncio. Como vemos, tiene vistas a las montañas nevadas y un balcón en el que el esquiador puede comer, tomar algo 
o descansar mientras disfruta del paisaje.""")

st.markdown("")
st.markdown("")
st.markdown("")

imagen = Image.open('img/alpes.jpg')
st.image(imagen, caption='Vista de los Alpes suízos.| Fuente: Wikimedia Commons. Url: https://commons.wikimedia.org/wiki/File:Genfersee_bei_montreux_2004_pischdi.JPG' , use_column_width=False, width=800, output_format='PNG')


st.markdown("")
st.markdown("")
st.markdown("")

st.markdown("""## **Caso número 2: La familia**""")

st.markdown("")
st.markdown("")
st.markdown("")

st.markdown("""El otro cliente es una familia (madre, padre e hijo pequeño) que desea pasar las vacaciones de navidad en Vaud y tienen pensado estar desde el 23 de diciembre
hasta el 3 de enero, fecha en la que regresarán a España para que su hijo pueda ver las cabalgatas de los Reyes Magos.
            
En este caso les interesa encontrar un alojamiento que tenga capacidad para tres ó más personas, que esté bien equipado (a poder
ser que sea una vivienda completa (*entired*)) y que esté en un distrito que dé al lago Leman para poder salir a pasear con el niño
por la orilla del lago.

Además, están dispuestos a pagar hasta 220 dólares por noche con tal de conseguir un sitio de estas características.
            
Los distritos que dan a este lago son Nyon, Morges, Lausanne, Ouest Iausannois, Lavaux-Oron, Riviera y Aigle. Podemos
empezar buscando en el distrto de Lavoux-Oron, que es pequeño, tiene bastante costa en el lago y una terminal de ferry en Cully.""")


imagen = Image.open('img/cully.jpg')
st.image(imagen, caption='Viñedos de la villa de Cully y lago Leman.| Fuente: Wikimedia Commons. Url: https://commons.wikimedia.org/wiki/File:Vi%C3%B1edos_Cully-Lavaux_%284%29.jpg', use_column_width=False, width=800, output_format='PNG')

st.markdown("""Filtramos por período de fechas, por el rango de precio, por distrito y elegimos un alojamiento de tipo completo. En el tipo de
propiedad, podemos probar con *entire home* como primera opción. Seleccionamos esta opción y vemos que sólo uno de los anuncios
tiene disponibilidad para nuestras fechas. 
            
El anuncio es ***Lake Geneva, the Lavaux and the Swiss Alps***, que tiene un precio de 153 dólares. El hecho de que el nombre aluda al
lago puede ser indicativo de que el alojamiento tenga vistas a él, y también a las montañas. Visitamos la url del anuncio
y vemos que, efectivamente, se encuentra muy cerca de la orilla y ofrece también vistas a las montañas que hay del otro lado del lago.
            
Además, tiene habitaciones, camas y baños suficientes para la familia, y la cocina y el baño están bien equipados.""")




st.markdown("")
st.markdown("")
st.markdown("")

st.markdown("""## **Caso número 3: Mi viaje con un grupo de amigos**""")

st.markdown("""Y ahora llega la última y **más importante búsqueda**: la de un alojamiento para pasar la próxima semana santa con mis amigos. Necesitaremos
un sitio que tenga como mínimo: 6 camas, 2 baños, y 3 habitaciones (ya que seremos 6 personas y podemos aceptar el compartir baño con otros dos).
Como podemos ver, de los más de 5000 anuncios, **apenas** hay unos **350** que cuentan con capacidad para seis o más personas.""")            

st.markdown("")
st.markdown("")
st.subheader('Alojamientos con 6 camas o más')

data = pd.read_csv('tablas/listings_seis_amigos.csv')
st.dataframe(data)

st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")
            
st.markdown("""El otro principal **factor limitante** va a ser el económico, ya que no estamos por la labor de gastar más de **200 euros** por noche. 
            
El primer paso es elegir la zona más barata de Vaud, y esa no es otra que la del distrito **Gross-de-Vaud**, que se encuentra en el interior 
y no da a ningún lago.
            
Para esta búsqueda, se **cambiará la estrategia** seguida en los dos ejemplos anteriores, pues tenemos que cerciorarnos de que el alojamiento
dispone del número de habitaciones, baños y camas necesarias, por lo que generamos tres gráficas de líneas que enfrenten estas tres
variables con el precio. De esta forma, cuando seleccionemos un nombre de anuncio, veremos que se generan puntos en estas gráficas que 
nos indican el número de habitaciones, baños y camas que tienen. El precio lo iremos viendo con un **medidor**.
            
Con un poco de paciencia, llegamos a un anuncio que pasa por todos los filtros:
        
- ***Maison de campagne chaleuresse et chats adorables***. Como vemos, se trata de una casa de campo que cuenta con:
            
    - 3 habitaciones
    - 2 baños
    - ¡7 camas!
            
Sólo nos costaría 180 dólares por noche (es decir, a treinta dólares por cabeza) y además (y esto es lo más importante), ¡tiene unos
gatos adorables! (como se puede ver en las fotos del anuncio).
            
Se trata, pues, de una casa de campo de aspecto muy rustico (chimenea, tablones de madera, etc.) que es ideal para viajes en grupos de amigos.""")
st.markdown("")
st.markdown("")

imagen = Image.open('img/chimenea.jpg')
st.image(imagen, caption='Chimenea de leña.| Fuente: pxheres. Url: https://pxhere.com/es/photo/593974', use_column_width=False, width=800, output_format='PNG')

st.markdown("")
st.markdown("")




st.markdown("""## Cierre del informe""")

st.markdown("")
st.markdown("")
st.markdown("")

st.markdown("""Hecha la búsqueda de nuestro alojamiento, toca enseñárselo a mis amigos. Como era lógico, les ha parecido un lugar genial,
y me han felicitado por mi trabajo (el tema de los gatos ha jugado a mi favor, todo hay que decirlo).
             
Viendo la nota de la reseña del alojamiento, que es de un **4.85**, se trata de una puntuación **por encima de la media** para una casa que
está en el rango de los precios intermedios (allí la media es de 4.75), a lo que se le suma el hecho de que el anfitrión tiene la
categoría de *superhost*.
            
Sin duda, creo que he dado con el sitio idóneo y creo que me merezco que el resto del viaje lo planifiquen ellos.""")

