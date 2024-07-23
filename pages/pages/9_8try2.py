import streamlit as st

def main():
    st.title("Form with CSS-like Layout")

    with st.form("my_form"):
        # Use columns to place fields side by side
        col1row1, col2row1 = st.columns(2)
        
        with col1row1:
            first_name = st.text_input("FirstName")
        
        with col2row1:
            last_name = st.text_input("LastName")
        
        # House address in a new row, no need for columns if it spans the full width
        house_address = st.text_input("HouseAddress")
        
        # Form submission button
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.write("Form Submitted!")

if __name__ == "__main__":
    main()