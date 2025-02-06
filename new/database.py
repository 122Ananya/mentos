import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

DB_NAME = "mental_health.db"


# Function to establish a database connection
def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row  # Enables dictionary-like access
    return conn


# Function to initialize the database with required tables
def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    with open("schema.sql", "r") as f:
        cursor.executescript(f.read())  # Execute schema.sql file

    conn.commit()
    conn.close()
    print("Database initialized successfully.")


# Function to execute a query (INSERT, UPDATE, DELETE)
def execute_query(query, params=()):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query, params)
    conn.commit()
    conn.close()


# Function to fetch a single record
def fetch_one(query, params=()):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query, params)
    result = cursor.fetchone()
    conn.close()
    return result


# Function to fetch multiple records
def fetch_all(query, params=()):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query, params)
    results = cursor.fetchall()
    conn.close()
    return results


def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


# Function to register a new user
def register_user(username, password):
    conn = get_db_connection()
    cursor = conn.cursor()

    hashed_password = generate_password_hash(password)  # Hash the password
    try:
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, hashed_password)
        )
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError:
        return False  # Username or email already exists


# Function to authenticate user login
def authenticate_user(username, password):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    conn.close()

    if user and check_password_hash(user["password"], password):
        return user["username"]  # Login successful
    return False  # Login failed


if __name__ == "__main__":
    init_db()  # Run this script once to initialize the database
