import json

class User:
    users_database = []
    
    def __init__(self, username, phone, password):
        self.username = username
        self.phone = phone
        self.password = password
    
    def save_user(self):
        User.users_database.append({
            'username': self.username,
            'phone': self.phone,
            'password': self.password
        })
        with open("users.json", "w") as file:
            json.dump(User.users_database, file, indent=4)
        return "Foydalanuvchi muvaffaqiyatli qo'shildi."

    @classmethod
    def create_user(cls, username, phone, password):
        if not username or not phone or not password:
            return "Hamma ma'lumotlar kiritilishi kerak."
        user = cls(username, phone, password)
        return user.save_user()

print(User.create_user("Diyorbek", "+998901234567", "my_secure_password"))
