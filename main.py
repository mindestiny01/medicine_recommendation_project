import streamlit as st
from streamlit_option_menu import option_menu
from menu import (
    Home, 
    Result, 
    Graph, 
    Table, 
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
        options = ['Home', 'Result', 'Graph', 'Table', 'Review'],
        icons = ['house', 'boxes', 'file-bar-graph', 'table', 'people'],
        menu_icon = 'house-fill', 
        default_index = 0,
        orientation = "horizontal"
    )
    
    if selected == 'Home': Home.get_start()
    if selected == 'Result': Result.get_start() 
    if selected == 'Graph': Graph.get_start()
    if selected == 'Table': Table.get_start()
    if selected == 'Review': Review.get_start()

get_option()