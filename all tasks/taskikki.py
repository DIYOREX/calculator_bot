juft_sonlar = [] 

for son in range(120, 1200): 
    if son % 2 == 0:
        juft_sonlar.append(son) 
print(juft_sonlar)  
          
summa = sum(juft_sonlar) 
print(f'summa = ', {summa})
   
SubtractionMaxMin = max(juft_sonlar) - min(juft_sonlar)
print(f'summaMinMax = ', {SubtractionMaxMin})

length = len(juft_sonlar)
print(f' length = ', {length})

first_7 = juft_sonlar[:7]
mid_index = len(juft_sonlar) // 2
middle_6 = juft_sonlar[mid_index - 3:mid_index + 3]
last_7 = juft_sonlar[-7:]
last_20 = juft_sonlar[-20:]
print(f'fisrt=, {first_7}, middle=, {middle_6}, last=, {last_7}')
