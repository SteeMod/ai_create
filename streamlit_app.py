import streamlit as st

# Function to hide the page
def hide_page():
    st.experimental_set_query_params(hidden="true")
    st.write("The page is now hidden.")

st.title("Medication Tracker")
st.write("Welcome and thank you for testing this app! 😊")
st.write("Kindly go to the Home Page, on mobile you should see a symbol like this <, tap on it")

# Button to hide the page
if st.button("Hide Page"):
    hide_page()

if __name__ == "__main__":
    main()