import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Simulador de Cookies", layout="centered")

st.title("🍪 Este site usa cookies")
st.write("Usamos cookies para melhorar sua experiência. Você aceita?")

col1, col2 = st.columns(2)

if "status" not in st.session_state:
    st.session_state.status = None

def registrar_consentimento(status):
    dados = {
        "timestamp": datetime.now().isoformat(),
        "resposta": status
    }
    try:
        df = pd.read_csv("consent_log.csv")
        df = df.append(dados, ignore_index=True)
    except FileNotFoundError:
        df = pd.DataFrame([dados])

    df.to_csv("consent_log.csv", index=False)
    st.session_state.status = status

with col1:
    if st.button("Aceito"):
        registrar_consentimento("Aceito")

with col2:
    if st.button("Recusar"):
        registrar_consentimento("Recusado")

if st.session_state.status:
    st.success(f"Você selecionou: {st.session_state.status}")