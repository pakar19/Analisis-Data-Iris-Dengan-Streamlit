# Import library
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title and description
st.title("Aplikasi Streamlit Sederhana")
st.write("""
Ini adalah contoh aplikasi Streamlit sederhana. Anda dapat memasukkan data, melihat tabel, dan memvisualisasikannya.
""")

# Input data
st.subheader("1. Input Data")
name = st.text_input("Masukkan nama Anda:")
age = st.number_input("Masukkan usia Anda:", min_value=1, max_value=100, step=1)
hobby = st.text_input("Masukkan hobi Anda:")

# Display user input
if st.button("Tampilkan Data"):
    st.write(f"**Nama:** {name}")
    st.write(f"**Usia:** {age} tahun")
    st.write(f"**Hobi:** {hobby}")

# Generate sample dataset
st.subheader("2. Dataset Contoh")
data = {
    "Nama": ["Alice", "Bob", "Charlie", "David"],
    "Usia": [25, 30, 35, 40],
    "Pekerjaan": ["Guru", "Dokter", "Insinyur", "Desainer"]
}
df = pd.DataFrame(data)
st.write("Berikut adalah dataset contoh:")
st.dataframe(df)

# Visualize data
st.subheader("3. Visualisasi Data")
chart_type = st.selectbox("Pilih jenis grafik:", ["Bar Chart", "Line Chart"])
if chart_type == "Bar Chart":
    fig, ax = plt.subplots()
    ax.bar(df["Nama"], df["Usia"], color="skyblue")
    ax.set_title("Usia Berdasarkan Nama")
    ax.set_xlabel("Nama")
    ax.set_ylabel("Usia")
    st.pyplot(fig)
elif chart_type == "Line Chart":
    fig, ax = plt.subplots()
    ax.plot(df["Nama"], df["Usia"], marker="o", linestyle="-", color="green")
    ax.set_title("Usia Berdasarkan Nama")
    ax.set_xlabel("Nama")
    ax.set_ylabel("Usia")
    st.pyplot(fig)

# Footer
st.write("---")
st.write("Dibuat menggunakan Streamlit. 😊")

