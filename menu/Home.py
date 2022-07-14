import streamlit as st
from menu import Result


def get_start():
    st.header("✋Welcome to Medicine Recommendation✋")
    st.markdown("## Dataset Information")
    st.markdown("The Project dataset are extracted by using several steps of Web Scraping\
                by using somes of python libaries, which are: built-in **string**, **BeautifulSoup4,**\
                    **Requests**, **Pandas.**")
    
    st.markdown("## The Project Motivation")
    st.markdown("The Project are builded for predicting medicine based on user's diseases and/or symtomps")

    st.markdown("## The Usefulness of the Project")
    st.markdown('''
        1. Helping to be doctor's second option
        2. To be a first media for getting th medicine information'
        3. Reduces personel costs
        4. Increasing the efficiency of medical treatment
    ''')

    st.markdown("## The Project resources")
    st.markdown('''
        1. Medicine Information from [Guesehat](https://www.guesehat.com/info-obat)
        2. Data Dashboard Web using [Streamlit](https://streamlit.io/)
        3. Visual Studio Code
        4. Python 3.10.4
    ''')

    st.markdown("### Click 'Result' button in navigation bar for the experiences")
    