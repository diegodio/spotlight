import streamlit as st
import folium
from streamlit_folium import st_folium

def mostrar_mapa(user_location, pontos_turisticos_londrina):
    m = folium.Map(
        location=[-23.2887, -51.2297],
        zoom_start=13,
        tiles="cartodb positron"
    )

    folium.Marker(
            location=[user_location["coords"]["latitude"], user_location["coords"]["longitude"]],
            tooltip="user",
            icon=folium.Icon(icon="map-marked", prefix="fa", color="green")
        ).add_to(m)
    

    for dic in pontos_turisticos_londrina:
        folium.Marker(
            location=[dic["latitude"], dic["longitude"]],
            tooltip=dic["nome"],
            icon=folium.Icon(icon="map-marked", prefix="fa", color="red")
        ).add_to(m)

    colA, colB, colC = st.columns(3)
    with colB:
        st_folium(m, width=700, height=500)
