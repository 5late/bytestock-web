# Description: This file is used to display the live crypto prices on the home page of the website.

import streamlit as st
import sys 

sys.path.append('./bytestock-core-public')

from data import Data

st.set_page_config(layout="wide")  # Set the page layout to wide

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
cols = [col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12, col13, col14, col15, col16, col17, col18] # Create a list of the columns


info = []

with open('./pages/crypto.txt', 'r') as f:
    lines = f.readlines()

for i in range(18): # Loop through the list of stocks
    stock = lines[i].rstrip()

    get_Data = Data(stock, 1) # Get the data for the stock

    info.append(get_Data.getRealTimeOCHL()) # Get the real time data for the stock
    rt_previous_close, rt_open, rt_current, rt_high, rt_low, rt_change, rt_change_percent = info[i]

    cols[i].metric(stock, f"${round(rt_current, 2)}", f"{round(rt_change_percent, 2)}%") # Display the data in the columns
