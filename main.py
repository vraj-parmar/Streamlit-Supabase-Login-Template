import streamlit as st
from auth import create_account, login, reset_password

def create_account_page():
    with st.form(key='signup_form'):
        username = st.text_input("Email")
        password = st.text_input("Password", type="password")
        password_confirm = st.text_input("Confirm Password", type="password")
        submit_button = st.form_submit_button(label='Register')

        if submit_button:
            if password != password_confirm:
                st.error("Passwords do not match!")
            else:
                create_account(username, password)

def login_page():
    with st.form(key='login_form'):
        username = st.text_input("Email")
        password = st.text_input("Password", type="password")
        submit_button = st.form_submit_button(label='Login')

        if submit_button:
            logged_in = login(username, password)
            if logged_in:
                st.success("Welcome!")
                # Add additional logic here for after successful login

def reset_password_page():
    with st.form(key='reset_password_form'):
        username = st.text_input("Email")
        new_password = st.text_input("New Password", type="password")
        new_password_confirm = st.text_input("Confirm New Password", type="password")
        submit_button = st.form_submit_button(label='Reset Password')

        if submit_button:
            if new_password != new_password_confirm:
                st.error("Passwords do not match!")
            else:
                reset_password(username, new_password)

def main():
    st.title("Streamlit - Supabase Login")

    tabs = st.tabs(["Login", "Register", "Forgot password"])

    with tabs[0]:
        login_page()

    with tabs[1]:
        create_account_page()

    with tabs[2]:
        reset_password_page()

if __name__ == "__main__":
    main()
