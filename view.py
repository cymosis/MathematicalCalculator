import streamlit as st

def get_user_input():
    st.sidebar.header("Calculator Input")
    expression = st.sidebar.text_input("Please enter problem")
    return expression
