import json

users = [
    {
        "username": "dmin",
        "password": "123",
        "is_active": True
    },
    {
        "username": "john",
        "password": "admin123",
        "is_active": False
    }
]

with open('users.json', 'w') as f:
    json.dump(users, f, indent=4)

def one_user_get(username):
    with open('users.json', 'r') as f:
        users = json.load(f)
    for user in users:
        if user['username'] == username:
            return user
    return None

def create_user(username, password, is_active=True):
    new_user = {
        "username": username,
        "password": password,
        "is_active": is_active
    }
    
    with open('users.json', 'r+') as f:
        users = json.load(f)
        if any(user['username'] == username for user in users):
            return f"Foydalanuvchi {username} allaqachon mavjud!"
        
        users.append(new_user)
        f.seek(0) 
        json.dump(users, f, indent=4)
        return f"Foydalanuvchi {username} muvaffaqiyatli qo'shildi!"

def update_user(username, new_data):
    with open('users.json', 'r+') as f:
        users = json.load(f)
        for user in users:
            if user['username'] == username:
                user.update(new_data)
                break
        else:
            return f"Foydalanuvchi {username} topilmadi!"
        
        f.seek(0)
        f.truncate() 
        json.dump(users, f, indent=4)
        return f"Foydalanuvchi {username} muvaffaqiyatli yangilandi!"

def delete_user(username):
    with open('users.json', 'r+') as f:
        users = json.load(f)
        new_users = [user for user in users if user['username'] != username]
        
        if len(users) == len(new_users):
            return f"Foydalanuvchi {username} topilmadi!"
        
        f.seek(0)
        f.truncate()
        json.dump(new_users, f, indent=4)
        return f"Foydalanuvchi {username} muvaffaqiyatli o'chirildi!"

def show_all_users():
    with open('users.json', 'r') as f:
        users = json.load(f)
        for user in users:
            print(user)

print(create_user('alice', 'mypassword'))
print(update_user('john', {'password': 'newpass'}))
print(delete_user('dmin'))
show_all_users()
