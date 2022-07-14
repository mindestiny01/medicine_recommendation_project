import streamlit as st
import pandas as pd
from awesome_table import AwesomeTable
from awesome_table.column import Column

def get_start():
    sample_data = './data/indonesian_medicine_dataset.csv'
    st.markdown("## ✋Welcome to Medicine Table Info ✋")
    st.markdown("### Hold 🖱️Left click + ⌨SHIFT to scrolled table to right")
    AwesomeTable(pd.read_csv(sample_data), columns = [
        Column(name = 'ID', label = 'ID'),
        Column(name = 'Name', label = 'Name Obat'),
        Column(name = 'Overview', label = 'Deskripsi Obat'),
        Column(name = 'Works', label = 'Cara Kerja'),
        Column(name = 'Effects', label = 'Efek Penggunaan'),
        Column(name = 'Use', label = 'Pemakaian'),
        Column(name = 'Dose', label = 'Dosis')
    ], show_search = True, show_order = True)
