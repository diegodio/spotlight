import streamlit as st
from mapa import criar_mapa
from dados import pontos_londrina
from gps import get_user_location
from streamlit_folium import st_folium


st.set_page_config(layout="wide", page_icon="icon.png", page_title="Spotlight")


with st.sidebar:
    st.write("Teste")

user_lat, user_lon = get_user_location()

if user_lat is None:
    st.warning("⚠️ Para continuar, permita o acesso à sua localização no navegador.")


# print(user_location["coords"]["latitude"])

rowA = st.container()

with rowA:
    colA, colB, colC = st.columns(3)

    with colA:
        #filtro
        options = st.multiselect(
            label="",
            placeholder = "Filtrar",
            options = ["Restaurantes", "Cultura", "Pontos Turísticos"],
            # default=["Yellow", "Red"],
        )
    with colB:
        #classificar
        options = st.selectbox(
            label="",
            placeholder = "Classificar",
            options = ["Proximidade", "Preço", "Avaliações"],
            # default=["Yellow", "Red"],
        )
    
    with colC:
        st.markdown("")
        st.markdown("")

        st.markdown("\n X resultados")

mapa = criar_mapa(user_lat, user_lon, pontos_londrina)

colA, colB, colC = st.columns(3)
with colB:
    st_folium(mapa, width=700, height=500)


