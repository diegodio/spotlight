import streamlit as st
import folium
from streamlit_folium import st_folium

def mostrar_mapa(user_lat, user_lon, pontos_turisticos_londrina):
    m = folium.Map(
        location=[-23.312160, -51.159634],
        zoom_start=16,
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
            
            
            popup = folium.Popup(f"""
                                 <h2 style="font-family: Verdana, sans-serif;">
    {dic["descricao"]}
</h2>
            <button
    style="float: right;"
    onclick="document.getElementById('historia').style.display='block'">
+
</button>

<div id="historia" style="
    display:none;
    position: fixed;
    top: 10%;
    left: 50%;
    transform: translateX(-50%);
    background: white;
    padding: 15px;
    width: 320px;
    max-height: 70%;
    overflow-y: auto;
    box-shadow: 0 4px 12px rgba(0,0,0,0.3);
    z-index: 9999;
">
    <p style="font-family: Arial; font-size: 14px;">
        {dic["historia"]}
    </p>

    <div style="text-align: right; margin-top: 10px;">
        <button onclick="document.getElementById('historia').style.display='none'">
            X
        </button>
    </div>
</div>


            """, max_width=200),
            
            # popup=dic["descricao"],
            icon=folium.Icon(icon=dic["icon"], prefix=dic["prefix"], color=dic["color"])
        ).add_to(m)

    colA, colB, colC = st.columns(3)
    with colB:
        st_folium(m, width=700, height=500)
