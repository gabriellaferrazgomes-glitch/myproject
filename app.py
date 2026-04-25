import pandas as pd
import plotly.express as px
import streamlit as st

# carregar dados
car_data = pd.read_csv('vehicles_us.csv')

st.header('Análise de veículos')

st.subheader('Histograma de quilometragem')
if st.button('Criar histograma'):
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

st.subheader('Relação entre preço e quilometragem')
if st.button('Criar gráfico de dispersão'):
    fig = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig, use_container_width=True)

# filtro interativo
st.subheader('Filtro por preço')
max_price = st.slider('Preço máximo', 0, 100000, 50000)

filtered_data = car_data[car_data['price'] <= max_price]

fig = px.scatter(filtered_data, x='odometer', y='price')
st.plotly_chart(fig, use_container_width=True)