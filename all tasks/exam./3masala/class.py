
class UserInformation:
    def __init__(self, name, age, email):
        self.name = name             
        self._age = age              
        self.__email = email         

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def _get_age(self): 
        return self._age

    def _set_age(self, age):
        self._age = age

    def __get_email(self):
        return self.__email

    def __set_email(self, email):
        self.__email = email

    def display_info(self):
        print(f"Name: {self.name}, Age: {self._age}, Email: {self.__email}")

user = UserInformation("Diyorbek", 17, "diyorbek@example.com")
user.display_info()

print(user.get_name())

print(user._get_age()) 
