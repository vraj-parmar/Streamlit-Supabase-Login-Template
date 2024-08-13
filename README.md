# Streamlit - Supabase Login Template

This project is a simple login UI built with Streamlit and Supabase. It provides functionality for user registration, login, and password reset using a Supabase database.

## Overview

The application allows users to:
- **Register**: Create a new account with a username and password.
- **Login**: Authenticate and log in with existing credentials.
- **Reset Password**: Change the password for an existing account.

## Project Structure

- `auth.py`: Contains functions for user authentication, password hashing, account creation, and password reset.
- `main.py`: The main Streamlit app that provides the user interface for registration, login, and password reset.
- `supabase_connection.py`: Handles the connection to the Supabase database.
- `requirements.txt`: Lists the project dependencies.
- `secrets.toml`: Stores sensitive information such as Supabase URL and key.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/vraj-parmar/Streamlit-Supabase-Login-Template.git
   cd Streamlit-Supabase-Login-Template
   ```

2. **Set Up a Virtual Environment (Optional but recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Supabase:**

   - Create a Supabase project and set up a table named `users` with columns `username` and `password`.
   - Update `secrets.toml` with your Supabase credentials:

     ```toml
     SUPABASE_URL = "https://your-supabase-url.supabase.co"
     SUPABASE_KEY = "your-supabase-key"
     ```

## Usage

1. **Run the Application:**

   ```bash
   streamlit run main.py
   ```

2. **Access the Application:**

   Open your web browser and navigate to `http://localhost:8501` to interact with the login UI.

## Functions

- **create_account(username: str, password: str)**: Creates a new user account with a hashed password.
- **login(username: str, password: str)**: Authenticates a user and logs them in if the credentials are correct.
- **reset_password(username: str, new_password: str)**: Updates the password for an existing user.

## Troubleshooting

- **Ensure Supabase Credentials Are Correct**: Double-check the `secrets.toml` file for the correct Supabase URL and key.
- **Database Table**: Make sure the `users` table exists in your Supabase project with the correct schema.

---

Happy coding!

### Notes:
- Make sure to adjust the URL and key in the `secrets.toml` to match your actual Supabase credentials.
- You may also want to add details about how to handle errors, logs, or any specific requirements for running the project.
