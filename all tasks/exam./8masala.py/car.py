from abc import ABC, abstractmethod

class Car(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class tesla(Car):
    def start(self):
        print("tesla is running")

    def stop(self):
        print("tesla is stoped.")

class nexia2(Car):
    def start(self):
        print("nexia is run")

    def stop(self):
        print("nexia is stop")

electric_car = tesla()
electric_car.start()
electric_car.stop()

petrol_car = nexia2()
petrol_car.start()
petrol_car.stop()
