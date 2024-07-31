import streamlit as st

pg = st.navigation({
    "Overview": [
        
        # You can also load pages from files, as usual
        st.Page("0_Instructions.py", title="Instructions", icon=":material/movie_filter::"),

        st.Page("1_Download.py", title="Download File", icon=":material/movie_filter::"),
        st.Page("2_Upload.py", title="Upload", icon=":material/movie_filter::"),
        st.Page("3_Review,py", title="Review Acurracy", icon=":material/movie_filter::"),
        st.Page("4_Dashboard.py", title="My Dashboard", icon=":material/movie_filter::"),
        ],
})
pg.run()