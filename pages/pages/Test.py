import streamlit as st

# Sidebar
st.sidebar.title("Menu")
menu = st.sidebar.radio("Go to", ["Home", "About Us", "Contact Us"])

# Page contents
if menu == "Home":
    st.title("Re[Fresh]")
    st.write(
        "At Re[Fresh], we are dedicated to providing exceptional addiction treatment services in a welcoming and inclusive environment. Our team of experienced professionals is committed to helping individuals overcome addiction and achieve long-term. We believe in creating a stigma-free and stereotype-free space where everyone feels comfortable seeking the help they need."
    )
elif menu == "About Us":
    st.title("About Us")
    # You can add content for the About Us page here
elif menu == "Contact Us":
    st.title("Contact Us")
    # You can add content for the Contact Us page here
