import streamlit as st
import streamlit as st
from PIL import Image
st.title("About[Me]")
st.write(
    "Stephen Modimakwane is a  Management Information Systems Specialist with over 18 years of experience in the field. I focus on Data Analytics, Data Visualization, and AI Infusion. I have a passion for creating data-driven solutions that help organizations."
)


import streamlit as st
from PIL import Image

# Load the image
image = Image.open('/workspaces/ai_create/photo.jpg.jpg')

# Display the image
st.image(image, caption='Your Image Caption', use_column_width=True)
