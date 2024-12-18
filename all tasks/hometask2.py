mahalla = []
while True:
   while True:
        name = input("Enter your name: ")
        if name.isalpha():
            mahalla.append(name)
            break
        else:
            print("Enter only letters for the name.")
   while True:
        age = input("Enter your age: ")
        if age.isdigit():
            mahalla.append(age)
            break
        else:
            print("Enter only numbers for the age.")
   while True:
        email = input("Enter your email (end with @gmail.com, @gmail.ru, or @yahoo.com): ")
        if email.endswith("@gmail.com") or email.endswith("@gmail.ru") or email.endswith("@yahoo.com"):
            mahalla.append(email)
            break
        else:
            print("Enter a valid email that ends with @gmail.com, @gmail.ru, or @yahoo.com.")
   while True:
        address = input("Enter your address: ")
        if any(char.isupper() for char in address):
            mahalla.append(address)
            break
        else:
            print("The address should contain at least one uppercase letter.")
   print(mahalla)
   more = input("Would you like to go again? Y/N or y/n ").upper()
   if not more.startswith("Y" or "y"): 
        break
print("Final list of users:")
for user in mahalla:
    print(user)
