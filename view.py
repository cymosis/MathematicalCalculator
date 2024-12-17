import streamlit as st

def get_user_input():
    st.sidebar.header("Calculator Input")
    options=['Trigonometric','Bodmas','Calculus']
    user_choice=st.sidebar.radio('Please select the type of expression to solve:',options)
    if user_choice=='Trigonometric':
        expression=st.sidebar.text_input('Please write trigonmetric expressin')
    elif user_choice=='Bodmas':
        expression = st.sidebar.text_input("Please enter problem")
    return expression
