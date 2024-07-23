import streamlit as st

def main():
    st.title("Form with Table-like Layout")

    with st.form("my_form"):
        # Define the number of rows and columns for your table
        num_rows = 3  # Example: 3 rows
        num_columns = 4  # Example: 4 columns (FirstName, LastName, Address, City)
        column_names = ["FirstName", "LastName", "Address", "City"]  # Column headers

        # Create a header row for column names
        header_cols = st.columns(num_columns)
        for col, col_name in zip(header_cols, column_names):
            col.write(col_name)

        # Create rows with input fields
        for row in range(num_rows):
            cols = st.columns(num_columns)  # Create columns for each row
            with cols[0]:
                st.text_input("First Name", key=f"fn{row}")  # Unique key for each input
            with cols[1]:
                st.text_input("Last Name", key=f"ln{row}")
            with cols[2]:
                st.text_input("Address", key=f"addr{row}")
            with cols[3]:
                st.text_input("City", key=f"city{row}")

        # Form submission button
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.write("Form Submitted!")

if __name__ == "__main__":
    main()