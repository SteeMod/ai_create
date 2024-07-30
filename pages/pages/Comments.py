import streamlit as st

# This will hold the comments. In a real-world application, consider using a database.
comments = []

st.title('Comment Section')

new_comment = st.text_input('Write a comment')
if new_comment:
    comments.append(new_comment)  # Add the new comment to the list of comments

# Display comments in reverse order
for comment in reversed(comments):
    st.markdown(f'---\n**{comment}**')
