import streamlit as st

pg = st.navigation({
    "Overview": [
        
        # You can also load pages from files, as usual
        st.Page("0_Instructions.py", title="Instructions", icon=":🔢:"),

        st.Page("1_Download.py", title="Download File", icon=":⬇️:"),
        st.Page("2_Upload.py", title="Upload", icon=":⬆️:"),
        st.Page("3_Review,py", title="Review Acurracy", icon=":null:"),
        st.Page("4_Dashboard.py", title="My Dashboard", icon=":null:"),
        ],
})
pg.run()