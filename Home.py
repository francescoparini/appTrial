import streamlit as st

st.set_page_config(page_title="Dashboard", page_icon="📊", layout="centered")

st.markdown(
    "<h1 style='color:#4CAF50;'>📊 Benvenuto nella Dashboard</h1>", unsafe_allow_html=True
)
st.write("Usa il menu a sinistra per navigare tra le sezioni dell’app.")
st.info("Hai domande? Scrivici!")
