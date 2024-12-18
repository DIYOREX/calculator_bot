class Passport:
    def __init__(self, passport_number, name, last_name):
        self._passport_number = passport_number
        self._name = name
        self._last_name = last_name

    @property
    def passport_number(self):
        return self._passport_number

    @property
    def name(self):
        return self._name

    @property
    def last_name(self):
        return self._last_name




passport = Passport('1234567890', 'diyorbek', 'yaxyayev')
print(passport.passport_number)  
print(passport.name)            
print(passport.last_name)      
