# auth.py

from supabase import Client
import bcrypt
import streamlit as st
from supabase_connection import supabase

# Utility functions for hashing and checking passwords
def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def check_password(password: str, hashed: str) -> bool:
    return bcrypt.checkpw(password.encode(), hashed.encode())

# Create a new user account
def create_account(username: str, password: str):
    hashed_pw = hash_password(password)
    try:
        response = supabase.table('users').insert({"username": username, "password": hashed_pw}).execute()
        if response.status_code == 201:
            st.success("Account created successfully! You can now log in.")
        else:
            st.error("Error creating account.")
    except Exception as e:
        st.error(f"Error: {e}")

# Authenticate user login
def login(username: str, password: str):
    try:
        response = supabase.table('users').select('password').eq('username', username).execute()
        if response.data and check_password(password, response.data[0]['password']):
            st.success("Logged in successfully!")
            return True
        else:
            st.error("Invalid username or password")
            return False
    except Exception as e:
        st.error(f"Error: {e}")
        return False

# Reset user password
def reset_password(username: str, new_password: str):
    hashed_pw = hash_password(new_password)
    try:
        response = supabase.table('users').update({"password": hashed_pw}).eq('username', username).execute()
        if response.status_code == 200:
            st.success("Password reset successfully! You can now log in with your new password.")
        else:
            st.error("Failed to reset password. Please check your username.")
    except Exception as e:
        st.error(f"Error: {e}")
