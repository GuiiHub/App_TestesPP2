import streamlit as st

st.title("Teste de aplicação Streamlit")
st.subheader("Desenvolvido via VS Code")

nome = st.text_input("Digite seu nome:")

if nome:
    st.success(f"Olá, {nome}, seja bem-vindo(a)! O app Streamlit está funcionando perfeitamente.")

    import pandas as pd

    data = "data\info.csv"

    df = pd.read_csv(data)
    st.dataframe(df)
