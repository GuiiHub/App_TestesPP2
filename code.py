import streamlit as st

st.title("Teste de aplicação Streamlit")
st.subheader("Desenvolvida no VS Code")

nome = st.text_input("Digite seu nome:")

if nome:
    st.success(f"Olá, {nome}, seja bem-vindo(a)! O ambiente Streamlit está funcionando perfeitamente.")