while True:
    password = input("Parolni kiriting: ")
    if len(password) < 8:
        print("Parol kamida 8 ta belgidan iborat bo'lishi kerak.")
    elif not any(c.isupper() for c in password):
        print("Parolda kamida 1 ta katta harf bo'lishi kerak.")
    elif not any(c.islower() for c in password):
        print("Parolda kamida 1 ta kichik harf bo'lishi kerak.")

    elif not any(c.isdigit() for c in password):
        print("Parolda kamida 1 ta raqam bo'lishi kerak.")
    elif not any(c in "!@#$%^&*()_+<>?/" for c in password):
        print("Parolda kamida 1 ta maxsus belgi bo'lishi kerak.")
    else:
        print("Parol to'g'ri.")
        break

