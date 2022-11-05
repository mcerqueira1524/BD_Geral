#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import streamlit.components.v1 as components
import numpy as np
import streamlit as st


# In[ ]:


@st.experimental_memo

def importar_base():
    sts = pd.read_excel('I:/PROJETOS/ENSINO_SUPERIOR/3. Base de Dados/2022/Status/2022_Status_Universitarios.xlsm', sheet_name='BD_Geral',skiprows=6)
    ra = pd.read_excel('I:/PROJETOS/ENSINO_SUPERIOR/3. Base de Dados/2022/RA/Acomp RA/RA_2022.1/Acomp_RA_2022_1.xlsm', sheet_name='Leitura_2022.1', skiprows=3)
    empregabilidade =  pd.read_excel('I:/PROJETOS/ENSINO_SUPERIOR/9. Relações Institucionais/Indicadores/2022/2022_Painel_Empregabilidade_VP.xlsm', sheet_name='BD_Geral', skiprows=3)
    return sts,ra,empregabilidade

sts,ra,empregabilidade=importar_base()


# In[3]:


juncao = pd.merge(sts,ra, on=['ID'], how="left")

# In[5]:


bd_completo = pd.merge(juncao, empregabilidade, left_on=['ID'], right_on=['RA'], how='left')


# In[6]

filtro = bd_completo.columns

# In[7]

st.sidebar.markdown('Indice:')
st.sidebar.markdown('1 - Gênero')
st.sidebar.markdown('2 - Raça')
    
# In[8]:

genero = st.multiselect(
          '1 - Gênero:',
          options= bd_completo['Gênero'].dropna().unique(),
          default= bd_completo['Gênero'].dropna().unique())
    
raca = st.multiselect(
          ' 2 -Raça:',
          options= bd_completo['Cor_Raça'].dropna().unique(),
          default= bd_completo['Cor_Raça'].dropna().unique())

colunas = st.multiselect(
          'Colunas:',
          options= bd_completo.columns.values.tolist())


# In[10]:


df_filtro = bd_completo.query('Gênero == @genero & Cor_Raça == @raca')

# In[11]:

st.dataframe(df_filtro[colunas])




