import numpy as np 
import pandas as pd 
import streamlit as st
import seaborn as sns

st.title('Limpieza de Datos')

st.header('Lectura de datos')

'''Como primer paso fue necesaria la lectura de nuestros datos. Esto se realizó mediante el notebook
poprocionado por el INEGI, el cual nos ayudó a descargar los datos de los estados necesarios, los cuales en este 
caso fueron **Querétaro**, **Tabasco** y **Coahuila**.'''

'''Primero fue necesario conocer nuestros datos; el tipo de estos, su longitud, valores faltantes, etc. Con ello nos
ibamos a poder dar una idea de como empezar la limpieza de los datos.'''

df_qro = pd.read_csv('limpiezacsvs/queretaro_raw.csv')
df_taba = pd.read_csv('limpiezacsvs/datos_raw_tabasco.csv')
df_coa= pd.read_csv('limpiezacsvs/coa_final.csv')
expander_1 = st.expander('Querétaro')
expander_1.table(df_qro.head())
expander_2 = st.expander('Tabasco')
expander_2.table(df_taba.head())
expander_3 = st.expander('Coahuila')
expander_3.table(df_coa.head())


st.subheader('Limpieza de los datos')



tab_qro,tab_tab,tab_coa = st.tabs(['Querétaro','Tabasco','Coahuila'])

if 'limpieza' not in st.session_state:
    st.session_state.limpieza=False

def click_button():
    st.session_state.limpieza= not st.session_state.limpieza




with tab_qro:


    if st.session_state.limpieza == False:
        st.subheader('Datos antes de la limpieza')
        df_qro_raw=pd.read_csv('limpiezacsvs/queretaro_raw.csv')
        df_qro_raw
        st.write('Dimensiones del data set:',df_qro_raw.shape)
        st.write('Datos faltantes : ', (df_qro_raw=='*').sum().sum())   
        st.button('Limpiar', on_click=click_button)
    else:
        st.subheader('Datos limpios')
        df_qro_raw=pd.read_csv('limpiezacsvs/qro_final.csv')
        df_qro_raw=df_qro_raw.drop('Unnamed: 0',axis=1)
        df_qro_raw
        st.write('Dimensiones del data set:',df_qro_raw.shape)
        st.write('Datos faltantes : ', (df_qro_raw=='*').sum().sum())
        st.button('Revertir', on_click=click_button)
        

with tab_tab:

    if st.session_state.limpieza == False:
        st.subheader('Datos antes de la limpieza')
        df_qro_raw=pd.read_csv('limpiezacsvs/datos_raw_tabasco.csv')
        df_qro_raw
        st.write('Dimensiones del data set:',df_qro_raw.shape)
        st.write('Datos faltantes : ', (df_qro_raw=='*').sum().sum())
        st.button('Limpiar', on_click=click_button,key='tabasco_1')
    else:
        st.subheader('Datos limpios')
        df_qro_raw=pd.read_csv('limpiezacsvs/tabasco_final.csv')
        df_qro_raw
        st.write('Dimensiones del data set:',df_qro_raw.shape)
        st.write('Datos faltantes : ', ((df_qro_raw=='*').sum().sum()))
        st.button('Revertir', on_click=click_button,key='tabasco_2')

with tab_coa:

    if st.session_state.limpieza == False:
        st.subheader('Datos antes de la limpieza')
        df_qro_raw=pd.read_csv('limpiezacsvs/coahuila_raw.csv')
        df_qro_raw
        st.write('Dimensiones del data set:',df_qro_raw.shape)
        st.write('Datos faltantes : ', (df_qro_raw=='*').sum().sum())
        st.button('Limpiar', on_click=click_button,key='coa_1')
    else:
        st.subheader('Datos limpios')
        df_qro_raw=pd.read_csv('limpiezacsvs/coa_final.csv')
        df_qro_raw=df_qro_raw.drop('Unnamed: 0',axis=1)
        df_qro_raw
        st.write('Dimensiones del data set:',df_qro_raw.shape)
        st.write('Datos faltantes : ', (df_qro_raw=='*').sum().sum())
        st.button('Revertir', on_click=click_button,key='coa_2')
    
    

    
