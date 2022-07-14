import streamlit as st
from fpdf import FPDF
from menu.recommendation_process import recommendation

def get_start():
    st.header("✋ Recommendation Menu ✋")
    with st.form("Input the related in to input box"):
        name = st.text_input("Your name: ")
        age = st.text_input("Your age: ")
        symtomps = st.text_input("What kind symtomps that you feel?")
        symtomps_another = st.text_input("Another symtomps: ")
        disease = st.text_input("Already know the disease? just tell us. It's more better")
        submit = st.form_submit_button("Give the recommendation")

        if submit:
            result = recommendation(symtomps, symtomps_another, disease)
            st.markdown(f'''
                Hai, {name} 👋👋👋. You are {age} years old.
                There is several symtomps/disease that you feel right know:
                1. Your Symtomp : {symtomps}
                2. Another Symtomp : {symtomps_another}
                3. Your Disease : {disease}

                and this is several medicine recommendation for you,
                1. Vitamin C
                2. Vitamin E
                3. Vitamin K
            ''')
