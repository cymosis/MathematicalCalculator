import streamlit as st
from view import get_user_input
from exceptions import DivisionByZeroError
from bodmas import split_bodmas

# Streamlit App Title
st.title("Modular Web-Based Calculator")
st.write("Perform mathematical equations.")

# Fetch user input
expression=get_user_input()

# Perform Calculation
if st.button("Calculate"):
    try:
        result = split_bodmas(expression)
        st.success(result)

    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
