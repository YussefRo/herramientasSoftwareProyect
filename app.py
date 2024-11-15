import streamlit as st
import pandas  as pd
import plotly.express as px


car_data = pd.read_csv('./vehicles_us.csv')

st.header('Anuncios de venta de coches')

hist_button = st.button('Construir histograma') # crear un botón
disp_button = st.button('Construir grafico de dispercion') # crear un botón

        
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

if disp_button:
     # escribir un mensaje
    st.write('Creación de un grafico de dispercion para el conjunto de datos de anuncios de venta de coches')
    
    # crear un histograma
    fig1 = px.scatter(car_data, x="model", y="price")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig1, key="iris", on_select="rerun")
