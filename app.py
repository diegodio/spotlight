# app.py
import streamlit as st

from splash import splash
from mapa import mostrar_mapa
from dados import pontos_turisticos_londrina
from gps import get_user_location

st.set_page_config(
    page_title="Spotlight",
    page_icon="🔦",
    layout="wide"
)

# --- Controle de splash via session_state ---
if "show_splash" not in st.session_state:
    st.session_state.show_splash = True

if st.session_state.show_splash:
    splash()
    # Depois que a splash terminar, ela mesma não desativa nada,
    # então a gente marca aqui:
    st.session_state.show_splash = False
    st.stop()  # interrompe a renderização desta rodada

# --- Sidebar ---
with st.sidebar:
    st.header("Spotlight")
    st.caption("Onde suas experiências brilham ✨")

# --- Localização do usuário ---
user_lat, user_lon = get_user_location()

if user_lat is None or user_lon is None:
    st.warning("Para continuar, permita o acesso à sua localização no navegador.")

# --- Filtros / Header ---
rowA = st.container()

with rowA:
    colA, colB, colC = st.columns([2, 2, 1])

    with colA:
        filtro_categorias = st.multiselect(
            label="Filtrar por categoria",
            placeholder="Selecione categorias",
            options=["Restaurantes", "Cultura", "Pontos Turísticos"],
        )
    with colB:
        criterio_ordenacao = st.selectbox(
            label="Ordenar por",
            options=["Proximidade", "Preço", "Avaliações"],
            index=0,
        )
    
    with colC:
        st.markdown("### ")
        st.markdown("**X resultados**")  # depois a gente substitui por algo real

# --- Mapa ---
st.subheader("Mapa de experiências")
mostrar_mapa(user_lat, user_lon, pontos_turisticos_londrina)
