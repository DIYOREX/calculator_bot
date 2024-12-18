from functools import reduce
from colorama import Fore, init

numbers = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, numbers)
print(Fore.RED,total)  
