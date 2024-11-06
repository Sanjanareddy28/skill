# --- Input for Author Information ---
st.sidebar.header("Visualization Skill Workshop - Plotly")
name = st.sidebar.text_input("Enter your name", placeholder="Sanjana")
usn = st.sidebar.text_input("Enter your roll no.", placeholder="USN123456")
instructor_name = st.sidebar.text_input("Enter Instructor's name", placeholder="Dr. Smith")

# Display author information if all fields are filled
if name and usn and instructor_name:
    st.markdown(
        f"<h5 style='color: #FF6347;'>Created by:</h5>"  # Tomato red color for header
        f"<p style='color: #FFD700;'>Name: {name} (USN: {usn})</p>"  # Golden color for name & USN
        f"<p style='color: #32CD32;'>Instructor: {instructor_name}</p>",  # Lime green for instructor name
        unsafe_allow_html=True
    )
else:
    st.sidebar.warning("Please enter your name, roll number, and instructor's name.")
