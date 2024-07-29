import streamlit as st

# Define the pages
pages = {
    "Page 1": page1,
    "Page 2": page2,
    "Page 3": page3
}

# Create a selectbox in the sidebar
page = st.sidebar.selectbox("Choose a page", list(pages.keys()))

# Call the appropriate page function
if page in pages and page != "Page 2":  # Deactivate Page 2
    pagespage
else:
    st.sidebar.text("This page is deactivated.")
