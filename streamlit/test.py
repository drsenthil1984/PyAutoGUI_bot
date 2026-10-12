import streamlit as st 


st.title("BMI Calculator")
st.write("This is a simple BMI calculator.")
weight = st.number_input("Enter your weight (in kg):", min_value=0.0, max_value=300.0, step=0.1)
height = st.number_input("Enter your height (in meters):", min_value=0.0, max_value=3.0, step=0.01)
if st.button("Calculate BMI"):
    if height > 0:
        bmi = weight / (height ** 2)
        st.write(f"Your BMI is: {bmi:.2f}")
        if bmi < 18.5:
            st.write("You are underweight.")
        elif 18.5 <= bmi < 24.9:
            st.write("You have a normal weight.")
        elif 25 <= bmi < 29.9:
            st.write("You are overweight.")
        else:
            st.write("You are obese.")
    else:
        st.error("Height must be greater than zero to calculate BMI.")  
