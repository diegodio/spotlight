import streamlit as st

from splash import splash
from mapa import mostrar_mapa
from dados import pontos_turisticos_londrina
from gps import get_user_location

st.set_page_config(
    page_title="Spotlight",
    page_icon="🔦",
    layout="wide",
)

# --- Splash (uma vez por sessão) ---
if "splash_done" not in st.session_state:
    st.session_state.splash_done = False

if not st.session_state.splash_done:
    splash()
    st.session_state.splash_done = True
    st.stop()

# --- Sidebar ---
with st.sidebar:
    st.header("Spotlight")
    st.caption("Onde suas experiências brilham ✨")

# --- Localização ---
user_lat, user_lon = get_user_location()

if user_lat is None or user_lon is None:
    st.warning("Para continuar, permita o acesso à sua localização no navegador.")

# --- Barra de filtros ---
rowA = st.container()

with rowA:
    colA, colB, colC = st.columns(3)

    with colA:
        filtro_categorias = st.multiselect(
            label="",
            placeholder="Filtrar",
            options=["Restaurantes", "Cultura", "Pontos Turísticos"],
        )
    with colB:
        criterio_ordenacao = st.selectbox(
            label="",
            placeholder="Classificar",
            options=["Proximidade", "Preço", "Avaliações"],
        )
    
    with colC:
        st.markdown("")
        st.markdown("")
        st.markdown("\n X resultados")

# --- Mapa ---
mostrar_mapa(user_lat, user_lon, pontos_turisticos_londrina)
