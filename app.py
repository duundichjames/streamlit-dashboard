import streamlit as st
st.title('🎯 My First Streamlit App')
st.write('Welcome to Streamlit!')
# Simple slider
age = st.slider('How old are you?', 0, 100, 25)
st.write(f'You are {age} years old')
# Simple button
if st.button('Click me'):
    st.write('Button clicked!')