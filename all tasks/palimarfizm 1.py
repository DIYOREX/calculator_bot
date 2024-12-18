class employee:
    def get_salary(self):
        pass

class developer(employee):
    def get_salary(self):
        return "salary of developer in uzbekiston: 1000 $ "

class Dizayner(employee):
    def get_salary(self):
        return "designher: 8 million so'm"

ishchilar = [developer(), Dizayner()]

for ishchi in ishchilar:
    print(ishchi.get_salary())
