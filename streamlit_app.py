import streamlit as st
from streamlit_option_menu import option_menu
import requests
from streamlit_lottie import st_lottie

st.set_page_config(layout="wide")

# Inject custom CSS
st.markdown(
    """
    <style>
    /* Change the background color */
    body {
        background-color: black;
        color: white;
    }
    /* Change the color of the icons */
    .css-18e3th9 {
        background-color: black;
    }
    .css-1aumxhk a {
        color: purple !important;
    }
    .st-bx, .st-bo, .st-bz {
        color: purple !important;
    }
    </style>
    """, unsafe_allow_html=True
)

st.write("##")
st.title("Mohammed Mohiuddin Portfolio")
st.write("Welcome to my website")
st.write('----')

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_url = load_lottieurl("https://lottie.host/5f38930a-19ba-417c-aedd-d679f9fa7216/wDROZxnu46.json")

with st.container():
    selected = option_menu(
        menu_title=None,
        options=['About', 'Projects', 'Contact'],
        icons=['person', 'code-slash', 'chat-left-text-fill'],
        orientation='horizontal'
    )

if selected == 'About':
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.write("##")
            st.subheader("I am Mohammed Mohiuddin")
            st.title("Undergraduate Student at University of Washington")
        with col2:
            st_lottie(lottie_url)

    st.write('----')
    
    with st.container():
        col3, col4 = st.columns(2)
        with col3:
            st.subheader("""
        Education
        - University of Washington Bothell
            - Bachelor of Computer Science & Software Engineering (CSSE)
            - GPA: 3.66
        - Bellevue Community College
            - Running Start Program
            - GPA: 3.98                
        """)
        with col4:
            st.subheader("""
            Experience
        - Dataroo AI Evaluator Internship
            - Duration: August 2023 - December 2023
            - <insert info>
        - Best Buy Computer Sales Associate
            - Duration: June 2023 - September 2023
            - <insert info>
        - Instructor at Interactive Math Academy IMA
            - Duration: Jan 2020 - Jan 2022
        """)
