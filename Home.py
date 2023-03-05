import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import sys
sys.path.append('bytestock-core')

import data

st.set_page_config(initial_sidebar_state='collapsed')

logo = Image.open('pics/bytestock-logo.png')
st.image(logo)

stock = st.text_input(label='See data over a specified time period.', placeholder='Enter a stock ticker: (Ex. AAPL)', max_chars=5)

st.write('You selected: $' + stock)

days = st.number_input(label='Include graphs for requested time period.', min_value=1, max_value=250, value=3, step=1, label_visibility='collapsed')

if st.button(label='Query'):
    open_days, daily_open, daily_close, daily_high, daily_low = data.getOCHLData(stock, days)

    st.write('Open: ', str(daily_open))