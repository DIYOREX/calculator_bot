class Kurs:
    def __init__(self, nomi, oquvchilar_soni):
        self.nomi = nomi
        self.__oquvchilar_soni = oquvchilar_soni  

    def oquvchilar_soni_olish(self):
        return self.__oquvchilar_soni

    def oquvchi_qoshish(self, soni):
        self.__oquvchilar_soni += soni
        return f"jami o'quvchilar soni: {self.__oquvchilar_soni}"

kurs = Kurs("yython dasturlash", 25)
print(kurs.oquvchilar_soni_olish())
print(kurs.oquvchi_qoshish(5))
