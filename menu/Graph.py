import streamlit as st
import seaborn as sns # Please install in local computer
import matplotlib.pyplot as plt
import menu.logical.db import get_user_review, get_symtomps, get_user_name
# from menu.logical.save_data import get_symtomps, get_review

def get_start():
    st.header("Welcome to Medicine Graph")

