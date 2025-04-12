import streamlit as st

def main():
   
    st.title("Welcome to My Python Website")


    st.header("About This Website")
    st.write("This is a simple web application built using Streamlit. "
             "You can enter your name, and I'll greet you!")

    name = st.text_input("Enter your name:")

 
    if st.button("Say Hello"):
        if name:
            st.write(f"Hello, {name}! Welcome to my Streamlit website!")
        else:
            st.write("Hello, stranger! Welcome to my Streamlit website!")

    age = st.slider("Select your age", 0, 100, 25)
    st.write(f"You selected age: {age}")

    color = st.selectbox("What's your favorite color?", ["Red", "Green", "Blue", "Yellow"])
    st.write(f"Your favorite color is: {color}")

    subscribe = st.checkbox("Subscribe to our newsletter")
    if subscribe:
        st.write("Thanks for subscribing!")

    st.image("https://via.placeholder.com/300", caption="Sample Image", use_column_width=True)


    st.markdown("### Contact Us")
    st.write("Email: contact@mywebsite.com")

if __name__ == "__main__":
    main()
