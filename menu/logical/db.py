import streamlit as st
from deta import Deta

# ADD to Advanced configuration -> secrets
# DETA_KEY = "c07gbli5_KACPnEqNNPER4fZwSMxZhGLDvRoMKNzA"

# deta = Deta(st.secrets["DETA_KEY"])

# db = deta.Base("user_recommendation_result")

def get_save_data(
    user_name: str, age: int, sym_record: dict, review_record: dict ):
    
    pass
    # return db.put({"key": user_name, "age": age, "Symtomps": sym_record, "Reviews": review_record})

def get_user_name(user_name):
    pass

def get_symtomps(sym_record):
    pass

def get_user_review(review_record):
    return review_record