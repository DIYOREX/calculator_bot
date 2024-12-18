class Display:
    def show(self):
        print("ekran kurinishi.")

class Camera:
    def take_photo(self):
        print("rasmga olishi.")

class Radio:
    def play_radio(self):
        print("ovozi.")

class Phone(Display, Camera, Radio):
    def __init__(self, model, room, price, color):
        self.model = model
        self.room = room
        self.price = price
        self.color = color
    
    def phone_details(self):
        print(f"Phone Model: {self.model}, Room: {self.room}, Price: {self.price}, Color: {self.color}")
        
my_phone = Phone("iPhone ", "mini", 1200, "blue")
my_phone.phone_details()
my_phone.show()
my_phone.take_photo()
my_phone.play_radio()
