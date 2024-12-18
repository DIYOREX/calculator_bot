taom = ['osh', 'shurva', 'chuchvara', 'manti', 'somsa']
nonushta = taom.copy()

nonushta.pop(0)  
nonushta.pop(2) 
nonushta.extend(['non', 'choy'])

print(f"{taom}, va {nonushta}")

numbers = [0, 1, 2, 3, 4]

zipped = zip(numbers, nonushta)
print(list(zipped))  
