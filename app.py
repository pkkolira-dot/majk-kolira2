from google import genai
import streamlit as st

# Načtení API klíče ze Streamlit Secrets
api_key = st.secrets.get("GEMINI_API_KEY")

# Inicializace klienta pomocí API klíče
if api_key:
    client = genai.Client(api_key=api_key)
else:
    client = genai.Client()

# Nastavení stránky
st.set_page_config(page_title="Majk - KOLIRA", page_icon="🪵", layout="centered")

st.title("🪵 Majk - Asistent pro KOLIRA")
st.caption("E-shop ramovaniobrazu.cz | Rámy na míru, lišty a data")
