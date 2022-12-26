

import streamlit as st
from segment import process
import pandas as pd

st.title('BTC')

test = st.file_uploader("Choose a CSV file", type=['csv'])
if not test is None: 
       data = pd.read_csv(test)   
       result = process(data)
       st.write(result)





