import streamlit as st

def main_page():
    st.title("Main Page")
    st.write("You are in the main page.")

def hidden_page():
    st.title("Hidden Page")
    st.write("You are in the hidden page.")

if st.button('Go to Hidden Page'):
    hidden_page()
else:
    main_page()
