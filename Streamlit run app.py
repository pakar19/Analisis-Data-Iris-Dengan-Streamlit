# Import library
pip install streamlit pandas seaborn matplotlib scikit-learn
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Set title for the Streamlit app
st.title("Analisis Data Iris dengan Streamlit")

# Load dataset Iris
iris = load_iris()
data = pd.DataFrame(iris.data, columns=iris.feature_names)
data['species'] = iris.target
data['species'] = data['species'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})

# Display dataset
st.subheader("Dataset Iris")
st.write("Berikut adalah dataset Iris yang digunakan dalam analisis:")
st.dataframe(data)

# Display basic statistics
st.subheader("Statistik Deskriptif")
st.write("Berikut adalah ringkasan statistik dari dataset:")
st.write(data.describe())

# Sidebar for user input
st.sidebar.title("Pengaturan Visualisasi")
x_axis = st.sidebar.selectbox("Pilih fitur untuk sumbu X:", data.columns[:-1])
y_axis = st.sidebar.selectbox("Pilih fitur untuk sumbu Y:", data.columns[:-1])
species_filter = st.sidebar.multiselect("Filter spesies:", options=data['species'].unique(), default=data['species'].unique())


