import streamlit as st
from awesome_table import AwesomeTable
from awesome_table.column import Column
import pandas as pd


def get_start():
    sample_review = './data/user_review.csv'
    st.markdown("# 👨👩Some Review from Users")
    st.markdown("### Hold 🖱️Left click + ⌨SHIFT to scrolled table to right")
    AwesomeTable(pd.read_csv(sample_review), columns = [
        Column(name = 'ID', label = 'ID'),
        Column(name = 'Name', label = 'Nama Pengunjung'),
        Column(name = 'Address', label = 'Alamat Rumah'),
        Column(name = 'Rating', label = 'Peringkat Rekomendasi'),
        Column(name = 'Review', label = 'Ulasan')
    ], show_order = True)