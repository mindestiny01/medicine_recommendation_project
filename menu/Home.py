import streamlit as st
from menu import Result


def get_start():
    st.header("✋Selamat di Aplikasi Rekomendasi Obat✋")
    st.markdown("## Informasi Dataset")
    # Dataset yang digunakan didapat dengan mengestraksi informasi dari website tertentu dengan beberapa library di Pyhthon
    # seperti built-in **string**, BeautifulSoup4, **requests**, dan **Pandas**
    st.markdown("The Project dataset are extracted by using several steps of Web Scraping\
                by using somes of python libaries, which are: built-in **string**, **BeautifulSoup4,**\
                    **Requests**, **Pandas.**")
    
    # Motivasi 
    # Projek ini dibangun dengan tujuan memberikan rekomendasi obat dengan dasar dari gejala pasien
    st.markdown("## The Project Motivation")
    st.markdown("The Project are builded for recommending medicine based on user's diseases and/or symtomps")

    # Kegunaan Projek
    st.markdown("## The Usefulness of the Project")
    
    # 1. Membantu dokter sebagai pilihan kedua
    # 2. Sebagai media informasi dalam informasi obat
    # 3. Mengurangi biaya pekerja
    # 4. Meningkatkan efisiensi dalam pengobatan pasien
    st.markdown('''
        1. Helping to be doctor's second option
        2. To be a first media for getting th medicine information'
        3. Reduces personel costs
        4. Increasing the efficiency of medical treatment
    ''')

    # Sumber Projek
    st.markdown("## The Project resources")
    # 1. Informasi Obat
    # 2. Library Streamlit
    # 3. Visual Studio Code
    # 4.  Python 3.10.4
    st.markdown('''
        1. Medicine Information from [Guesehat](https://www.guesehat.com/info-obat)
        2. Data Dashboard Web using [Streamlit](https://streamlit.io/)
        3. Visual Studio Code
        4. Python 3.10.4
    ''')

    # Klik menu 'Result' diatas untuk mendapatkan informasi rekomendasi
    st.markdown("### Click 'Result' button in navigation bar for the experiences")
    