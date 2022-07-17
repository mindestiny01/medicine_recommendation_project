import streamlit as st
from deta import Deta

# ADD to Advanced configuration -> secrets
# DETA_KEY = "c07gbli5_KACPnEqNNPER4fZwSMxZhGLDvRoMKNzA"

deta = Deta(st.secrets["DETA_KEY"])

db = deta.Base("user_recommendation_result")

def get_save_data(
    user_name: str, age: int, sym_record: dict, review_record: dict ):
    return db.put({"key": user_name, "age": age, "Symtomps": sym_record, "Reviews": review_record})


def get_user_name(user_name):
    return db.get(user_name)

def get_symtomps(sym_record):
    symtomps = db.get(sym_record)
    return symtomps.values

def get_user_review(review_record):
    return review_record