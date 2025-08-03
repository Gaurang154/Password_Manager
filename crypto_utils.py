import os
from cryptography.fernet import Fernet

def load_key():
    if not os.path.exists ("key.key"):
        key = Fernet.generate_key()
        with open("key.key" , "wb") as key_file:
            key_file.write(key)
    else :
        with open("key.key" , "rb") as key_file:
            key = key_file.read()       
    return Fernet (key)        