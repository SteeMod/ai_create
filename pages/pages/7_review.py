import streamlit as st
import pandas as pd
# Load CSV data into a DataFrame
def load_csv_data(filename):
    return pd.read_csv(filename)
# Generate and pre-populate the form based on the CSV data
def generate_form(df, row_index=0):
    if df.empty or row_index >= len(df):
        st.write("No data found in CSV or index out of range")
        return
    row_data = df.iloc[row_index]
    form = st.form(key='csv_form')
    fields = {}
    for column in df.columns:
        fields[column] = form.text_input(column, value=row_data[column])
    submit_button = form.form_submit_button(label='Submit')
    if submit_button:
        st.write("Form submitted")
        # Here you can handle the form submission (e.g., save the edited data)
        # For demonstration, we'll just display the submitted values
        for column, value in fields.items():
            st.write(f"{column}: {value}")
# Main function to control the app
def main():
    st.title("CSV to Web Form")
    # Specify your CSV file path here
    csv_file = 'out1.csv'
    df = load_csv_data(csv_file)
    generate_form(df)
if __name__ == "__main__":
    main()