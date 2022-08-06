
import streamlit as st
import templates
# from streamlit_lottie import st_lottie
# from streamlit_lottie import st_lottie_spinner

import requests

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()




languages = ["Python", "R", "Java", "JavaScript", "C++", "Cotlin", "Ruby", "Fotran", "Visual Basic", "PHP"]
roles = ["Software Engineer", "Cloud Engineer", "Data Engineer", "Data Scientist", "Web developer", "Full stack Developer", "Back End developer", "Mobile developer"]
def app():
    st.markdown("# Applicants")
    lottie_url_hello = "https://assets2.lottiefiles.com/packages/lf20_azqcvl9w.json"
# lottie_url_download = "https://assets4.lottiefiles.com/private_files/lf30_t26law.json"
    lottie_hello = load_lottieurl(lottie_url_hello)
# lottie_download = load_lottieurl(lottie_url_download)


    # st_lottie(lottie_hello, key="hello")
    
    st.sidebar.markdown("# Notes for Applicants 🎉")
    st.sidebar.markdown(" Equal tech is a gender neutral recruitment app that helps you secure a job without bias.")
    
    name = st.text_input('Please enter your name')
    surname = st.text_input('Please enter your surname')
    languages_x = st.multiselect("What Programming languages are you proficient at?", languages)
    min_salary = st.slider("What is your minimum salary expectation per month?", min_value= 1000, max_value= 1000000, step= 1000)

    col1, col2, col3 = st.beta_columns(3)

    with col1:
        st.success("Education history 1")
        
        st.date_input("Start Date")
        st.date_input("End Date")
        st.multiselect("What Frameworks were required in this job, click all that apply", languages)

    with col2:
        st.success("Education history 2")
        st.date_input("Start Date", key="1")
        st.date_input("End Date", key="2")

    with col3:
        st.success("Education history 3")
        st.date_input("Start Date", key="3")
        st.date_input("End Date", key= "4")

    col4, col5, col6 = st.beta_columns(3)

    with col4:
        st.success("Work history 1")
        st.multiselect("What role did you work as", roles)
        st.date_input("Start Date", key="10")
        st.date_input("End Date", key= "11")

    with col5:
        st.success("Work history 2")
        st.date_input("Start Date", key="6")
        st.date_input("End Date", key="7")

    with col6:
        st.success("Work history 3")
        st.date_input("Start Date", key="8")
        st.date_input("End Date", key= "9")

    hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                </style>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True) 