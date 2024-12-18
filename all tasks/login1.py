from colorama import Fore, init
init(autoreset=True)

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
    print(Fore.MAGENTA + 'Enter your username: ', end='')
    username = input()
    user = get_user_by_username(username)
    
    if user is None:
        return Fore.RED + 'User does not exist'
    
    if user['login_try_count'] >= 3:
        return Fore.RED + 'Your account is blocked due to too many failed login attempts.'
    
    password = input('Enter your password: ')
    
    if user['password'] != password:
        user['login_try_count'] += 1
        return Fore.RED + f'wrong password. attempt {user["login_try_count"]} of 3.'
    
    user['is_active'] = True
    user['login_try_count'] = 0  
    return Fore.GREEN + 'Logged in successfully'

while True:
    print(login())
