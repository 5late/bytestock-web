import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.set_page_config(initial_sidebar_state='collapsed')

logo = Image.open('pics/bytestock-logo.png')
st.image(logo)

chart_data = pd.DataFrame(np.random.randn(20,3), columns = ['a', 'b', 'c'])

st.line_chart(chart_data)

