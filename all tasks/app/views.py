import utils
from models import Chat, Message
from models import User


def create_user(user_id: str, password: str, phone_number: str):
    users_data: dict = User.load_users()
    if user_id in users_data:
        print("User already exists")
    else:
        user = User(user_id=user_id, password=password, phone_number=phone_number)
        user.password = str(utils.hash_password(password))
        users_data[user_id] = user.__dict__
        User.save_users(users_data)
        print("User successfully created!")


def add_contact(user_id, contact_id):
    users_data: dict = User.load_users()
    if (user_id and contact_id) not in users_data:
        print("User does not exists")
    elif user_id == contact_id:
        print("IDs must not be equal")
    elif contact_id in users_data[user_id]["contacts"]:
        print("This contact id already exists")
    else:
        users_data[user_id]["contacts"].append(contact_id)

        User.save_users(users_data)

        print("Contact successfully added!")


def contact_list(user_id):
    users_data = User.load_users()
    if user_id not in users_data:
        print("User does not exists")
    else:
        print(f"{user_id}'s contacts : {users_data[user_id]['contacts']}")


def create_chat(user1, user2):
    chat_id = f"{user1}_{user2}"
    chats_data = Chat.load_chats()
    if (user1 and user2) not in User.load_users():
        print("You cannot create chat.Because there is not enough user")
        return

    if chat_id in chats_data:
        print("Chat is already exists")
        return

    chat = Chat(chat_id, users=[user1, user2])
    chats_data[chat_id] = chat.__dict__
    Chat.save_chats(chats_data)
    print("Chat successfully created")


def add_message(chat_id):
    chats_data = Chat.load_chats()
    if chat_id not in Chat.load_chats():
        print("Chat does not exist")
        return

    sender = input("Sender ID : ")
    receiver = input("Receiver ID : ")
    body = input("Body : ")

    message = Message(sender, receiver, body)
    chats_data[chat_id]["messages"].append(message.__dict__)
    Chat.save_chats(chats_data)
    print("Message successfully sent")


def read_message(chat_id):
    chats_data = Chat.load_chats()
    if chat_id not in chats_data:
        print("Chat does not exist")
        return
    
    messages = chats_data[chat_id]["messages"]
    if not messages:
        print("No messages in this chat")
    else:
        print(f"Messages in chat {chat_id}:")
        for message in messages:
            print(f"From: {message['sender']} To: {message['receiver']}")
            print(f"Message: {message['body']}")
            print("------")
