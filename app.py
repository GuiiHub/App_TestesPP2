import streamlit as st

st.title("Teste Streamlit - Guilherme Queiroz")
st.subheader("Exemplo simples de aplicação web usando Streamlit.")

nome = st.text_input("Digite seu nome/usuário:")

if nome:
    st.success(f"Olá, {nome}! Seja bem-vindo(a)! O app Streamlit está funcionando perfeitamente.")
    st.subheader("Exibindo dataframe em formato CSV")
    import pandas as pd

    data = r"data/info.csv"

    df = pd.read_csv(data, sep=",")
    st.dataframe(df)


