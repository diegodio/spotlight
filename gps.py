# gps.py
from streamlit_js_eval import get_geolocation

def get_user_location():
    """
    Retorna (lat, lon) ou (None, None) se o usuário não deu permissão.
    Não faz nenhuma chamada de UI (st.*).
    """
    location = get_geolocation()
    
    if not location or "coords" not in location:
        return None, None

    coords = location["coords"]
    return coords.get("latitude"), coords.get("longitude")
