import streamlit as st
import base64
import time

def load_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()
    return encoded

def splash():
    img_base64 = load_base64_image("passaro.png")
    placeholder = st.empty()
    placeholder.markdown(
        f"""
        <div style="
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        ">
            <img src="data:image/png;base64,{img_base64}" style="width:200px;">
            <h2 style="text-align: center; margin-top: 10px;">
                SPOTLIGHT
            </h2>
            <h4 style="text-align: center; margin-top: 10px;">
                Onde suas experiências brilham
            </h4>
        </div>
        """,
        unsafe_allow_html=True
    )

    with st.spinner(text=""):
        

        time.sleep(3)
        placeholder.empty()





    

   

        