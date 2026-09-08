import streamlit as st
from google import genai

# Nastavení stránky
st.set_page_config(page_title="Majk - KOLIRA", page_icon="🪵", layout="centered")

st.title("🪵 Majk – Asistent pro KOLIRA")
st.caption("E-shop ramovaniobrazu.cz | Rámy na míru, lišty a data")

# Inicializace klienta pro Gemini (využívá tvůj ověřený projekt a globální endpoint)
client = genai.Client(
    vertexai=True, 
    project="619691121535", 
    location="global"
)

# Systémové instrukce, aby Majk věděl, co má dělat
SYSTEM_INSTRUCTION = """
Jsi Majk, virtuální asistent pro firmu KOLIRA a e-shop ramovaniobrazu.cz.
Pomáháš s vytvářením popisků pro obrazové rámy, lišty, pasparty, skla (Artglass, Museum Glass) a zpracováním dat.
Komunikuješ česky, jsi věcný, vstřícný a rozumíš oboru rámování na míru.
"""

# Paměť chatu v rámci relace
if "messages" not in st.session_state:
    st.session_state.messages = []

# Vypsání předchozích zpráv
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Vstup od uživatele
if prompt := st.chat_input("Napište zprávu pro Majka..."):
    # Uložení a zobrazení uživatelské zprávy
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generování odpovědi od Majka
    with st.chat_message("assistant"):
        with st.spinner("Majk přemýšlí..."):
            try:
                response = client.models.generate_content(
                    model="gemini-3.5-flash",
                    contents=prompt,
                    config={
                        'system_instruction': SYSTEM_INSTRUCTION,
                        'temperature': 0.7,
                    }
                )
                answer = response.text
            except Exception as e:
                answer = f"Omlouvám se, něco se pokazilo: {e}"
            
            st.markdown(answer)
            
    # Uložení odpovědi do historiky
    st.session_state.messages.append({"role": "assistant", "content": answer})