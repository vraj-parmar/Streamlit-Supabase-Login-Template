# supabase_connection.py

from supabase import create_client, Client
import streamlit as st

# Initialize connection to Supabase
def init_supabase() -> Client:
    SUPABASE_URL = st.secrets["SUPABASE_URL"]
    SUPABASE_KEY = st.secrets["SUPABASE_KEY"]
    return create_client(SUPABASE_URL, SUPABASE_KEY)

supabase = init_supabase()
