import json
import uuid
from typing import Optional
from datetime import datetime
import os

filename = 'db/users.json'

if not os.path.exists('db'):
    os.makedirs('db')

def read_all_users() -> dict:
    if not os.path.exists(filename): 
        with open(filename, mode='w') as f:
            json.dump({}, f) 
        return {}  

    with open(filename, mode='r') as f:
        users_db: dict = json.load(f)
        return users_db

def create_user(username: str, password: str, email: Optional[str] = None, is_active=False) -> str | None:
    users_db = read_all_users()
    
    user_id = str(uuid.uuid4())
    new_user = {
        "username": username,
        "password": password,
        "email": email,
        "is_active": is_active,
        "created_at": str(datetime.now())
    }
    
    users_db[user_id] = new_user
    with open(filename, mode='w') as f:
        json.dump(users_db, f, indent=4)
        return f"User {username} successfully created with UUID: {user_id}"

print(create_user('anna', 'admin123', 'anna@gmail.com'))

print(read_all_users()) 
