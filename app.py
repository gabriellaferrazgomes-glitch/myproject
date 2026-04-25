import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles.csv')

st.header('Análise de veículos')

hist_button = st.button('Criar histograma')

if hist_button:
    st.write('Criando um histograma para o conjunto de dados')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)


car_data = pd.read_csv('/vehicles.csv') # lendo os dados
fig = px.scatter(car_data, x="odometer", y="price") # criar um gráfico de dispersão
fig.show() # exibindo