# mapa.py
import folium
from streamlit_folium import st_folium

DEFAULT_CENTER = [-23.2887, -51.2297]

def criar_mapa(user_lat, user_lon, pontos_turisticos_londrina):
    """
    Cria e retorna o objeto folium.Map, sem renderizar no Streamlit.
    """
    # Se a localização do usuário for válida, usa como centro
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

    # Marcador do usuário, se existir
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
            icon=folium.Icon(icon=dic["icon"], prefix=dic["prefix"], color=dic["color"])
        ).add_to(m)

    return m

def mostrar_mapa(user_lat, user_lon, pontos_turisticos_londrina, height=500):
    """
    Conveniência: cria o mapa e já renderiza com st_folium.
    O layout (colunas etc.) é decidido no app, não aqui.
    """
    m = criar_mapa(user_lat, user_lon, pontos_turisticos_londrina)
    st_folium(m, use_container_width=True, height=height)
