class Avto:
    def __init__(self, nom, narx, yil):
        self.nom = nom
        self.narx = narx
        self.yil = yil

    def __str__(self):
        return f"{self.nom} ({self.yil}) - {self.narx}$"

    def __repr__(self):
        return f"Avto('{self.nom}', {self.narx}, {self.yil})"

    def __add__(self, boshqa):
        return self.narx + boshqa.narx

    def __getitem__(self, xususiyat):
        attributes = {'nom': self.nom, 'narx': self.narx, 'yil': self.yil}
        return attributes.get(xususiyat, "bunday xususiyat mavjud emas")

    def __del__(self):
        print(f"{self.nom} obyekti uchirildi")


avto1 = Avto("toyota", 25000, 2020)
avto2 = Avto("Honda", 22000, 2019)

print(avto1)               
print(repr(avto2))        

print(avto1 + avto2)      

print(avto1["nom"])        
print(avto2["narx"])       
print(avto1["yil"])         
print(avto2["rangi"])       

del avto1                



