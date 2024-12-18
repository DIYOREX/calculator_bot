import sqlite3
from colorama import Fore, init

init(autoreset=True)
import hashlib


conn = sqlite3.connect("database.db")


def commit(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        conn.commit()
        return result
    return wrapper


class CharField:
    def __init__(self, max_length=255):
        self.max_length = max_length


class PasswordField:
    def __init__(self, max_length=128):
        self.max_length = max_length

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()


class PhoneNumberField:
    def __init__(self):
        pass 

class User:
    username = CharField(max_length=255) 
    phone_number = PhoneNumberField() 
    password = PasswordField(max_length=128) 

    def __init__(self, username, phone_number, password):
        self.username = username
        self.phone_number = phone_number
        self.password = self.password.hash_password(password) 

    @commit
    def save(self):
        """Save the user to the database."""
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (username, phone_number, password) VALUES (?, ?, ?)",
            (self.username, self.phone_number, self.password),
        )


def create_user_table():
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        phone_number TEXT NOT NULL,
        password TEXT NOT NULL
    )
    """)
    conn.commit()


if __name__ == "__main__":
    create_user_table() 

    user = User(username="JohnDoe", phone_number="+123456789", password="securepassword123")
    user.save()

    print(Fore.GREEN+"User saved successfully!")
