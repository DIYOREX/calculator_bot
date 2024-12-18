# Bismillah

from colorama import Fore, init
init(autoreset=True)
from typing import Optional
from uuid import uuid4, UUID
import json

class FileHandling:
    def __init__(self, filename: str, mode: str):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.open_file()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close_file()

    def open_file(self):
        try:
            self.file = open(self.filename, self.mode)
            print(Fore.GREEN+'File successfully opened')
        except FileNotFoundError:
            print(f"File '{self.filename}' not found.")
        except IOError as e:
            print(f"An IOError occurred: {e}")

    def read_file(self):
        if self.file and 'r' in self.mode:
            try:
                content = self.file.read()
                print(content)
            except IOError as e:
                print(f"An IOError occurred while reading the file: {e}")
        else:
            print('File not open for reading or no such file.')

    def write_file(self, text: str):
        if self.file and ('w' in self.mode or 'a' in self.mode):
            try:
                self.file.write(text)
                print('Text successfully written to file.')
            except IOError as e:
                print(f"An IOError occurred while writing to the file: {e}")
        else:
            print('File not open for writing.')

    def close_file(self):
        if self.file and not self.file.closed:
            self.file.close()
            print('File successfully closed.')

with FileHandling(Fore.LIGHTBLUE_EX+'saved_data.txt', mode='a+') as file:
    file.read_file()                
    file.write_file(Fore.YELLOW+'Hello, My name is Diyorbek,')  
