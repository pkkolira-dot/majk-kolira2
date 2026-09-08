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

# Inicializace historie chatu
if "messages" not in st.session_state:
    st.session_state.messages = []

# Vypsání předchozích zpráv
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Vstup od uživatele
if prompt := st.chat_input("Napište zprávu pro Majka..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Odpověď od modelu Gemini
    with st.chat_message("assistant"):
        try:
          response = client.models.generate_content(
                model="gemini-3.6-flash",
                contents=prompt,
            )
            answer = response.text
            st.markdown(answer)
            st.session_state.messages.append({"role": "assistant", "content": answer})
        except Exception as e:
            error_msg = f"Omlouvám se, něco se pokazilo: {e}"
            st.error(error_msg)
