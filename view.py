import streamlit as st
import math
from nukeyboard import nuinput_expression
from keyboardtri import trinput_expression

def get_user_input():
    st.sidebar.header("Calculator Input")
    options = ['Trigonometric', 'Bodmas', 'Calculus']
    user_choice = st.sidebar.radio('Please select the type of expression to solve:', options)

    expression = None
    if user_choice == 'Trigonometric':
        expression = trinput_expression()
    elif user_choice == 'Bodmas':
        expression = nuinput_expression()
    elif user_choice == 'Calculus':
        expression = print('This feature is under development')

    return expression, user_choice
