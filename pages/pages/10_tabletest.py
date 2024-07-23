import streamlit as st

def main():
    st.title("Form with Table-like Layout")

    with st.form("my_form"):
        # Define the number of rows and columns for your table
        num_rows = 4  # Example: 4 rows
        num_columns = 7  
        column_names = ["Mark X", "Medication", "Dosage", "Frequency", "Form", "Route" "Instructions"]  # Column headers

        # Create a header row for column names
        header_cols = st.columns(num_columns)
        for col, col_name in zip(header_cols, column_names):
            col.write(col_name)

        # Create rows with input fields
        for row in range(num_rows):
            cols = st.columns(num_columns)  # Create columns for each row
            with cols[0]:
                st.text_input("Mark X", key=f"fn{row}")  # Unique key for each input
            with cols[1]:
                st.text_input("Medname", key=f"medname{row}")
            with cols[2]:
                st.text_input("Dosage", key=f"addr{row}")
            with cols[3]:
                st.text_input("Frequency", key=f"freq{row}")
            with cols[4]:
                st.text_input("Form", key=f"form{row}")
            with cols[5]:
                st.text_input("Route", key=f"route{row}")
            with cols[6]:
                st.text_input("Instructions", key=f"instructions{row}")
        # Form submission button
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.write("Form Submitted!")

if __name__ == "__main__":
    main()