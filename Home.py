import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.set_page_config(initial_sidebar_state='collapsed')

logo = Image.open('pics/bytestock-logo.png')
st.image(logo)

stock = st.text_input(label='See data over a specified time period.', placeholder='Enter a stock ticker: (Ex. AAPL)', max_chars=5)

st.write('You selected: $' + stock)