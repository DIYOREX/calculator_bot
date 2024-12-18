from decimal import Decimal

class DecimalValue:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
              
        if not isinstance(value, Decimal):
            raise TypeError(f"'{self.name}' faqat decimal turida bo'lishi kerak!")
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        raise AttributeError(f"'{self.name}' qiymatini o'chirish taqiqlangan!")

class Product:
    price = DecimalValue("price")
    
    tax_rate = DecimalValue("tax_rate")

    def __init__(self, price, tax_rate):
        self.price = price
        self.tax_rate = tax_rate
        
        
        
        
        
        
        
        
        
        

    def total_price(self):
        return self.price + (self.price * self.tax_rate)

product = Product(Decimal('150.75'), Decimal('0.15'))
print(f"Jami narx: {product.total_price()}")

try:
    product.price = 150.75 
except TypeError as e:
    print(e)
