import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from menu.logical.db import get_user_review, get_symtomps, get_user_name
from datetime import datetime

DATASET = 'menu/logical/data/preprocessing_finish.csv'

def get_start():
    st.header("Diagram Informasi")

    st.markdown("### 1. Top 10 Topik yang Berhubungan")
    st.caption("Data yang didapat dari pencocokan hasil ekstraksi data dengan keluhan/gejala")
    dt = pd.read_csv(DATASET)
    cond = dict(dt['Symtomps'].value_counts())
    top_condition = list(cond.keys())[0:10]
    values = list(cond.values())[0:10]

    fig_1 = plt.figure(figsize = (10, 5))
    plt.bar(top_condition, values)
    plt.xlabel("Keluhan/Gejala")
    plt.ylabel("Besar Data")
    plt.title("Top 1o Topik Kesehatan")
    st.pyplot(fig_1)


    st.markdown("### 2. Peringkat dari Pengguna")
    now = datetime.now()
    day_clocks = now.strftime("%d/%m/%Y %H:%M:%S")
    st.caption("Data terbaru sejak " + day_clocks)
