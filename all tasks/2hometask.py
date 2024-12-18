def kvadrat_and_kubi():
    while True:
        number = input('enter a number: ')
        if not number.isdigit():
            print("Please enter only a valid number")
        else:
            number = int(number)    
            break
    kvadrati = number**2
    kubi = number**3
    print(f"The square of {number} is {kvadrati}")
    print(f"The cube of {number} is {kubi}")

kvadrat_and_kubi()
