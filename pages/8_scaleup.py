import streamlit as st

def main():
    st.title("Form with CSS-like Layout")

    with st.form("my_form"):
        # Use columns to place fields side by side
        col1, col2 = st.columns(2)
        
        with col1:
            first_name = st.text_input("FirstName")
        
        with col2:
            last_name = st.text_input("LastName")
        
        # Continue with other fields
        address = st.text_input("Address")
        city = st.text_input("City")
        # Add more fields as needed
        
        # Form submission button
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.write("Form Submitted!")

if __name__ == "__main__":
    main()