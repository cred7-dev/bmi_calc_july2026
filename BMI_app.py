import streamlit as st
import google.genai as genai


google_api_key = st.secrets["google"]["api_key"]
c = genai.Client(api_key=google_api_key)

#title
st.title("BMI Calculator and AI Nutritionist")

#text input
weight = st.number_input("Enter your weight in kg")
height = st.slider("Enter your height in meters", min_value=1.0, max_value=2.5, step=0.01)
gender = st.selectbox("Select your gender",["Pick one","Male", "Female"])

#BMI calculate
bmi = weight / (height **2)

if st.button("Calculate BMI"):
    st.write(f"Your BMI is: {bmi:.2f}")

#AI
if st.button("Generate recommendations"):
    prompt = f"Act like a nutionist and give advice for a {gender} with height {height} meters and weight {weight} kg and a BMI of {bmi}. Keep it short and consise under 150 words"
    response = c.models.generate_content(model = "gemini-3.5-flash", contents = prompt)
    st.write(response.text)
