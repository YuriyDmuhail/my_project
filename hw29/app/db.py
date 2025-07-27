import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="testdb",
        user="postgres",
        password="postgres",
        host="db",  # Docker service name
        port="5432"
    )

def create_table():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    name TEXT,
                    email TEXT
                )
            """)
            conn.commit()

def insert_user(name, email):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
            conn.commit()

def get_users():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM users")
            return cur.fetchall()

def update_user(user_id, name):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("UPDATE users SET name = %s WHERE id = %s", (name, user_id))
            conn.commit()

def delete_user(user_id):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM users WHERE id = %s", (user_id,))
            conn.commit()