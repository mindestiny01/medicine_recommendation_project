import streamlit as st
from deta import Deta

# ADD to Advanced configuration -> secrets
# DETA_KEY = "c07gbli5_KACPnEqNNPER4fZwSMxZhGLDvRoMKNzA"

# PLease to set up the DETA_KEY to advanced configuration
deta = Deta(st.secrets["DETA_KEY"])

# Create and Set the Database
db = deta.Base("user_recommendation_result")

# Save the data to the Deta base
def get_save_data(
    user_name: str, age: int, sym_record: dict, review_record: dict ):
    return db.put({"key": user_name, "age": age, "Symtomps": sym_record, "Reviews": review_record})

# Get the specific key, which is user name to get all the information
def get_user_name(user_name):
    return db.get(user_name)

# Get the newest info for the recommendation
def get_symtomps():
    symtomps = db.get(sym_record)
    return symtomps.values

# Get the newest user review
def get_user_review():
    return review_record