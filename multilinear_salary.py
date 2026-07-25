import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

st.title("Experience to Salary Prediction")

df = pd.read_csv("multiple_linear_salary_dataset_50_records.csv")

X = df[["Experience", "Education_Level", "Age"]]
y = df["Salary"]

model = LinearRegression()
model.fit(X, y)

experience = st.slider("Experience", 0, 20, 5)

education = st.number_input(
    "Education Level",
    min_value=1,
    max_value=12,
    value=3
)

age = st.slider("Age", 18, 60, 25)

if st.button("Predict Salary"):
    predicted_salary = model.predict([[experience, education, age]])[0]
    st.subheader("Predicted Salary")
    st.success(f"₹ {predicted_salary:,.2f}")