import streamlit as st
import hashlib
from cryptography.fernet import Fernet

# ---- Setup ----
master_key = Fernet.generate_key()
cipher_suite = Fernet(master_key)

stored_data = {}
users = {"admin": "admin123"}
MAX_ATTEMPTS = 3

# ---- Helper Functions ----
def hash_passkey(passkey):
    return hashlib.sha256(passkey.encode()).hexdigest()

def encrypt_text(text):
    return cipher_suite.encrypt(text.encode()).decode()

def decrypt_text(encrypted_text):
    return cipher_suite.decrypt(encrypted_text.encode()).decode()

def reset_attempts():
    st.session_state['attempts'] = 0
    st.session_state['authorized'] = False

# ---- Streamlit Config ----
st.set_page_config(page_title="Secure Data Storage", page_icon="🛡️", layout="centered")

# Initialize session state
if 'attempts' not in st.session_state:
    st.session_state['attempts'] = 0
if 'authorized' not in st.session_state:
    st.session_state['authorized'] = True

# ---- UI Styling ----
st.markdown("""
    <style>
    .title {
        text-align: center;
        font-size: 36px;
        font-weight: bold;
        margin-bottom: 20px;
        color: #4CAF50;
    }
    .subtitle {
        text-align: center;
        font-size: 24px;
        margin-bottom: 20px;
        color: #555;
    }
    .stButton > button {
        width: 100%;
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
    }
    .stTextInput > div > input {
        border: 1px solid #ccc;
        padding: 8px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">🛡️ Secure Data Encryption System</div>', unsafe_allow_html=True)

# ---- Pages ----
menu = st.sidebar.selectbox("📄 Navigate", ["Home", "Insert Data", "Retrieve Data", "Login"])

# ---- Login Page ----
if menu == "Login":
    st.markdown('<div class="subtitle">🔐 Login Page</div>', unsafe_allow_html=True)
    username = st.text_input("👤 Username")
    password = st.text_input("🔒 Password", type="password")
    if st.button("Login"):
        if username in users and users[username] == password:
            st.success("✅ Login successful!")
            st.session_state['authorized'] = True
            reset_attempts()
        else:
            st.error("❌ Invalid credentials!")

# ---- Home Page ----
elif menu == "Home":
    st.markdown('<div class="subtitle">🏠 Welcome to Secure Data Storage</div>', unsafe_allow_html=True)
    st.info("➡️ Use the sidebar to insert new data or retrieve stored data securely.")

# ---- Insert Data Page ----
elif menu == "Insert Data":
    st.markdown('<div class="subtitle">📝 Insert New Data</div>', unsafe_allow_html=True)

    if st.session_state['authorized']:
        data = st.text_area("🖋️ Enter the text you want to store:")
        passkey = st.text_input("🔑 Enter a passkey to secure your data:", type="password")
        
        if st.button("Store Data"):
            if data and passkey:
                encrypted_text = encrypt_text(data)
                hashed_passkey = hash_passkey(passkey)
                stored_data[data] = {"encrypted_text": encrypted_text, "passkey": hashed_passkey}
                st.success("✅ Your data has been stored securely!")
            else:
                st.error("❗ Please enter both text and passkey.")
    else:
        st.warning("⚠️ Please login to insert data.")
        st.page_link("Login", label="🔗 Go to Login Page")

# ---- Retrieve Data Page ----
elif menu == "Retrieve Data":
    st.markdown('<div class="subtitle">🔍 Retrieve Stored Data</div>', unsafe_allow_html=True)

    if st.session_state['authorized']:
        if stored_data:
            selected_data = st.selectbox("📂 Select the stored data:", list(stored_data.keys()))
            passkey = st.text_input("🔑 Enter your passkey to decrypt:", type="password")
            
            if st.button("Retrieve Data"):
                if selected_data and passkey:
                    stored_passkey = stored_data[selected_data]["passkey"]
                    user_passkey = hash_passkey(passkey)

                    if stored_passkey == user_passkey:
                        decrypted_text = decrypt_text(stored_data[selected_data]["encrypted_text"])
                        st.success(f"🟢 Decrypted Data: {decrypted_text}")
                        st.session_state['attempts'] = 0
                    else:
                        st.session_state['attempts'] += 1
                        st.error(f"❗ Wrong passkey! Attempts left: {MAX_ATTEMPTS - st.session_state['attempts']}")
                        if st.session_state['attempts'] >= MAX_ATTEMPTS:
                            st.warning("🚨 Maximum attempts reached! Please login again.")
                            st.session_state['authorized'] = False
                            st.switch_page("Login")
        else:
            st.info("ℹ️ No data available yet.")
    else:
        st.warning("⚠️ Please login to retrieve data.")
        st.page_link("Login", label="🔗 Go to Login Page")
