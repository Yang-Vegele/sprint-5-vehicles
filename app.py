import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')
hist_button = st.button('criar histograma')

if hist_button:
    st.write('Criando histograma para o conjunto de dados de anuncios de vendas de carros')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

disp_button = st.button('criar gráfico de dispersão')

if disp_button:
    st.write('Criando gráfico de dispersão para o conjunto de dados de anuncios de vendas de carros')
    fig = px.scatter(car_data, x = 'odometer', y = 'price')
    st.plotly_chart(fig, use_container_width=True)