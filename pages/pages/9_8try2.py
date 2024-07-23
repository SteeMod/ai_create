import streamlit as st

def main():
    st.title("Form with Dynamic Table Input")

    with st.form("my_form"):
        # Use columns to place fields side by side for the table header
        st.write("Table Input:")
        col_names = ["FirstName", "LastName", "Address", "City"]
        cols = st.columns(len(col_names))
        for col, col_name in zip(cols, col_names):
            col.write(col_name)

        # Dynamic row addition
        num_rows = st.number_input("How many rows do you want to add?", min_value=0, value=1, step=1)
        table_data = []
        for i in range(num_rows):
            row = []
            cols = st.columns(len(col_names))
            for col in cols:
                # For simplicity, using text_input for all columns, you can customize this based on column type
                row_value = col.text_input("", key=f"{i}{col}")  # Unique key for each input
                row.append(row_value)
            table_data.append(row)

        # Form submission button
        submitted = st.form_submit_button("Submit")
        if submitted:
            # Process the table data
            st.write("Table Data Submitted:")
            for row in table_data:
                st.write(row)

if __name__ == "__main__":
    main()