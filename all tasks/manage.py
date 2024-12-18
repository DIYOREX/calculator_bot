from colorama import Fore, init
init(autoreset=True)
def menu():
          print(Fore.LIGHTBLUE_EX+'login => 1')
          print(Fore.LIGHTBLUE_EX+'exit => 0')
          return input('?:')



from auth import login
def run():
          while True:
                    choice = menu()
                    if choice in ['0', 'no', 'n']:
                              break
                    elif choice == '1':
                              login()
                    else:
                              print("invalid choice")
                              