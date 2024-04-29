import numpy as np 
import pandas as pd 
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

df_tabasco=pd.read_csv('limpiezacsvs/tabasco_final.csv')
df_coahuila=pd.read_csv('limpiezacsvs/coa_final.csv')
df_qro=pd.read_csv('limpiezacsvs/qro_final.csv')
df_qro=df_qro.drop('Unnamed: 0',axis=1)
df_qro.drop(['ENTIDAD','NOM_ENT','MUN','LOC','NOM_LOC','AGEB'],axis=1,inplace=True)
df_coahuila.drop(['ENTIDAD','NOM_ENT','MUN','LOC','NOM_LOC','AGEB'],axis=1,inplace=True)
df_tabasco.drop(['ENTIDAD','NOM_ENT','MUN','LOC','NOM_LOC','AGEB','MZA'],axis=1,inplace=True)
df_coahuila=df_coahuila.drop('Unnamed: 0',axis=1)

st.title('Exploración de los datos')

""" Luego de haber llevado a cabo una limpieza exitosa de los datos, se realizó una 
exploración de estos para saber más acerca de que es lo estos datos nos pueden decir
que todavía no hayamos visto."""

option = st.selectbox('Selecciona el estado',('Querétaro', 'Tabasco', 'Coahuila'),index=None,placeholder='Selecciona el estado')

if option is not None:
    radio=st.radio('Elige que quieres ver',('Medidas de dispersión y tendencia central','Boxplots','Correlaciones'),index=None)

if option == 'Tabasco' and radio == 'Medidas de dispersión y tendencia central':
   st.write(df_tabasco.describe())
elif option == 'Querétaro' and radio == 'Medidas de dispersión y tendencia central':
   st.write(df_qro.describe())
elif option == 'Coahuila' and radio == 'Medidas de dispersión y tendencia central':
   st.write(df_coahuila.describe())
elif option == 'Tabasco' and radio == 'Boxplots':
   df=df_tabasco.copy()
   fig, ax = plt.subplots()
   ax=sns.boxplot(data=df)
   ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
   st.pyplot(fig)
elif option == 'Querétaro' and radio == 'Boxplots':
   df=df_qro.copy()
   fig, ax = plt.subplots()
   ax=sns.boxplot(data=df)
   ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
   st.pyplot(fig)
elif option == 'Coahuila' and radio == 'Boxplots':
   df=df_coahuila.copy()
   fig, ax = plt.subplots()
   ax=sns.boxplot(data=df)
   ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
   st.pyplot(fig)
elif option == 'Tabasco' and radio == 'Correlaciones':
   df_corr=df_tabasco.drop('NOM_MUN',axis=1).corr()
   fig, ax = plt.subplots()
   sns.heatmap(data=df_corr,annot=True,ax=ax,cmap='rocket_r')
   st.pyplot(fig)
elif option == 'Querétaro' and radio == 'Correlaciones':
   df_corr=df_qro.drop('NOM_MUN',axis=1).corr()
   fig, ax = plt.subplots()
   sns.heatmap(data=df_corr,annot=True,ax=ax,cmap='rocket_r')
   st.pyplot(fig)
elif option == 'Coahuila' and radio == 'Correlaciones':
   df_corr=df_coahuila.drop('NOM_MUN',axis=1).corr()
   fig, ax = plt.subplots()
   sns.heatmap(data=df_corr,annot=True,ax=ax,cmap='rocket_r')
   st.pyplot(fig)
