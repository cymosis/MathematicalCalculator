
import streamlit as st

# Initialize the number string in session state
if 'number_string' not in st.session_state:
    st.session_state.number_string = ""

def trinput_expression():
    # Function to handle the button click
    def update_number(number):
        st.session_state.number_string += str(number)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        for i in range(0, 3):
            if st.button(str(i)):
                update_number(i)
    with col2:
        for i in range(3, 6):
            if st.button(str(i)):
                update_number(i)
    with col3:
        for i in range(6, 9):
            if st.button(str(i)):
                update_number(i)

    with col4:
        for op in ['9', 'sin ', 'cos ']:
            if st.button(op):
                update_number(op)

    with col5:
        for op in ['tan ', 'sec ', 'cot ']:
            if st.button(op):
                update_number(op)
        if st.button('Clear'):
            st.session_state.number_string = ""  

    # Display the current number string in a text box
    expression = st.text_area("Please enter expression:", value=st.session_state.number_string, height=100)
    return expression

