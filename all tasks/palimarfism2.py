class Transport:
    def harakatlanish(self):
        pass

class Mashina(Transport):
    def harakatlanish(self):
        return "car is run"

class Samolyot(Transport):
    def harakatlanish(self):
        return "plane is fly"

transportlar = [Mashina(), Samolyot()]

for transport in transportlar:
    print(transport.harakatlanish())
