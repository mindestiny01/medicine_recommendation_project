import streamlit as st
from fpdf import FPDF
from menu.logical.recommendation_process import recommendation
from menu.logical.db import get_save_data, get_user_review, get_symtomps, get_user_name

def get_start():

    ## some configuration
    symtomps = ["Symtomp One", "Symtomp Two", "Symtomp Three"]
    reviews = ["Your Rating? Type A - F.", "Your Comment"]

    ## headers
    st.header("✋ Recommendation Menu ✋")

    ## creating user form
    with st.form("Input the related in to input box", clear_on_submit = True):
        
        ## make columns for name and age
        col_one, col_two = st.columns(2)
        with col_one: user_name = st.text_input("Your Name", placeholder = "Input here")
        with col_two: age = st.text_input("Your age: ", placeholder = "Input here")

        "---"
        ## text input for symtomps
        with st.expander("Symtomps"):
            for symtomp in symtomps: symtomp = st.text_input(f"{symtomp}", key = symtomp)
        
        # user comment
        with st.expander("Reviews"):
            for review in reviews: review = st.text_input(f"{review}", key = review)

        "---"
        ## submit buttom
        submit = st.form_submit_button("Give the recommendation")

        ## if submitted
        if submit:
            record_symtomps = [] # storing the all symtomps

            ## Dictionary of symtomps
            sym_record = {symtomp: st.session_state[symtomp] for symtomp in symtomps}
            review_record = {review: st.session_state[review] for review in reviews}

            ## Appending the value of dictionary
            for v in sym_record.values(): record_symtomps.append(v)
            result = recommendation(record_symtomps) # get the reccomnendation
            user_review = get_user_review(review_record)

            #Data already recorded
            # Displaying the data
            st.success("Data Saved!!")
            st.markdown(f"Hai, **{user_name}**")
            st.markdown(f"Your are **{age}** years old")
            for idx, val in sym_record.items(): st.markdown(f"**{idx} = {val}**")
            for idx, val in review_record.items(): st.markdown(f"**{idx} = {val}**")
            st.markdown(f"Recommendation medicine for you is/are:  **{result}**")
            st.markdown(user_review)
            
            # Save the user data
            get_save_data(user_name, age, sym_record, review_record)
            
