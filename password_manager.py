import os
import json
from crypto_utils import load_key

fernet = load_key()

def save_password():
    if os.path.exists("vault.json"):
        with open("vault.json", "r") as vault_file:
            vault_data = json.load(vault_file)
    else:
        vault_data = {}

    website = input("Enter website name\n")
    username = input("Enter username\n")
    password = input("Enter your password\n")

    encrypted_password = fernet.encrypt(password.encode()).decode()

    vault_data[website] = {
        "username": username,
        "password": encrypted_password
    }

    with open("vault.json", "w") as vault_file:
        json.dump(vault_data, vault_file, indent=4)

    print("Password saved successfully 🔐")


def view_password():
    if os.path.exists("vault.json"):
        with open("vault.json", "r") as vault_file:
            vault_data = json.load(vault_file)

        for website, details in vault_data.items():
            username = details["username"]
            encrypted_password = details["password"]
            decrypted_password = fernet.decrypt(encrypted_password.encode()).decode()

            print(f"Website: {website}\nUsername: {username}\nPassword: {decrypted_password}\n")
    else:
        print("No password file found 🔒")