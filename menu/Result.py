import streamlit as st
from fpdf import FPDF
from menu.recommendation_process import recommendation

def get_start():

    ## CONFIGURATION
    symtomps = ["Symtomp One", "Symtomp Two", "Symtomp Three"]

    st.header("✋ Recommendation Menu ✋")
    with st.form("Input the related in to input box", clear_on_submit = True):
        col_one, col_two = st.columns(2)
        with col_one:
            first_name = st.text_input("First Name")
        with col_two:
            second_name = st.text_input("Second Name")
        age = st.number_input("Your age: ", min_value = 0, format = "%i")

        "---"
        with st.expander("Symtomps"):
            for symtomp in symtomps:
                symtomp = st.text_input(f"{symtomp}", key = symtomp)
        disease = st.text_input("Already know the disease? just tell us. It's more better")
        
        "---"
        with st.expander("Your Comment"):
            comment = st.text_area("", placeholder = "Type your comment")
        
        "---"
        submit = st.form_submit_button("Give the recommendation")

        if submit:
            st.success("Data Saved!!")
            result = recommendation(symtomps, disease)
            st.markdown(f"Hai, {first_name}{second_name}")
            st.markdown(f"Your are {age} years old")
            st.markdown("Your Diseases: ")
            sym_record = {symtomp: st.session_state[symtomp] for symtomp in symtomps}
            for idx, val in sym_record.items():
                st.markdown(f"{idx} = {val}")
            st.markdown(f"Your disease is {disease}")
            st.markdown(f'{comment}')
