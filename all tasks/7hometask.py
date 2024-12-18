def number():
    num = int(input("Sonni kiriting: ")) 

    topish = False
    for i in range(2, 11):
        if num % i == 0:
            print(f"{num} soni {i} ga qoldiqsiz bo'linadi.")
            topish = True
    
    if not topish:
        print(f"{num} soni 2 dan 10 gacha bo'lgan hech qanday songa qoldiqsiz bo'linmaydi.")

number()






