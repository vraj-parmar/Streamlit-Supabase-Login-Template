# app.py

import streamlit as st
from auth import create_account, login, reset_password

def create_account_page():
    st.header("Create New Account")

    with st.form(key='signup_form'):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        password_confirm = st.text_input("Confirm Password", type="password")
        submit_button = st.form_submit_button(label='Sign Up')

        if submit_button:
            if password != password_confirm:
                st.error("Passwords do not match!")
            else:
                create_account(username, password)

def login_page():
    st.header("Login")

    with st.form(key='login_form'):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit_button = st.form_submit_button(label='Login')

        if submit_button:
            logged_in = login(username, password)
            if logged_in:
                st.success("Welcome!")
                # Add additional logic here for after successful login

def reset_password_page():
    st.header("Reset Password")

    with st.form(key='reset_password_form'):
        username = st.text_input("Username")
        new_password = st.text_input("New Password", type="password")
        new_password_confirm = st.text_input("Confirm New Password", type="password")
        submit_button = st.form_submit_button(label='Reset Password')

        if submit_button:
            if new_password != new_password_confirm:
                st.error("Passwords do not match!")
            else:
                reset_password(username, new_password)

def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Choose an option", ["Login", "Create Account", "Reset Password"])

    if page == "Login":
        login_page()
    elif page == "Create Account":
        create_account_page()
    elif page == "Reset Password":
        reset_password_page()

if __name__ == "__main__":
    main()
