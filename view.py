import streamlit as st

def get_user_input():
    st.sidebar.header("Calculator Input")
    options=['Trigonometric','Bodmas','Calculus']
    user_choice=st.sidebar.radio('Please select the type of expression to solve:',options)
    if user_choice=='Trigonometric':
        st.write("Trigonometric Functions Table")
        st.table({
                "Function": ["sin", "cos", "tan", "cosec", "arcsin"],
                "Description": [
                    "Sine of the angle",
                    "Cosine of the angle",
                    "Tangent of the angle",
                    "Cosecant (1/sin) of the angle",
                    "Inverse sine of the angle"
                ]
            })
            
        trig_functions = ['sin', 'cos', 'tan', 'cosec', 'arcsin']
        selected_function = st.sidebar.selectbox("Select a function:", trig_functions)
        expression = selected_function +' '+ str(st.sidebar.number_input("Enter the angle (in degrees):"))
        
        
    
    elif user_choice=='Bodmas':
        expression = st.sidebar.text_input("Please enter problem")

    elif user_choice=='Calculus':
        expression=st.write('This feature is not yet available')
        
    return expression,user_choice
