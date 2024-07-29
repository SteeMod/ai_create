import streamlit as st
st.title("Re[Fresh]")


# Split the text into two parts for the two columns
text = "At Re[Fresh], we are dedicated to providing exceptional addiction treatment services in a welcoming and inclusive environment. Our team of experienced professionals is committed to helping individuals overcome addiction and achieve long-term. We believe in creating a stigma-free and stereotype-free space where everyone feels comfortable seeking the help they need. Contact us today to learn more about our personalized treatment and start your journey towards a healthier, happier life."
text_parts = text.split(". ", 2)

# Create two columns
col1, col2 = st.beta_columns(2)

# Write the text to the columns
col1.write(text_parts[0] + ".")
col2.write(text_parts[1])

