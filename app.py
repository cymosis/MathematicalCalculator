import streamlit as st
from view import get_user_input
from bodmas import split_bodmas
from trigonometric import trigon_value
from brackets_bodmas import evaluate_expression

# Streamlit App Title
st.title("Modular Web-Based Calculator")
st.write("Perform mathematical equations.")

# Fetch user input
expression,user_choice=get_user_input()
if user_choice=='Bodmas':
    # Perform Calculation
    if st.button("Calculate"):
        try:
            result = evaluate_expression(expression)
            st.success(result)

        except Exception as e:
            st.error(f"An unexpected error occurred: {e}")

elif user_choice=='Trigonometric':

    if st.button("Calculate"):
        try:
            result = trigon_value(expression)
            st.success(result)

        except Exception as e:
            st.error(f"An unexpected error occurred: {e}")

elif user_choice=='Calculus':
    st.status('This feature is under development')