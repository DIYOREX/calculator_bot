def find_max(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
son1 = 3
son2 = 3
son3 = 3
max_son = find_max(son1, son2, son3)
print("berilgan  sonlarning eng kattasi: ", max_son)
