def get_user_by_username(username):
          for user in  username:
                    if user[username] == username:
                              return user
          
          return None






def login():
          username = input("enter your username:")
          password = input("enter  your password: ")
          user = get_user_by_username(username)
          
          if user is None:
                    print('user is does not excist')
          elif user.get('login_try_count') >=3:
                    print('you are blocked')
          elif user['password'] != password:
                    user['login_try_count'] +=1
                    print('wrong password')
          else:
                    user['login_try_count'] = 0
                    user['is_active']=True
                    print('successfully logged in !')