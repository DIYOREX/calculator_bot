from enum import Enum
from typing import Optional
from datetime import datetime


class Language(Enum):
    RUSSIAN = 'ru'
    ENGLISH = 'en'
    UZBEK = 'uz'
    FRENCH = 'fr'


class User:
    def __init__(self,
                 full_name: str,
                 password: str,
                 phone_number,
                 user_id: Optional[str] = None,
                 language: Optional[Language] = None,
                 created_at: Optional[datetime] = None
                 ):
        self.full_name = full_name
        self.password = password
        self.phone_number = phone_number
        self.user_id = user_id
        self.language = language or Language.ENGLISH.value
        self.created_at = created_at or str(datetime.now())
        self.contacts = []


class Message:
    def __init__(self, sender_id, receiver_id, body, created_at):
        self.sender_id = sender_id
        self.receiver_id = receiver_id
        self.body = body
        self.created_at = str(datetime.now())


class Chat:
    def __init__(self, chat_id, users):
        self.chat_id = chat_id
        self.users = users
        self.messages = []


class Channel:
    pass
