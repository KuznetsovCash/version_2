

import streamlit as st
from segment import process
import pandas as pd

st.title('BTC')

test = st.file_uploader("Choose a CSV file", type=['csv'])
data = pd.read_csv(test)

process(data)







