import streamlit as st

st.title("Teste Streamlit")
st.subheader("Exemplo simples de aplicação web usando Streamlit.")

nome = st.text_input("Digite seu nome:")

if nome:
    st.success(f"Olá, {nome}, seja bem-vindo(a)! O app Streamlit está funcionando perfeitamente.")


