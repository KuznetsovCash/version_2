

import streamlit as st
from segment import process

st.title('BTC')

file = st.file_uploader('Load', type=['csv'])

if not file in None:
       result = process(file)


