import streamlit as st

def calculate_bmi(weight, height):
   
    bmi = weight / (height ** 2)
    return bmi

def main():

    st.title("BMI Calculator")
    weight = st.number_input("Enter your weight (in kg)", min_value=1)
    height = st.number_input("Enter your height (in meters)", min_value=0.1)

    if st.button("Calculate BMI"):
        if weight > 0 and height > 0:
            bmi = calculate_bmi(weight, height)
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
            st.write("Please enter valid values.")

if __name__ == "__main__":
    main()
