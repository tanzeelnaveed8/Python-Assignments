import streamlit as st

st.title("🌐 Unit Converter App")
st.markdown("### Converts Length, Weight, and Time Instantly")

# Category selection
category = st.selectbox("Choose a Category", ["Length", "Weight", "Time"])

# Define conversion function
def convert_units(category, value, unit):
    if category == "Length":
        if unit == "Kilometers to Miles":
            return value * 0.621371
        elif unit == "Miles to Kilometers":
            return value / 0.621371

    elif category == "Weight":
        if unit == "Kilograms to Pounds":
            return value * 2.20462
        elif unit == "Pounds to Kilograms":
            return value / 2.20462

    elif category == "Time":
        if unit == "Seconds to Minutes":
            return value / 60
        elif unit == "Minutes to Seconds":
            return value * 60
        elif unit == "Minutes to Hours":
            return value / 60
        elif unit == "Hours to Minutes":
            return value * 60
        elif unit == "Hours to Days":
            return value / 24
        elif unit == "Days to Hours":
            return value * 24

# Define unit options based on category selection
if category == "Length":
    unit = st.selectbox("📏 Select Conversion", ["Kilometers to Miles", "Miles to Kilometers"])
elif category == "Weight":
    unit = st.selectbox("⚖️ Select Conversion", ["Kilograms to Pounds", "Pounds to Kilograms"])
elif category == "Time":
    unit = st.selectbox("⏰ Select Conversion", ["Seconds to Minutes", "Minutes to Seconds", "Minutes to Hours", "Hours to Minutes", "Hours to Days", "Days to Hours"])

# Input field for value to convert
value = st.number_input("Enter the value to convert", min_value=0.0, format="%.2f")

# Convert button
if st.button("Convert"):
    if value:
        result = convert_units(category, value, unit)
        if result is not None:
            st.success(f"The result is {result:.2f}")
        else:
            st.error("Invalid conversion")
    else:
        st.warning("Please enter a valid number")
