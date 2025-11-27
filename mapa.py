import folium

def criar_mapa(user_lat, user_lon, pontos):
    m = folium.Map(
        location=[-23.2887, -51.2297],
        zoom_start=13,
        tiles="cartodb positron"
    )

    if user_lat and user_lon:
        folium.Marker(
            location=[user_lat, user_lon],
            tooltip="Você está aqui",
            icon=folium.Icon(icon="user", prefix="fa", color="green")
        ).add_to(m)

    for p in pontos:
        folium.Marker(
            location=[p["latitude"], p["longitude"]],
            tooltip=p["nome"],
            icon=folium.Icon(icon=p["icon"], prefix=p["prefix"], color=p["color"])
        ).add_to(m)

    return m
