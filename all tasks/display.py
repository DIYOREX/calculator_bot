from colorama import Fore, init
init(autoreset=True)
def print_succses(message):
          print(Fore.GREEN+ message)
          
          
          
def print_error(message):
          print(Fore.RED+message)
          