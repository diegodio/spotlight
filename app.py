import streamlit as st

from splash import splash
from mapa import mostrar_mapa
from dados import pontos_turisticos_londrina
from gps import get_user_location
st.set_page_config(layout="wide")

rowA = st.container()
rowB = st.container()
rowC = st.container()

# with rowB:
#     splash()

# splash()

#TODO pegar loc user

user_location = get_user_location()
# print(user_location["coords"]["latitude"])
mostrar_mapa(user_location, pontos_turisticos_londrina)

# st.map([{"lat": -23.312160, "lon": -51.159634}])
