meals = ['plov', 'manti', 'shurva', 'shirguruch', 'chuchvara']
breakfast = meals[:]

meals.pop(-1)
meals.pop(1)
extra_ones = meals.extend(['sugar', 'sweet'])

print(f'{breakfast} and {meals}')

breakfast = tuple(breakfast)
breakfast[0] = 'qaymoq va non' # tuple bo'lganligi uchun xatolik beradi.

