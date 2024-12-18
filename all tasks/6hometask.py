def x_number():
    while True: 
        x = input("Enter the first number: ")
        y = 2

        if not x.isdigit():
            print("Please enter valid numbers!")
            continue 

        num1 = int(x)
        
        multiply = num1 ** y
        print(multiply)
        break  

x_number()
