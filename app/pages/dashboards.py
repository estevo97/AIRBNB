import streamlit as st
import pandas as pd
import numpy as np
from pycaret.classification import load_model, predict_model
import os
import io
from PIL import Image


st.title("Dashboards")

st.markdown("""### Precios medios""")

# URL del dashboard de Power BI
power_bi_url = "https://app.powerbi.com/view?r=eyJrIjoiZDg5MWM1MDgtMTFiZS00ZDcxLWE4YjUtZjYwNWIwOGZjODE0IiwidCI6IjhhZWJkZGI2LTM0MTgtNDNhMS1hMjU1LWI5NjQxODZlY2M2NCIsImMiOjl9"  # Reemplaza con tu URL de Power BI

# Incrustar el iframe en Streamlit
st.components.v1.iframe(power_bi_url, width=1000, height=600)

