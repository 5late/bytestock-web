#Description: Main file for the ByteStock web app. This file contains the main code for the web app.

import streamlit as st 
import altair as alt
import pandas as pd
import numpy as np
from PIL import Image
import time
import sys
sys.path.append('bytestock-core-public') # Imports the bytestock-core-public folder

import data
import main


st.set_page_config(initial_sidebar_state='collapsed') # Collapses the sidebar by default

logo = Image.open('pics/bytestock-logo.png') # Logo
st.image(logo)

stock = st.text_input('See data over a specified time period.', placeholder='Enter a stock ticker: (Ex. AAPL)', max_chars=5) # Stock ticker input

st.write('You selected: $' + stock) # Stock ticker output

days = st.number_input(label='Include graphs for requested time period.', min_value=1, max_value=2000, value=500, step=1, label_visibility='collapsed') # Number of days input

def chart(data, low, high, ticker): # Chart function
    hover = alt.selection_single(fields=["date"], nearest=True, on="mouseover", empty="none")

    lines = (alt.Chart(data, title=f"${ticker} Historical Price").mark_line().encode(x="date", y=alt.Y("price", scale=alt.Scale(domain=[low, high]))))

    # Draw points on the line, and highlight based on selection
    points = lines.transform_filter(hover).mark_circle(size=65)

    # Draw a rule at the location of the selection
    tooltips = (
        alt.Chart(data)
        .mark_rule()
        .encode(
            x="date",
            y="price",
            opacity=alt.condition(hover, alt.value(0.3), alt.value(0)),
            tooltip=[
                alt.Tooltip("date", title="Date"),
                alt.Tooltip("price", title="Price (USD)"),
            ]
        )
        .add_selection(hover)
    )
    return (lines + points + tooltips).interactive()

if st.button(label='Query'): # Query button
    open_days, daily_open, daily_close, daily_adj_close, daily_high, daily_low = data.getOCHLData(days, stock) # Gets data from data.py

    lowest_price = min(daily_close) - 3
    highest_price = max(daily_close) + 3

    chart_data = pd.DataFrame(list(zip(daily_close, open_days)), columns=['price', 'date']) # Dataframe for chart
    
    st.altair_chart(chart(chart_data, lowest_price, highest_price, stock.upper()), use_container_width = True)
    st.dataframe(chart_data, use_container_width = True)
