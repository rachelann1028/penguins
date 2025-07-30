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
    # Sample input dataframe (replace with actual user input logic)
input_df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv")
input_df = input_df.dropna()

with st.expander("Input data"):
    st.write("**Input data**")
    st.dataframe(input_df)

    # Extract target column separately
    y_raw = input_df['species']

    # Remove target column from input features
    input_penguins = input_df.drop('species', axis=1)

    st.write("**Combined data**")
    st.dataframe(input_penguins)

# One-hot encoding for features
encode = ['island', 'sex']
df_penguins = pd.get_dummies(input_penguins, columns=encode, prefix=encode)

# Prepare input row and feature matrix
X = df_penguins[1:]
input_row = df_penguins[:1]

# Encode target labels
target_mapper = {
    'Adelie': 0,
    'Chinstrap': 1,
    'Gentoo': 2
}
def target_encode(val):
    return target_mapper[val]

y = y_raw.apply(target_encode)

st.write("**Encoded Features**")
st.dataframe(df_penguins)

st.write("**Encoded Labels**")
st.write(y.head())

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