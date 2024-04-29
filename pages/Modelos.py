import numpy as np 
import pandas as pd 
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor

st.title('Modelos')

"""Antes de meter los datos al modelo fue necesario hacer una transformación de estos
para reducir el peso de los outliers, en nuestro caso se utilizó una transformación logarítmica aplicando 
el logaritmo a cada uno de los datos."""

"""Los modelos que elegimos para hacer predicciones fueron: **Regresión Lineal**, **Ridge**, **Lasso**
**Árboles de decisión** y **Random Forest.**"""

st.header('Entrenamiento de los modelos')

#with st.echo():