import streamlit as st
from streamlit_js_eval import get_geolocation

# st.set_page_config(page_title="Localização do Usuário")

# st.title("📍 Localização pelo navegador")

# def get_user_location():
#     location = get_geolocation()
    
#     return location

    # if location:
    #     st.success("Localização obtida com sucesso ✅")

    #     st.write("Latitude:", location["coords"]["latitude"])
    #     st.write("Longitude:", location["coords"]["longitude"])
    #     st.write("Precisão (m):", location["coords"]["accuracy"])
    # else:
    #     st.info("Clique em permitir acesso à localização no navegador.")

def get_user_location():
    
    location = get_geolocation()
    
    if location:
         
        return location["coords"]["latitude"], location["coords"]["longitude"]
    
    else:
        st.warning("Para continuar, permita o acesso à sua localização no navegador.")
