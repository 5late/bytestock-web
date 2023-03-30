import streamlit as st 

with open('./pages/about.md') as file: 
    lines = file.readlines() 

    for line in lines: 
        st.write(line) 