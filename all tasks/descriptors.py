class PermissionDescriptor:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name, False)

    def __set__(self, instance, value):
        if not isinstance(value, bool):
            raise ValueError(f"{self.name} must be a boolean value.")
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        raise AttributeError(f"Cannot delete {self.name} attribute.")

class User:
    can_edit = PermissionDescriptor('can_edit')
    can_delete = PermissionDescriptor('can_delete')

    def __init__(self, username):
        self.username = username

try:
    user = User("diyorbek")
    print(user.can_edit)  
    user.can_edit = True  
    print(user.can_edit)
    user.can_edit = "Test"  
except ValueError as e:
    print(e)

try:
    del user.can_edit  
except AttributeError as e:
    print(e)
