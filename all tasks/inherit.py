from colorama import Fore, init
init(autoreset=True)


class BMW:
    def X5(self):
        return Fore.GREEN+"Hello from BMW family!"

class X7(BMW):
    def greet_parent(self):
        return Fore.BLUE+"Hello from BMW X7 model!"

class i5(BMW):
    def greet_aunt(self):
        return Fore.LIGHTMAGENTA_EX+"Hello from BMW i5 model!"

class i7(X7, i5):
    def greet_child(self):
        return Fore.LIGHTRED_EX+"Hello from BMW i7 model!"

car = i7()

print(car.X5())            
print(car.greet_parent()) 
print(car.greet_aunt())   
print(car.greet_child()) 
