import streamlit as st
import folium
from streamlit_folium import st_folium

def mostrar_mapa(user_lat, user_lon, pontos_turisticos_londrina):
    m = folium.Map(
        location=[-23.2887, -51.2297],
        zoom_start=13,
        tiles="cartodb positron"
    )

    try:
        if user_lat and user_lon:
            folium.Marker(
                    location=[user_lat, user_lon],
                    tooltip="user",
                    icon=folium.Icon(icon="map-marked", prefix="fa", color="green")
                ).add_to(m)
    except:
        st.warning("Para continuar, permita o acesso à sua localização no navegador.")

    for dic in pontos_turisticos_londrina:
        folium.Marker(
            location=[dic["latitude"], dic["longitude"]],
            tooltip=dic["nome"],
            icon=folium.Icon(icon=dic["icon"], prefix=dic["prefix"], color=dic["color"])
        ).add_to(m)

    colA, colB, colC = st.columns(3)
    with colB:
        st_folium(m, width=700, height=500)
