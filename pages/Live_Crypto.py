import streamlit as st 
import sys 
sys.path.append('../bytestock-core') 

import data 

st.set_page_config(layout="wide") 

col1, col2, col3, col4, col5, col6 = st.columns(6) 
st.text("") 
st.text("") 
st.text("") 
st.text("") 
st.text("") 
col7, col8, col9, col10, col11, col12 = st.columns(6)
st.text("") 
st.text("") 
st.text("") 
st.text("") 
st.text("") 
col13, col14, col15, col16, col17, col18 = st.columns(6)
cols = [col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12, col13, col14, col15, col16, col17, col18]
 
 
info = [] 
 
with open('./pages/crypto.txt', 'r') as f: 
    lines = f.readlines() 

for i in range(18): 
    stock = lines[i].rstrip() 

    info.append(data.getRealTimeOCHL(stock, 1)) 
    rt_previous_close, rt_open, rt_current, rt_high, rt_low, rt_change, rt_change_percent = info[i] 
 
    cols[i].metric(stock, f"${round(rt_current, 2)}", f"{round(rt_change_percent, 2)}%") 
