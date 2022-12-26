

import streamlit as st
from segment import process

st.title('BTC')

test = st.file_uploader("Choose a CSV file", type=['csv'])
file_r = test.read()

process(file_r)







