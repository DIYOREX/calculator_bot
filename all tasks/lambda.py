users = [
    {
        'username': 'sara',
        'password': 'sara06',
        'login_try_count': 0,
        'is_active': False
    },
    {
        'username': 'mechael',
        'password': 'mechael06',
        'login_try_count': 0,
        'is_active': False
    },
    {
        'username': 'tebek',
        'password': 'tebek06',
        'login_try_count': 0,
        'is_active': False
    }
]

def get_user_by_username(username):
    for user in users:
        if user['username'] == username:
            return user
    return None

def login():
    username = input('Enter your username: ')
    user = get_user_by_username(username)
    
    if user is None:
        return 'User does not exist'
    
    if user['login_try_count'] >= 3:
        return 'Your account is blocked due to too many failed login attempts.'
    
    password = input('Enter your password: ')
    
    if user['password'] != password:
        user['login_try_count'] += 1
        return f'Wrong password. Attempt {user["login_try_count"]} of 3.'
    
    user['is_active'] = True
    user['login_try_count'] = 0  
    return 'Logged in successfully'

while True:
    print(login())
