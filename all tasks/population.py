from colorama import Fore, init
init(autoreset=True)
from typing import List, Optional


class Citizen:
    def __init__(self, name: str, surname: str, age: int, address: str):
        self.name = name
        self.surname = surname
        self.age = age
        self.address = address

    def __repr__(self):
        return f'{self.name} {self.surname}, {self.age} years old, Address: {self.address}'

    def update_info(self, name: Optional[str] = None, surname: Optional[str] = None, age: Optional[int] = None, address: Optional[str] = None):
        if name:
            self.name = name
        if surname:
            self.surname = surname
        if age:
            self.age = age
        if address:
            self.address = address
        print(Fore.GREEN + 'Citizen information successfully updated')


class Population:
    def __init__(self):
        self.citizens: List[Citizen] = []

    def add_citizen(self, citizen: Citizen):
        self.citizens.append(citizen)
        print(Fore.GREEN+f'Citizen {citizen.name} successfully added')

    def show_all_citizens(self):
        if not self.citizens:
            print(Fore.RED+"No citizens in the population")
        for index, citizen in enumerate(self.citizens, 1):
            print(f'{index}. {citizen}')

    def delete_citizen(self):
        self.show_all_citizens()
        index = int(input(Fore.BLUE+'Enter the index of the citizen to delete: '))
        if 0 < index <= len(self.citizens):
            removed = self.citizens.pop(index - 1)
            print(Fore.RED+f'Citizen {removed.name} successfully deleted')
        else:
            print(Fore.CYAN+'Invalid index')

    def update_citizen(self):
        self.show_all_citizens()
        index = int(input(Fore.LIGHTMAGENTA_EX+'Enter the index of the citizen to update: '))
        if 0 < index <= len(self.citizens):
            citizen = self.citizens[index - 1]
            name = input('Enter new name: ')
            surname = input('Enter new surname: ')
            age = input('Enter new age: ')
            citizen.update_info(name=name, surname=surname, age=int(age) if age else None)
        else:
            print(Fore.RED+'Invalid index')

    def get_citizen(self):
        self.show_all_citizens()
        index = int(input('Enter the index of the citizen to view: '))
        if 0 < index <= len(self.citizens):
            print(self.citizens[index - 1])
        else:
            print('Invalid index')


def main():
    population = Population()

    while True:
        print(Fore.LIGHTMAGENTA_EX+"\n1. Add Citizen")
        print(Fore.LIGHTBLUE_EX+"2. Show All Citizens")
        print(Fore.LIGHTMAGENTA_EX+"3. Get Citizen Info")
        print(Fore.LIGHTYELLOW_EX+"4. Update Citizen")
        print(Fore.LIGHTCYAN_EX+"5. Delete Citizen")
        print(Fore.RED+"6. Quit")

        choice = input(Fore.BLUE +"Choose an option: ")

        if choice == '1':
            name = input(Fore.BLUE+'Enter name: ')
            surname = input(Fore.BLUE+'Enter surname: ')
            age = int(input(Fore.BLUE+'Enter age: '))
          #   address = input('Enter address: ')
            citizen = Citizen(name, surname, age)
            population.add_citizen(citizen)

        elif choice == '2':
            population.show_all_citizens()

        elif choice == '3':
            population.get_citizen()

        elif choice == '4':
            population.update_citizen()

        elif choice == '5':
            population.delete_citizen()

        elif choice == '6':
            print("Exiting the program.")
            break

        else:
            print(Fore.RED+"Invalid option. Try again.")


if __name__ == '__main__':
    main()
