import sys
from password_manager import save_password, view_password
print("Welcome to the Password Manager 🔐\n")
while True:
    try:
        o = int(input("Please choose an option:\n 1: Save a new password \n 2:View saved passwords \n 3:Exit \n"))
        if (o==1):
            save_password()
        elif(o==2):
            view_password()
        elif(o==3):
            print("Goodbye! 👋")
            sys.exit()
        else:
            print("Invalid input. Please try again.")
    except ValueError:
        print("Please enter a valid number (1, 2, or 3).\n")        