def juft_or_toq():
    while True:
        number = input('enter a number: ')
        if not number.isdigit():
            print("Please enter only a valid number")
        else:
            number = int(number)    
            break  
          
    if number % 2 == 0: 
        print('bu raqam juft son')
    else:
        print('bu son toq son')
    print(number)
    
juft_or_toq()
