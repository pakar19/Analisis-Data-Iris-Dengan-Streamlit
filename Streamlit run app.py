# Import library
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

# Filter data berdasarkan input pengguna
filtered_data = data[data['species'].isin(species_filter)]

# Scatter plot
st.subheader("Visualisasi Data (Scatter Plot)")
st.write(f"Scatter plot untuk {x_axis} vs {y_axis} berdasarkan spesies yang dipilih:")
fig, ax = plt.subplots()
sns.scatterplot(data=filtered_data, x=x_axis, y=y_axis, hue="species", ax=ax, palette="viridis")
st.pyplot(fig)

# Correlation heatmap
st.subheader("Heatmap Korelasi")
st.write("Visualisasi korelasi antar fitur:")
fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(data.corr(), annot=True, cmap="coolwarm", ax=ax)
st.pyplot(fig)

# Additional insights
st.subheader("Analisis Tambahan")
st.write("""
- Dataset Iris memiliki 150 sampel yang terbagi menjadi tiga spesies: Setosa, Versicolor, dan Virginica.
- Scatter plot memungkinkan Anda untuk memahami distribusi data berdasarkan fitur yang dipilih.
- Heatmap menunjukkan tingkat hubungan (korelasi) antara berbagai fitur.
""")
