import streamlit as st

st.title("Minha Primeira Aplicação Streamlit")
st.subheader("Desenvolvida no VS Code")

# Componente interativo
nome = st.text_input("Digite seu nome:")

if nome:
    st.success(f"Olá, {nome}! Seu ambiente Streamlit está funcionando perfeitamente.")