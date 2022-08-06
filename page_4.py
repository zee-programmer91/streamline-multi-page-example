import streamlit as st

def app():
    st.markdown("# Rate a company ⭐️ ")
    st.sidebar.markdown("# Notes for Companies")

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 