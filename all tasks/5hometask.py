def x_number():
    while True:  # Start an infinite loop
        x = input("Enter the first number: ")
        y = input("Enter the second number: ")

        if not x.isdigit() or not y.isdigit():
            print("Please enter valid numbers!")
            continue 

        num1 = int(x)
        num2 = int(y)
        multiply = num1 ** num2
        print(multiply)
        break  

x_number()
