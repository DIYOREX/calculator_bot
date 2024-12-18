class Car:
    def __init__(self, color):
        self._color = color

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        if isinstance(value, str):
            self._color = value
        else:
            raise ValueError("color names  must be a string in this code")

    @color.deleter
    def color(self):
        print("all color is deleted")
        del self._color

car = Car("magenta")
print(car.color)

car.color = "yellow"
print(car.color)

del car.color
