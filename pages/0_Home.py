import streamlit as st
st.title("MedicationTracker")
st.write("The latest technology [AI] is making working with the oldest technology[pen and paper] a whole lot easier. The Medication Tracker utilizes Azure AI Document Intelligence to extract medication tracker data from PDF file and save as digital data. I have developed  a simple form to track medication intake by using pen and paper. This is hassle free and more natural way of tracking progress on intake rather than ‘tinkering’ with digital devices which often need WIFI, power, internet, subscription to operate. When its all done you will need one though to upload the PDF :)Please follow instructions to test how well the solution extracts data from raw to digital.  There is a Review stage to check accuracy of the output, particularly hand written recording. Remember to use FICTITIOUS information as this solutions is STRICTLY for testing purposes and is not configured for secure connections and data privacy. Alternatively, you can download an already filled out form and use it for testing.  Please remember to leave some comments on the review section or via email.")
import streamlit as st
st.title("Instructions")
st.header("Follow exact instructions")
st.subheader("Step 1.")
st.write("First go to the download page and either download or print the form you select. Completed sample forms are provided to make testing quicker (download and upload), however, you can print the form and fill it out This is a test so do not use any real information use pseudo information to fill the form.")
st.subheader("Step 2.")
st.write("After filling the form, Go to the upload page and select your filled form and click submit. If there are no error messages that means it has been uploaded move on to the review page")
st.subheader("Step 3.")
st.write("Go to the review Page to check accuracy and edit the form accordingly *Note that innacuracies may be caused by ineligible handwriting* If you don't take medication everyday replace :unselected: fileds with nan to insure accuracy")
st.subheader("Step 4")
st.write("Go to your Dashboard to view your results.")
st.header("Final Step")
st.write("Leave a comment")

