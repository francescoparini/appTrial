import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

st.title("Simulatore di Funzione")

# Parametri
a = st.slider("Scegli il coefficiente a", -10.0, 10.0, 1.0)
b = st.slider("Scegli il coefficiente b", -10.0, 10.0, 0.0)

# Costruzione dati
x = np.linspace(-10, 10, 400)
y = a * x + b

# Grafico
fig, ax = plt.subplots()
ax.plot(x, y, label=f"y = {a}x + {b}")
ax.axhline(0, color='gray', lw=0.5)
ax.axvline(0, color='gray', lw=0.5)
ax.legend()
st.pyplot(fig)

# Esporta CSV
df = pd.DataFrame({'x': x, 'y': y})
csv = df.to_csv(index=False).encode('utf-8')
st.download_button("📥 Scarica i dati", csv, "dati.csv", "text/csv")
