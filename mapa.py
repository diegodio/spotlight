# mapa.py
import streamlit as st
import folium
from streamlit_folium import st_folium

DEFAULT_CENTER = [-23.2887, -51.2297]

def mostrar_mapa(user_lat, user_lon, pontos_turisticos_londrina):
    # Decide o centro do mapa
    if user_lat is not None and user_lon is not None:
        center = [user_lat, user_lon]
        zoom = 14
    else:
        center = DEFAULT_CENTER
        zoom = 13

    m = folium.Map(
        location=center,
        zoom_start=zoom,
        tiles="cartodb positron"
    )

    # Marcador do usuário (se tivermos coordenadas)
    if user_lat is not None and user_lon is not None:
        folium.Marker(
            location=[user_lat, user_lon],
            tooltip="Você está aqui",
            icon=folium.Icon(icon="map-marked", prefix="fa", color="green")
        ).add_to(m)

    # Pontos turísticos
    for dic in pontos_turisticos_londrina:
        folium.Marker(
            location=[dic["latitude"], dic["longitude"]],
            tooltip=dic["nome"],
            icon=folium.Icon(
                icon=dic["icon"],
                prefix=dic["prefix"],
                color=dic["color"]
            )
        ).add_to(m)

    # Layout simples: mapa centralizado em uma coluna
    colA, colB, colC = st.columns(3)
    with colB:
        st_folium(m, width=700, height=500)
