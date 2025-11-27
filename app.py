import streamlit as st

from splash import splash
from mapa import mostrar_mapa
from dados import pontos_londrina
from gps import get_user_location

st.set_page_config(layout="wide", page_icon="icon.png", page_title="Spotlight")

with st.sidebar:
    st.write("Teste")

user_lat, user_lon = get_user_location()

rowA = st.container()

with rowA:
    colA, colB, colC = st.columns(3)

    label_to_tipo = {
        "Restaurantes": "restaurante",
        "Cultura": "cultura",
        "Pontos Turísticos": "ponto_turistico",
        "Hotéis": "hotel",  
    }

    with colA:
        # Filtro
        filtros_selecionados = st.multiselect(
            label="",
            placeholder="Filtrar",
            options=list(label_to_tipo.keys()),
        )

    with colB:
        # Classificar (ainda não implementado)
        criterio_ordem = st.selectbox(
            label="",
            placeholder="Classificar",
            options=["Proximidade", "Preço", "Avaliações"],
        )

    # APLICAR FILTRO SOBRE pontos_londrina
    if filtros_selecionados:
        tipos_selecionados = [label_to_tipo[lab] for lab in filtros_selecionados]
        pontos_filtrados = [
            p for p in pontos_londrina if p["tipo"] in tipos_selecionados
        ]
    else:
        # se nada selecionado, mostra tudo
        pontos_filtrados = pontos_londrina

    with colC:
        st.markdown("")
        st.markdown("")
        st.markdown(f"\n **{len(pontos_filtrados)} resultados**")

mostrar_mapa(user_lat, user_lon, pontos_filtrados)
