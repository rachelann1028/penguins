import pandas as pd
import streamlit as st
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier

st.title("Penguine species prediction")
st.info("This is end-to-end Machine Learning app")

with st.expander("Data"):
    st.write("**Raw Data**")
    df = pd.read_csv ("https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv")
    df

    st.write("Input Variables")
    X_raw = df.drop('species', axis=1)
    X_raw
    
    st.write("Input Variables")
    y_raw = df.species
    y_raw

    st.write("Descriptive Statistics")
    des = df.describe()
    des
    st.write("Data info")
    info = df.info
    info


with st.expander("Data Visualization"):
    st.scatter_chart(data=df, x='bill_length_mm', y='body_mass_g', color = 'species')

    st.title("Boxplot Example")

    # Select boxplot variables
    x_axis = st.selectbox("species", df.select_dtypes(include='object').columns)
    y_axis = st.selectbox("body_mass_g", df.select_dtypes(include='number').columns)

    # Draw the boxplot
    fig, ax = plt.subplots()
    sns.boxplot(data=df, x=x_axis, y=y_axis, ax=ax)
    st.pyplot(fig)

with st.expander("Input Data"):
    pass

with st.expander("Data preparation"):
    pass



with st.sidebar:
    st.header("Input Variables")
    island = st.selectbox('Island',('Select island','Biscoe','Dream','Torgersen'))
    bill_length_mm = st.slider('Bill length (mm)',32.1,59.6,43.9)
    bill_depth_mm = st.slider('Bill depth (mm)',13.1,21.5,17.2)
    flipper_length_mm = st.slider('Flipper length (mm)',172.0,231.0,201.0)
    body_mass_g = st.slider('Body mass (g)',2700.0,6300.0,4207.0)
    gender = st.selectbox('Gender',('select gender','male','female'))

    data = {
        "island": island,
        "bill_length_mm": bill_length_mm,
        "bill_depth_mm": bill_depth_mm,
        "flipper_length_mm": flipper_length_mm,
        "body_mass_g": body_mass_g,
        "sex": gender
    }

    input_df = pd.DataFrame(data,index=[0])
    input_penguins = pd.concat([input_df, X_raw], axis=0)

with st.expander("Input data"):
    st.write("**Input data**")
    input_df

    st.write("**Combined data**")
    input_penguins
    
encode = ["island", "sex"]
df_penguins = pd.get_dummies(input_penguins, prefix = encode)

X = df_penguins[1:]
input_row = df_penguins[:1]

target_mapper = {
    'Adelie': 0,
    'Chinstrap': 1,
    'Gentoo': 2
}
def target_encode(val):
    return target_mapper[val]

y = y_raw.apply(target_encode)
