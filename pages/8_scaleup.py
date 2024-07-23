import streamlit as st

def main():
    st.title("Form with CSS-like Layout")

    with st.form("my_form"):
        # Use columns to place fields side by side
        col1, col2 = st.columns(2)
        
        with col1:
            FirstName = st.text_input("FirstName")
        
        with col2:
            LastName = st.text_input("LastName")
        
        Address = st.text_input("Address")
        
        col3, col4 = st.columns(2)
         
        with col3:
            City = st.text_input("City")
        
        with col4:
            State = st.text_input("State")
            col5, col6 = st.columns(2)

        col5, col6 = st.columns(2)
         
        with col5:
            Zipcode = st.text_input("Zipcode")
        
        with col6:
            Phone = st.text_input("Phone")
            
            col7, col8 = st.columns(2)
        
        with col7:
            Allergy1 = st.text_input("Allergy1")
        
        with col8:
            Allergy2 = st.text_input("Allergy2")
            
        # Form submission button
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.write("Form Submitted!")

if __name__ == "__main__":
    main()