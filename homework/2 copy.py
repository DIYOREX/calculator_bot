from decimal import Decimal

usd_to_uzs_rate = Decimal('12250.50')

usd_amount = Decimal('200.00')  

uzs_amount = usd_amount * usd_to_uzs_rate
# natja
print(f"{usd_amount} USD = {uzs_amount} UZS")
