from colorama  import Fore, init
init(autoreset=True)
try:
    with open("db.txt", "r") as file:
        content = file.read()
        print(Fore.GREEN+"db file dagi hamma ma'lumotlar:")
        print(content)
except FileNotFoundError:
    with open("db.txt", "w") as file:
        print(Fore.RED+"File not found, file is created.")
