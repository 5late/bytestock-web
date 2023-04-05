# Description: About page

import streamlit as st 
 
with open('./pages/about.md') as file: # Reads data from the about.md file
    lines = file.readlines() 
 
    for line in lines: 
        st.write(line) 