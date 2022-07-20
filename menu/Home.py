import streamlit as st


def get_start():
    st.caption("Klik menu 'Hasil' diatas untuk mendapatkan informasi rekomendasi")
    st.header("✋Selamat di Aplikasi Rekomendasi Obat✋")
    st.markdown("## Informasi Dataset")
    st.markdown("Dataset yang digunakan didapat dengan mengestraksi informasi dari website tertentu\
                dengan beberapa library di Pyhthon seperti\
                built-in **string**, BeautifulSoup4, **Requests**, dan **Pandas**")
    

    st.markdown("## Motivasi ")
    st.markdown("Projek ini dibangun dengan tujuan memberikan rekomendasi obat dengan dasar dari gejala pasien")

    st.markdown("## Kegunaan Projek")
    st.markdown('''
        1. Membantu dokter sebagai pilihan kedua
        2. Sebagai media informasi dalam rekomendasi obat
        3. Mengurangi biaya pekerja
        4. Meningkatkan efisiensi dalam pengobatan pasien
    ''')

    st.markdown("## Sumber dan Alat Projek")
    st.markdown('''
        1. Informasi Obat dari [Guesehat](https://www.guesehat.com/info-obat)
        2. Library [Streamlit](https://streamlit.io/)
        3. Visual Studio Code
        4.  Python 3.10.4
    ''')