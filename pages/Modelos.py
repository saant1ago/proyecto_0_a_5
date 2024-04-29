import numpy as np 
import pandas as pd 
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
st.title('Modelos')

df_tabasco=pd.read_csv('modelos/modelos_tabasco.csv')
df_coahuila=pd.read_csv('modelos/modelo_coahuila.csv')
df_qro=pd.read_csv('modelos/modelos_qro.csv')
df_coahuila.drop('Unnamed: 0',axis=1,inplace=True)

"""Antes de meter los datos al modelo fue necesario hacer una transformación de estos
para reducir el peso de los outliers, en nuestro caso se utilizó una transformación logarítmica aplicando 
el logaritmo a cada uno de los datos."""

"""Los modelos que elegimos para hacer predicciones fueron: **Regresión Lineal**, **Ridge**, **Lasso**
**Árboles de decisión** y **Random Forest.**"""

st.header('Entrenamiento de los modelos')

#def log_transform(column):
#    return column.apply(lambda x: np.log(x+1))

#df_qro=df_qro.apply(log_transform)
#df_coahuila=df_coahuila.apply(log_transform)
#df_tabasco=df_tabasco.apply(log_transform)

option = st.selectbox('Selecciona el estado',('Querétaro', 'Tabasco', 'Coahuila'),index=None,placeholder='Selecciona el estado')

train=0

if option == 'Querétaro':
    option = df_qro
    option
    max=7
    n_est=20
elif option == 'Tabasco':
    option = df_tabasco
    option
    max=7
    n_est=50
elif option == 'Coahuila':
    option = df_coahuila
    option
    max=15
    n_est=120

if option is not None:
    train=st.slider('Selecciona el porcentaje de entrenamiento',0,99)
    
if train is not 0:

    with st.echo():
        X=option.drop('Poblacion de 0 a 5', axis=1)
        y=option['Poblacion de 0 a 5']
        X_train,X_test,y_train,y_test=train_test_split(X,y,train_size=(train/100),random_state=3)
        model = RandomForestRegressor(n_estimators = n_est, max_depth = max)
        model.fit(X_train,y_train)

    st.subheader('Evaluación del modelo')


    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test,y_pred)
    Resultados=pd.DataFrame([y_pred,y_test]).T
    Resultados.columns=['y_test','y_pred']

    col1,col2 = st.columns(2)

    with col1:
        st.write('Tabla de test vs predicciones')
        st.write(Resultados)
    with col2:
        'Métricas del modelo'
        st.write('Tamaño del entrenamiento',X_train.shape[0])
        st.write('Error medio cuadrado', mse)
        st.write('R^2: ',r2)
    
        