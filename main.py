import streamlit as st
from st_supabase_connection import SupabaseConnection

# Initialize connection.
conn = st.connection("supabase",type=SupabaseConnection)

# Example usage
if conn.is_connected():
    data = conn.get_table("users").select("*").execute()
    st.write(data)
else:
    st.error("Failed to connect to Supabase.")