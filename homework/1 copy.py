from decimal import Decimal

price = Decimal('150.75')
tax_rate = Decimal('0.15')  

tax_amount = price * tax_rate
total_price = price + tax_amount

print(f"mahsulot narxi: {price}")

print(f"qqs: {tax_amount}")


print(f"jami narx: {total_price}")
