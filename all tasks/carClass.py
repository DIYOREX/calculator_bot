from colorama import Fore, init
init(autoreset=True)
class Avtomobil:
    def __init__(self, nomi, rangi, narxi):
        self.nomi = nomi
        self.rangi = rangi
        self._narxi = narxi 

    @property
    def narx(self):
        return self._narxi

    @narx.setter
    def narx(self, qiymat):
        if qiymat > 0:
            self._narxi = qiymat
        else:
            raise ValueError("narx musbat bo'lishi kerak!")

    @narx.deleter
    def narx(self):
        del self._narxi

avto = Avtomobil("nexia", "oq", 10000)

print("avtomobil narxi:", avto.narx)

avto.narx = 12000
print("yangilangan narx:", avto.narx)

del avto.narx
