import streamlit as st
from supabase import create_client, Client

# Initialize connection to Supabase
SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_KEY = st.secrets["SUPABASE_KEY"]

# Create a client to interact with Supabase
def init_supabase():
    return create_client(SUPABASE_URL, SUPABASE_KEY)

conn = init_supabase()

# Use the connection
data = conn.table("users").select("*").execute()

st.write(data)
