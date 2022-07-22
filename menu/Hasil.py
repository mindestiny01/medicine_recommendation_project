from jinja2 import Environment, select_autoescape, FileSystemLoader
import streamlit as st
import pdfkit
import os

# Several important functions
from menu.logical.recommendation_process import main_recommendation
from menu.logical.db import get_save_data

THIS_DIR = os.path.dirname(os.path.abspath(__file__))

def get_start():
    # Configuration
    symtomps = ["Gejala Satu", "Gejala Dua", "Gejala Tiga"]
    reviews = ["Berikan Peringkat? Dari A - F.", "Komentar anda"]
    os_env = Environment(loader = FileSystemLoader(THIS_DIR), autoescape = select_autoescape())
    pdf_template = os_env.get_template('template/template.html')
    for_the_report = {}

    ## UI START
    st.header("✋ Menu Rekomendasi ✋")

    with st.form("Masukkan Data Diri kamu", clear_on_submit = True):
        
        col_one, col_two = st.columns(2)
        with col_one: user_name = st.text_input("Nama anda", placeholder = "Ketik disini")
        with col_two: user_age = st.text_input("Umur anda: ", placeholder = "Ketik disini")

        with st.expander("Gejala"):
            for symtomp in symtomps: symtomp = st.text_input(f"{symtomp}", key = symtomp)
        
        with st.expander("Tinjuan"):
            for review in reviews: review = st.text_input(f"{review}", key = review)

        if st.form_submit_button("Berikan rekomendasi"):
            
            record_symtomps = []
            # Session state for the symtomps and user_review
            sym_record = {symtomp: st.session_state[symtomp] for symtomp in symtomps}
            review_record = {review: st.session_state[review] for review in reviews}
            for v in sym_record.values(): record_symtomps.append(v)
            result = None

            # Append the User Input into dictionary
            for_the_report['name'] = user_name
            for_the_report['age'] = int(user_age)
            for_the_report['symtomps'] = record_symtomps
            for_the_report['recommendation'] = result
            
            # More Informations
            with st.expander("See Information"):
                st.success("Data tersimpan !!!")
                st.markdown(f"Halo, **{user_name}**")
                st.markdown(f"Kamu saat ini berumur **{user_age}** Tahun")
                st.markdown(f"Berikut gejala - gejala yang kamu rasakan saat ini: ")
                for idx, val in sym_record.items(): st.markdown(f"**{idx} = {val}**")
                # st.markdown(f"Rekomendasi obat terbaik untukmu adalah:  **{result}**")
                # st.markdown(user_review)
                for idx, val in review_record.items(): st.markdown(f"**{idx} = {val}**")
            
            # Save the user data
            get_save_data(user_name, int(user_age), sym_record, review_record)
            st.success('🥳 Informasi telah berhasil dibuat')


    # Generating PDF of Medicine Recommendation
    render_template = pdf_template.render(for_the_report)
    final_result = pdfkit.from_string(render_template, False)

    st.download_button(
        "Unduh rekomendasi",
        data = final_result,
        file_name = f'{user_name}+{user_age}+success.pdf',
        mime = "application/octet-stream"
    )