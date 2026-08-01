import streamlit as st

st.set_page_config(page_title="Student Registration Form", layout="centered")
st.divider()
st.title("📋 STUDENT REGISTRATION FORM")
st.divider()
student_name = st.text_input("Student Name")
father_name = st.text_input("Father Name")
age = st.number_input("Age", min_value=1, max_value=100, step=1)

gender = st.radio(
    "Gender",
    ["Male", "Female"],
    horizontal=True
)

course = st.selectbox(
    "Course",
    ["Data Science", "Python", "Java", "AI & ML", "Web Development"]
)

address = st.text_area("Address", height=100)

if st.button("Submit"):
    st.success("Registration Successful!")

    st.subheader("Student Details")

    st.write("**Student Name:**", student_name)
    st.write("**Father Name:**", father_name)
    st.write("**Age:**", age)
    st.write("**Gender:**", gender)
    st.write("**Course:**", course)
    st.write("**Address:**", address)