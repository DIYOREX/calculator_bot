class Oyinchi:
    def __init__(self, ism, ochko):
        self.ism = ism
        self.__ochko = ochko 

    def ochko_olish(self):
        return self.__ochko

    def __ochko_sirini_yashirish(self):
        return f"{self.ism}ning ochkosi sir!"

    def ochko_malumoti(self):
        return self.__ochko_sirini_yashirish()

oyinchi = Oyinchi("Diyorbek", 85)
print(oyinchi.ochko_olish())
print(oyinchi.ochko_malumoti())
