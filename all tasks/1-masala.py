#kiritilgan sonlarni juft yoki toq sonlarga ajratish:
son1 = int(input("birinchi sonni kiriting: "))
son2 = int(input("Ikkinchi sonni kiriting: "))
son3 = int(input("uchun sonni kiriting: "))
son4 = int(input("to'rtinchi sonni kiriting: "))
juft_sonlar = []
toq_sonlar = []

if son1%2==0:
          juft_sonlar.append(son1)
if son1%2==1:
          toq_sonlar.append(son1)
if son2%2==0:
          juft_sonlar.append(son2)
if son2%2==1:
          toq_sonlar.append(son2)
if son3%2==0:
          juft_sonlar.append(son3)
if son3%2==1:
          toq_sonlar.append(son3)
if son4%2==0:
          juft_sonlar.append(son4)
if son4%2==1:
          toq_sonlar.append(son4)

print("juft sonlar:",juft_sonlar)
print("toq sonlar:",toq_sonlar)

