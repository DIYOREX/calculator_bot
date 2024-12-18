def max_number():
    while True:
        num1 = input("Enter the first number: ")
        num2 = input("Enter the second number: ")

        if not num1.isdigit() or not num2.isdigit():
            print("Please enter valid numbers!")
            continue

       
        num1 = int(num1)
        num2 = int(num2)

        if num1 > num2:
            print(f"{num1} is greater than {num2}")
        elif num2 > num1:
            print(f"{num2} is greater than {num1}")
        else:
            print("The numbers are equal")
        break

max_number()
