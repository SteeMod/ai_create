import streamlit as st

def main():
    st.title("Verify Accuracy")

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
     
        with col5:
            Zipcode = st.text_input("Zipcode")
    
        with col6:
            Phone = st.text_input("Phone")
        
        col7, col8 = st.columns(2)
    
        with col7:
            Allergy1 = st.text_input("Allergy1")
    
        with col8:
            Allergy2 = st.text_input("Allergy2")

        # Define the number of rows and columns for your table
        num_rows = 4  # Example: 4 rows
        num_columns = 7  
        column_names = ["Mark X", "Medication", "Dosage", "Frequency", "Form", "Route", "Instructions"]  # Column headers

        # Create a header row for column names
        header_cols = st.columns(num_columns)
        for col, col_name in zip(header_cols, column_names):
            col.write(col_name)

        # Create rows with input fields
        for row in range(num_rows):
            cols = st.columns(num_columns)  # Create columns for each row
            with cols[0]:
                st.text_input("Mark X", key=f"markx{row}")  # Unique key for each input
            with cols[1]:
                st.text_input("Medication", key=f"medname{row}")
            with cols[2]:
                st.text_input("Dosage", key=f"dosage{row}")
            with cols[3]:
                st.text_input("Frequency", key=f"freq{row}")
            with cols[4]:
                st.text_input("Form", key=f"form{row}")
            with cols[5]:
                st.text_input("Route", key=f"route{row}")
            with cols[6]:
                st.text_input("Instructions", key=f"instructions{row}")

        # Additional fields for medication intake progress
        MedicationName = st.text_input("MEDICATION NAME")
        Month = st.text_input("MONTH")
        Year = st.text_input("YEAR")

        # Form submission button
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.write("Form Submitted!")

if __name__ == "__main__":
    main()