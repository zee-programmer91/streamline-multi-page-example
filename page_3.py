


import streamlit as st
import pandas as pd
import numpy as np
import time
import requests
import templates
# import streamlit_authenticator as stauth
# from streamlit_lottie import st_lottie
# from streamlit_lottie import st_lottie_spinner


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()




def app():
    lottie_url_hello = "https://assets3.lottiefiles.com/private_files/lf30_hdiNFs.json"
# lottie_url_download = "https://assets4.lottiefiles.com/private_files/lf30_t26law.json"
    lottie_hello = load_lottieurl(lottie_url_hello)
# lottie_download = load_lottieurl(lottie_url_download)


    # st_lottie(lottie_hello, key="hello")

    selected = st.text_input("", "Search...")

    button_clicked = st.button("OK")    
    st.markdown("# Companies")
    st.sidebar.markdown("# Notes for Com")
    st.markdown(templates.title_template.format("Olayile Ejekwu", "Data Scientist", "University of Pretoria", "UP", "07/07/2022", "I am a Data Scientist with 6 moths of experience, I enjoy coding and long walks on the beach"),  unsafe_allow_html=True)
    st.markdown(templates.title_template.format("Olayile Ejekwu", "Data Scientist", "University of Pretoria", "UP", "07/07/2022", "I am a Data Scientist with 6 moths of experience, I enjoy coding and long walks on the beach"),  unsafe_allow_html=True)
    st.markdown(templates.title_template.format("Olayile Ejekwu", "Data Scientist", "University of Pretoria", "UP", "07/07/2022", "I am a Data Scientist with 6 moths of experience, I enjoy coding and long walks on the beach"),  unsafe_allow_html=True)
    st.markdown(templates.title_template.format("Olayile Ejekwu", "Data Scientist", "University of Pretoria", "UP", "07/07/2022", "I am a Data Scientist with 6 moths of experience, I enjoy coding and long walks on the beach"),  unsafe_allow_html=True)

    df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

    #st.map(df)


hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

# credentials:
#   usernames:
#     jsmith:
#       email: jsmith@gmail.com
#       name: John Smith
#       password: '123' # To be replaced with hashed password
#     rbriggs:
#       email: rbriggs@gmail.com
#       name: Rebecca Briggs
#       password: '456' # To be replaced with hashed password
# cookie:
#   expiry_days: 30
#   key: some_signature_key
#   name: some_cookie_name
# preauthorized:
#   emails:
#   - melsby@gmail.com