import streamlit as st
st.set_page_config(page_title="Cartão Dia das Mães", page_icon= "💖")
st.title("🌹 Feliz dia das Mães! 🌹")
nome = st.text_input("Digite o nome da sua Mãe:")

if st.button("Mostrar Mensagem"):
    st.success(nome, "você é uma mãe incríve! Te amo muito")
else:
    st.warning("Digite o nome da sua mãe para ver a mensagem")