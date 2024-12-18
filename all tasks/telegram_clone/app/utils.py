import time
import bcrypt


def generate_id():
    return time.time_ns()


def hash_password(raw_password: str):
    raw_password = raw_password.encode('utf-8')
    return bcrypt.hashpw(raw_password, salt=bcrypt.gensalt())


# bcrypt
#
# password = 'admin123'.encode('utf-8')
# salt = bcrypt.gensalt()
# hashed_password = bcrypt.hashpw(password, salt)
#
# new_password = input('...').encode('utf-8')
# result = bcrypt.checkpw(new_password, hashed_password)
# if result:
#     print('Password is correct!')
#
# else:
#     print('----------')
