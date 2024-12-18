def information_of_people():
    while True:
        
        while True:
            name = input("Enter your name: ")
            if name.isdigit(): 
                print('Please enter only letters for your name.')
            else:
                break
        
        
        while True:
            age = input("Enter your age: ")
            if not age.isdigit(): 
                print("Please enter only numbers for your age.")
            else:
                age = int(age) 
                break

        birth_of_year = 2024 - age 
        print(f"{name}, you were born in {birth_of_year}.") 
        break 

information_of_people()
