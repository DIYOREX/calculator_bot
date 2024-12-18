from functools import reduce

raqamlar = [1, 2, 3, 4, 5]

yigindi = reduce(lambda x, y: x + y, raqamlar)

print(yigindi)
