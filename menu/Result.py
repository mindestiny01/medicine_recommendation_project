import streamlit as st
from fpdf import FPDF
from menu.logical.recommendation_process import recommendation
# from menu.logical import save_data as sd

def get_start():

    ## some configuration
    symtomps = ["Symtomp One", "Symtomp Two", "Symtomp Three"]
    reviews = ["Rating", "Comment"]

    ## headers
    st.header("✋ Recommendation Menu ✋")

    ## creating user form
    with st.form("Input the related in to input box", clear_on_submit = True):
        
        ## make columns for name and age
        col_one, col_two = st.columns(2)
        with col_one:
            user_name = st.text_input("Your Name", placeholder = "Input here")
        with col_two:
            age = st.number_input("Your age: ", min_value = 0, format = "%i")

        "---"
        ## text input for symtomps
        with st.expander("Symtomps"):
            for symtomp in symtomps:
                symtomp = st.text_input(f"{symtomp}", key = symtomp)
        # disease = st.text_input("Already know the disease? just tell us. It's more better")
        
        "---"
        ## user comment
        # with st.expander("Reviews"):
        #     # Rating
        #     reviews[0] = st.selectbox("Your Rating?", ('A', 'B', 'C', 'D', 'E', 'F'))
        #     # Comment
        #     reviews[1] = st.text_area("Your Comment", placeholder = "Type here")

        "---"
        ## submit buttom
        submit = st.form_submit_button("Give the recommendation")

        ## if submitted
        if submit:
            record_symtomps = [] # storing the all symtomps

            ## Dictionary of symtomps
            sym_record = {symtomp: st.session_state[symtomp] for symtomp in symtomps}
            # review_record = {review: st.session_state[review] for review in reviews}

            ## Appending the value of dictionary
            for v in sym_record.values(): record_symtomps.append(v)
            result = recommendation(record_symtomps) # get the reccomnendation

            #Data already recorded
            # Displaying the data
            st.success("Data Saved!!")
            st.markdown(f"Hai, **{user_name}**")
            st.markdown(f"Your are **{age}** years old")
            st.markdown(f"Your Symtomps is {result}")
            for idx, val in sym_record.items(): st.markdown(f"**{idx} = {val}**")
            # st.markdown(f"your rating is **{reviews[0]}**")
            # st.markdown(f'*{reviews[1]}*')
            
            # Save the user data
            # sd.get_save_data(user_name, age, sym_record, review_record)
            
