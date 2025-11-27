import streamlit as st

from splash import splash
from mapa import mostrar_mapa
from dados import pontos_turisticos_londrina
from gps import get_user_location

st.set_page_config(layout="wide")


with st.sidebar:
    st.write("Teste")

user_lat, user_lon = get_user_location()

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


mostrar_mapa(user_lat, user_lon, pontos_turisticos_londrina)

