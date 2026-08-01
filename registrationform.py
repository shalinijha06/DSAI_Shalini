import streamlit as st

st.set_page_config(page_title="Student Registration Form")

st.title("🎓 Student Registration Form")

with st.form("student_form"):

    # Student Details
    name = st.text_input("Student Name")
    roll_no = st.text_input("Roll Number")
    age = st.number_input("Age", min_value=16, max_value=35, step=1)
    father=st.text_input("father's name")
    email=st.text_input("email")
    mobile=st.text_input("mobile number")
    gender = st.radio("Gender", ["Male", "Female", "Other"])

    dob = st.date_input("Date of Birth")

    course = st.selectbox(
        "Course",
        ["B.Tech", "BCA", "B.Sc", "MCA", "MBA"]
    )

    branch = st.selectbox(
        "Branch",
        ["CSE", "IT", "ECE", "EEE", "Mechanical", "Civil"]
    )

    skills = st.multiselect(
        "Skills",
        ["Python", "Java", "C", "C++", "HTML", "CSS", "JavaScript", "SQL"]
    )

    email = st.text_input("Email")

    mobile = st.text_input("Mobile Number")

    address = st.text_area("Address")

    agree = st.checkbox("I confirm that all the information is correct.")

    col1, col2 = st.columns(2)

    with col1:
        submit = st.form_submit_button("Register")

    with col2:
        reset = st.form_submit_button("Reset")

# Registration
if submit:
    if (name == "" or roll_no == "" or email == "" or
        mobile == "" or address == ""):
        st.warning("Please fill all the required fields.")
    elif not agree:
        st.error("Please accept the declaration.")
    else:
        st.success("Student Registered Successfully!")
        st.balloons()

        st.subheader("Student Details")
        st.write("**Name:**", name)
        st.write("**Roll No:**", roll_no)
        st.write("**Age:**", age)
        st.write("**Gender:**", gender)
        st.write("**Date of Birth:**", dob)
        st.write("**Course:**", course)
        st.write("**Branch:**", branch)
        st.write("**Skills:**", ", ".join(skills))
        st.write("**Email:**", email)
        st.write("**Mobile:**", mobile)
        st.write("**Address:**", address)

# Reset
if reset:
    st.info("Form has been reset. Enter new details.")
                        