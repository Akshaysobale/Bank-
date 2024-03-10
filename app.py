import streamlit as st 
import numpy as np
import pandas as pd
import pickle
import sklearn
from PIL import Image

#loading model
model = pickle.load(open(r'C:\Users\CSC\Desktop\jup\Excelr Projects\Project 4\model.sav','rb'))

#PAge setting
st.set_page_config(layout='wide')

#Title
st.title('BANKRUPTCY PREDICTION')

#Image
image = Image.open('IMG.jpeg')
st.image(image, '',width=500)

#Sidebar
st.sidebar.header('Financila Data of the Organizarion')

# FUNCTION
def input_index():
  d1 = st.sidebar.slider('Cash/Current Liability', -50,50,5 )
  d2 = st.sidebar.slider('Fixed Assets to Asset', -45,102,5 )
  d3 = st.sidebar.slider('Net Value Growth Rate', -30,70,5 )
  d4 = st.sidebar.slider('Fixed Assets Turnover Frequency', -30,30,5)
  d5 = st.sidebar.slider('Revenue per person', -20,125,5)
  d6 = st.sidebar.slider('Total assets to GNP price', -22,30,5)
  d7 = st.sidebar.slider('Quick Ratio', -75,80,5)
  d8 = st.sidebar.slider('Quick Asset Turnover Rate', -45,55,5)
  d9 = st.sidebar.slider('Total debt/Total net worth', -30,82,5)
  d10 = st.sidebar.slider('Total Asset Growth Rate', -20,25,2)
  d11 = st.sidebar.slider('Research and development expense rate', -20,30,3)
  d12 = st.sidebar.slider('Current Asset Turnover Rate', -15,40,5)
  d13 = st.sidebar.slider('Operating Expense Rate', -22,25,3)
  d14 = st.sidebar.slider('Cash Turnover Rate', -30,50,5)
  d15 = st.sidebar.slider('Allocation rate per person', -35,65,5)
  d16 = st.sidebar.slider('Interest-bearing debt interest rate', -15,40,3)
  d17 = st.sidebar.slider('Inventory Turnover Rate (times)', -20,32,3)
  d18 = st.sidebar.slider('Long-term Liability to Current Assets', -18,35,3)
  d19 = st.sidebar.slider('Average Collection Days', -25,32,3)
  d20 = st.sidebar.slider('Quick Assets/Current Liability', -25,30,3)
  d21 = st.sidebar.slider('Accounts Receivable Turnover', -30,45,5)
  d22 = st.sidebar.slider('Revenue Per Share', -15,20,2)
  d23 = st.sidebar.slider('Current Ratio', -18,22,2)
  d24 = st.sidebar.slider('Inventory/Current Liability', -22,38,3)
  d25 = st.sidebar.slider('Liability-Assets Flag', -22,32,3)



  input_data = {
      'P1':d1,
      'P2':d2,
      'P3':d3,
      'P4':d4,
      'P5':d5,
      'P6':d6,
      'P7':d7,
      'P8':d8,
      'P9':d9,
      'P10':d10,
      'P11':d11,
      'P12':d12,
      'P13':d13,
      'P14':d14,
      'P15':d15,
      'P16':d16,
      'P17':d17,
      'P18':d18,
      'P19':d19,
      'P20':d20,
      'P21':d21,
      'P22':d22,
      'P23':d23,
      'P24':d24,
      'P25':d25,
  }
  dev_data = pd.DataFrame(input_data, index=[0])
  return dev_data

#Model
input_data_print = input_index()
st.header('Selected Financial data:')
st.write(input_data_print)

dev_model = model.predict(input_data_print)[0]
st.subheader('Bankruptcy Status of the organization is:')

if st.button('Run Analysis'):
    if dev_model == 0:
        st.subheader("Solvent")
    elif dev_model ==1:
        st.subheader("Bankrupt")



