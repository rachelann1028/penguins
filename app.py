import pandas as pd
import streamlit as st
import numpy as np
from sklearn.ensemble import RandomForestClassifier

st.title("Penguine species prediction")
st.info("This is end-to-end Machine Learning app")

with st.expander("Data"):
    pass

with st.expander("Data Visualization"):
    pass

with st.expander("Input Data"):
    pass

with st.expander("Data preparation"):
    pass

with st.sidebar:
    st.header("Input Variables")
    island = st.selectbox('Island',('Select island','Biscoe','Dream','Torgersen'))
    
