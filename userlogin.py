import streamlit as st
st.title("user login form")
uid=st.text_input("user id:-")
pswd=st.text_input("password",type="password")
gender=st.radio("Gender",["Male","Female"])
skills = st.multiselect("Skills",["Python","Java"])
course = st.selectbox("Course",["Python","AI"]) 
age = st.slider("Age",0,100)
age = st.number_input("Age") 
msg = st.text_area("Feedback")
name = st.text_input("Name") 
st.divider() 
st.button("login")
st.button("reset")
agree=st.checkbox("I Agree")

st.set_page_config(page_title="student registration form",page_icon