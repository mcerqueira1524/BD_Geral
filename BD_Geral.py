#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import streamlit.components.v1 as components
from PIL import Image
from functools import reduce
import io
from io import BytesIO
from pyxlsb import open_workbook as open_xlsb
from st_pages import Page, Section, add_page_title, show_pages
# In[ ]:


@st.experimental_memo

def importar_base():
    bd = st.file_uploader("Upload do arquivo XLSX", type="xlsx")
    return bd

sts,ra,empregabilidade=importar_base()


# In[3]:


#juncao = pd.merge(sts,ra, on=['ID'], how="left")
