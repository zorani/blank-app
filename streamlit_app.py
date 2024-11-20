import streamlit as st

# Title of the app
st.title("Hello, World!")

# Displaying text
st.write("Welcome to your first Streamlit app! 🎉")

# Adding a button
if st.button("Click Me"):
    st.write("Button clicked! Hello again!")

# Adding an input field
name = st.text_input("What's your name?")
if name:
    st.write(f"Hello, {name}!")

