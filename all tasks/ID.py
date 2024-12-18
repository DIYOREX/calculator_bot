info_humans = {}

def id_info():
    while input('Do you wanna add someone else? (y/n) ').startswith('y'):
        phone_number = input("Enter your phone number: ")

        name = input('Enter your full name: ')
        if name.isalpha():
            pass
        else:
            print("Enter your name using only letters.")
            continue 

        age = input('Enter your age: ')
        if age.isdigit():
            pass
        else:
            print("Enter your age using only numbers.")
            continue 

        address = input('Enter your address: ')

        serial = input('Enter your passport serial (AB, AC, or AD): ')
        if serial.startswith(('AB', 'AC', 'AD')):
            pass
        else:
            print("Enter a valid passport serial (AB, AC, or AD).")
            continue 

        number = input('Enter your passport number: ')
        if number.isdigit():
            pass
        else:
            print('Enter your passport number using only numbers.')
            continue 

        info_humans[phone_number] = {
            'name': name,
            'age': age,
            'address': address,
            'serial': serial,
            'number': number
        }

    print("Collected Information about people:", info_humans)

id_info()
