import streamlit as st

st.title("Benvenuto nella mia Web App")
st.write("Questa è la mia prima app creata con Streamlit!")
x = st.slider("Scegli un numero", 0, 100)
st.write(f"Hai scelto: {x}")
