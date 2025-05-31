import streamlit as st
import pandas as pd
import numpy as np

st.title("📈 Analisi Dati")

# Dati casuali
df = pd.DataFrame({
    "Anno": np.arange(2015, 2025),
    "Vendite": np.random.randint(1000, 5000, 10)
})

st.dataframe(df.style.highlight_max(axis=0, color='#D1E7DD'))

# Plot
st.bar_chart(df.set_index("Anno"))
