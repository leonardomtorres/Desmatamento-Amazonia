import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dashboard Amazônia", layout="wide")

st.title("📊 Monitoramento Amazônia")

# Tente carregar o arquivo
try:
    df = pd.read_csv("amazonia_tratado.csv")
    
    # KPIs
    total_desmatado = df["Desmatado 2022"].sum()
    st.metric("Total Desmatado 2022", f"{total_desmatado:,.2f} km²")

    # Gráfico simples para testar
    fig = px.bar(df.groupby("Estado")["Desmatado 2022"].sum().reset_index(), 
                 x="Estado", y="Desmatado 2022", title="Desmatamento por Estado")
    
    st.plotly_chart(fig, use_container_width=True)

except Exception as e:
    st.error(f"Erro ao carregar os dados: {e}")
    st.info("Verifique se o arquivo 'amazonia_tratado.csv' está na mesma pasta do script.")