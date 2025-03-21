

import streamlit as st

name = st.text_input("Enter your name", "John Doe")
password = st.text_input("Enter your password", type="password")


if st.button("Submit"):
   if len(password) < 8:
       st.warning("Password must be at least 8 characters long")


   st.success("Password is valid")

# st.title('Hello World')
# st.write('This is a simple Streamlit app.')


# if st.button('Say hello'):
#    st.text('Hello, Streamlit!')


# name = st.text_input('Please enter your name:')
# if name:
#    st.write(f'Hello, {name}!')


# if st.file_uploader('Please upload a file:', type=['txt', 'csv']):
#    st.write('Thanks for uploading a file!')




