import streamlit as st
from awesome_table import AwesomeTable
from awesome_table.column import Column
import pandas as pd
from menu.logical.db import get_save_data, get_user_review, get_symtomps, get_user_name


def get_start():
    sample_review = './data/user_review.csv'
    st.markdown("## 👨👩Beberapa Tinjauan dari para pengguna")
    st.caption("Tahan 🖱️Klik kiri + ⌨SHIFT untuk digulir ke kiri")
    AwesomeTable(pd.read_csv(sample_review), columns = [
        Column(name = 'ID', label = 'ID'),
        Column(name = 'Name', label = 'Nama Pengunjung'),
        Column(name = 'Address', label = 'Alamat Rumah'),
        Column(name = 'Rating', label = 'Peringkat Rekomendasi'),
        Column(name = 'Review', label = 'Ulasan')
    ], show_order = True)