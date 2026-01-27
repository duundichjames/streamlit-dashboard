import streamlit as st

# Selectbox
country = st.selectbox('Country', ['USA', 'Korea', 'UK', 'Japan'])
st.write(f'Country: {country}')

# Multiselect
interests = st.multiselect('Interests',
    ['Finance', 'Data Science', 'Web Dev', 'AI'])
st.write(f'Interests: {interests}')