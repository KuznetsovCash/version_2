

import streamlit as st
from segment import process

st.title('BTC')

file = st.file_uploader('Load')

process(file)


