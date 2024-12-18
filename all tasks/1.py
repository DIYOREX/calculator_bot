son = []
while True:
    num = int(input("Sonni kiriting: "))
    son.append(num)
    
    if len(son) >= 5:
        break


mutlaq_sonlar = list(map(lambda x: abs(x), son))
print("kiritilgan sonlarning musbat qiymatlari :", mutlaq_sonlar)


