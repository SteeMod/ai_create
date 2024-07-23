import streamlit as st

def main():
    st.title("Verify Accuracy")

    with st.form("my_form"):
        # Use columns to place fields side by side
        col1, col2 = st.columns(2)
        FirstName = col1.text_input("FirstName")
        LastName = col2.text_input("LastName")
        Address = st.text_input("Address")
        City, State = st.columns(2)
        City = City.text_input("City")
        State = State.text_input("State")
        Zipcode, Phone = st.columns(2)
        Zipcode = Zipcode.text_input("Zipcode")
        Phone = Phone.text_input("Phone")
        Allergy1, Allergy2 = st.columns(2)
        Allergy1 = Allergy1.text_input("Allergy1")
        Allergy2 = Allergy2.text_input("Allergy2")

        # Medication details section
        col3, col4, col5 = st.columns(3)
        MedicationName = col3.st.text_input("MEDICATION NAME")
        Month = col4.st.text_input("MONTH")
        Year = col5.st.text_input("YEAR")
        
        # Medication table
        num_rows_medication = 4
        num_columns_medication = 7
        column_names_medication = ["Mark X", "Medication", "Dosage", "Frequency", "Form", "Route", "Instructions"]
        header_cols_medication = st.columns(num_columns_medication)
        for col, col_name in zip(header_cols_medication, column_names_medication):
            col.write(col_name)
        for row in range(num_rows_medication):
            cols = st.columns(num_columns_medication)
            for i, col in enumerate(cols):
                col.text_input(column_names_medication[i], key=f"{column_names_medication[i]}_{row}")

        # Medication intake progress section
        num_rows_progress = 31
        num_columns_progress = 7
        column_names_progress = ["Date", "Yes", "No", "Dosage", "Frequency", "Form", "Route"]
        header_cols_progress = st.columns(num_columns_progress)
        for col, col_name in zip(header_cols_progress, column_names_progress):
            col.write(col_name)
        for row in range(num_rows_progress):
            cols = st.columns(num_columns_progress)
            for i, col in enumerate(cols):
                col.text_input(column_names_progress[i], key=f"{column_names_progress[i]}_{row}_progress")

        
    NameofOTPProgram= st.text_input("OTP Program")
    Adress = st.text_input("OTP Adress")
    DoctororClinician = st.text_input("Doctor/Clinician Name")
    PharmacyName = st.text_input("Pharmacy Name")
    PharmacyPhone= st.text_input("Pharmacy Phone")

# Form submission button
    submitted = st.form_submit_button("Submit")
    if submitted:
            st.write("Form Submitted!")
if __name__ == "__main__":
    main()