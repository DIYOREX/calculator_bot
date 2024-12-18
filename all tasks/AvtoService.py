class AvtoService:
    cars = []  

    def __init__(self) -> None:
        pass

    def add_car(self, car):
        self.cars.append(car)

    def show_cars(self):
        for car in self.cars:
            print(car)

class Avto:
    def __init__(self, model, year, color) -> None:
        self.model = model
        self.year = year
        self.color = color

    def __str__(self) -> str:
        return f"Model: {self.model}, Year: {self.year}, Color: {self.color}"

service = AvtoService()

car2 = Avto('BMW', 2021, 'Black')

service.add_car(car2)

service.show_cars()
