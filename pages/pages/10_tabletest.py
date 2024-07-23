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
        MedicationName, Month, Year = st.columns(3)
        MedicationName = MedicationName.text_input("MEDICATION NAME")
        Month = Month.text_input("MONTH")
        Year = Year.text_input("YEAR")
        
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
 
        
        # Medication details section
        OTPName, OTPClinician, OTPphone= st.columns(3)
        OTPName = OTPName.text_input("OTPName")
        OTPClinician=OTPClinician.text_input("OTPClinician")
        OTPphone = OTPphone.text_input("OTPphone")
        OTPAdress= st.text_input("OTPAdress")  

        PharmacyName, PharmacyPhone = st.columns(2)
        PharmacyName=PharmacyName.text_input("PharmacyName")
        PharmacyPhone=PharmacyPhone.text_input("PharmacyPhone")
        
        # Form submission button
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.write("Form Submitted!")
if __name__ == "__main__":
    main()