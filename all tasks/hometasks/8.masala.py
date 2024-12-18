my_tuple = (10, 20, 30)
new_price = 25
temp_list = list(my_tuple)
temp_list[1] = new_price  
new_tuple = tuple(temp_list)
print(new_tuple)
