import streamlit as st
from streamlit_option_menu import option_menu
from menu import (
    Diagram,
    Hasil,
    Home,
    Tabel, 
    Review)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def get_option():

    hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
    st.markdown(hide_st_style, unsafe_allow_html=True)

    selected = option_menu(
        menu_title = None,
        options = ['Home', 'Hasil', 'Diagram', 'Tabel', 'Review'],
        icons = ['house', 'boxes', 'file-bar-graph', 'table', 'people'],
        menu_icon = 'house-fill', 
        default_index = 0,
        orientation = "horizontal"
    )
    
    if selected == 'Home': Home.get_start()
    if selected == 'Hasil': Hasil.get_start() 
    if selected == 'Diagram': Diagram.get_start()
    if selected == 'Tabel': Tabel.get_start()
    if selected == 'Review': Review.get_start()

get_option()