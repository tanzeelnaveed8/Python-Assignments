import streamlit as st
import re

st.set_page_config(page_title="Password Strength Checker", page_icon="🔒")

st.title("🔐 Password Strength Checker")
st.markdown(""" 
## Welcome to the Ultimate Password Strengthener ⚡
This app analyzes the strength of your password and provides tailored suggestions for improvement.
At **Password Strength Checker**, we prioritize your privacy and security. **We do not store any passwords entered into this app.**
Our goal is to help you create **stronger, more secure passwords** by offering the best possible recommendations.
""")

# User input
password = st.text_input("Enter your password here", type="password")

# Initialize feedback list and score
feedback = []
score = 0

# Password strength checks
if len(password) < 8:
    feedback.append("❌ Password should be at least **8 characters** long.")
else:
    score += 1

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Password should contain **at least one uppercase and one lowercase letter**.")

    if re.search(r"\d", password):  # Corrected digit check
        score += 1
    else:
        feedback.append("❌ Password should contain **at least one digit**.")

    if re.search(r"[!@#$%^&*()_+{}|:<>?]", password):
        score += 1
    else:
        feedback.append("❌ Password should contain **at least one special character** (e.g., @, #, $).")

# Provide feedback based on score
if score == 4:
    feedback.append("✅ **Your password is strong. Great job!**")
elif score == 3:
    feedback.append("⚠ **Your password is medium strength. Consider adding a special character.**")
else:
    feedback.append("🔴 **Your password is weak. Consider adding an uppercase letter, a digit, and a special character.**")

# Display feedback
if password:
    st.markdown("### 🔍 Password Strength Suggestions")
    for tip in feedback:
        st.write(tip)
else:
    st.write("Enter a password to get started.")
