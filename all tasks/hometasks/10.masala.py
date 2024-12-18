my_list = [(1, 2), (3, 4), (5, 6)]
new_list = [element for tpl in my_list for element in tpl]
print(new_list)
