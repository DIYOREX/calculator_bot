from views import (
    create_user,
    add_contact,
    contact_list,
    create_chat,
    add_message
)


def menu():
    print('Create User  => 1')
    print("Add Contact  => 2")
    print("Contact List => 3")
    print("Create Chat  => 4")
    print("Add Message  => 5")
    print('Exit         => q')
    return input("?:")


def run():
    while True:
        choice = menu()
        if choice == '1':
            user_id = input("User ID : ")
            password = input("password : ")
            phone_number = input("phone number : ")
            create_user(user_id, password, phone_number)
        elif choice == '2':
            user_id = input("User ID : ")
            contact_id = input("Contact ID : ")
            add_contact(user_id, contact_id)
        elif choice == '3':
            user_id = input("User ID : ")
            contact_list(user_id)
        elif choice == '4':
            user1 = input("User ID1 : ")
            user2 = input("User ID2 : ")
            create_chat(user1, user2)
        elif choice == '5':
            chat_id = input("Chat ID : ")
            add_message(chat_id)

        elif choice == 'q':
            print('Come back again')
            break


if __name__ == '__main__':
    run()
