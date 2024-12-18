import psycopg2

def connect_to_db():
    try:
        conn = psycopg2.connect(
            dbname="users_db", user="your_username", password="your_password", host="localhost", port="5432"
        )
        return conn
    except Exception as e:
        print(f"Connection error: {e}")
        return None

def create_user(username, email):
    conn = connect_to_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Users (username, email) VALUES (%s, %s) RETURNING id;", (username, email)
        )
        user_id = cursor.fetchone()[0]
        conn.commit()
        cursor.close()
        conn.close()
        return user_id
    return None

def create_message(user_id, content):
    conn = connect_to_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Messages (user_id, content) VALUES (%s, %s) RETURNING id;", (user_id, content)
        )
        message_id = cursor.fetchone()[0]
        conn.commit()
        cursor.close()
        conn.close()
        return message_id
    return None

def get_users():
    conn = connect_to_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, username, email FROM Users;")
        users = cursor.fetchall()
        cursor.close()
        conn.close()
        return users
    return []

def get_messages_by_user(user_id):
    conn = connect_to_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, content, created_at FROM Messages WHERE user_id = %s;", (user_id,))
        messages = cursor.fetchall()
        cursor.close()
        conn.close()
        return messages
    return []

def update_user(user_id, username=None, email=None):
    conn = connect_to_db()
    if conn:
        cursor = conn.cursor()
        if username:
            cursor.execute("UPDATE Users SET username = %s WHERE id = %s;", (username, user_id))
        if email:
            cursor.execute("UPDATE Users SET email = %s WHERE id = %s;", (email, user_id))
        conn.commit()
        cursor.close()
        conn.close()

def delete_user(user_id):
    conn = connect_to_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Users WHERE id = %s;", (user_id,))
        conn.commit()
        cursor.close()
        conn.close()

def delete_message(message_id):
    conn = connect_to_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Messages WHERE id = %s;", (message_id,))
        conn.commit()
        cursor.close()
        conn.close()
