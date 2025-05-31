import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("🧪 Simulatore")

# Parametri input
mean = st.slider("Media", -10.0, 10.0, 0.0)
std = st.slider("Deviazione standard", 0.1, 5.0, 1.0)

data = np.random.normal(mean, std, 1000)

# Istogramma
fig, ax = plt.subplots()
ax.hist(data, bins=30, color="#FF6B6B", edgecolor="white")
ax.set_title("Distribuzione simulata")
st.pyplot(fig)
