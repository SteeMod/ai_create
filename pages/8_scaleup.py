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
        
        with st.form ("Medication Intake"):
            col1row4, col2row4, col3row4, col4row4, col5row4=st.colums(5)
            with col1row4:
                st.text_input("Medicationcheckmark")
            with col2row4: 
                st.text_input("MedicationName")
        # Form submission button
                submitted = st.form_submit_button("Submit")
        if submitted:
            st.write("Form Submitted!")

if __name__ == "__main__":
    main()