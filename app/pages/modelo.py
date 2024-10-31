import streamlit as st
import pandas as pd
import numpy as np
from pycaret.classification import load_model, predict_model
import os
import io
from PIL import Image

st.title('Limpieza de datos')