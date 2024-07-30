import streamlit as st
import pandas as pd

# Create a dataframe to store comments and ratings
# This should ideally be replaced with a persistent storage
df = pd.DataFrame(columns=["Comment", "Rating"])

# Display existing comments and ratings
if not df.empty:
    st.markdown("## Comments and Ratings")
    for index, row in df.iterrows():
        st.markdown(f"**Comment:** {row['Comment']}")
        st.markdown(f"**Rating:** {'⭐' * int(row['Rating'])}")
        st.markdown("---")

# Create a text input for the comment
comment = st.text_input("Enter your comment")

# Create a selectbox for the rating
rating = st.selectbox("Rate us", list(range(1, 6)))

# Create a button to submit the comment and rating
if st.button("Submit"):
    # Append the comment and rating to the dataframe
    df = df.append({"Comment": comment, "Rating": rating}, ignore_index=True)
    
    # Clear the input fields after submission
    st.empty()
