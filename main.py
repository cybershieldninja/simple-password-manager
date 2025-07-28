import sys
import getpass
from password_manager import save_password, retrieve_password, generate_random_password

def display_menu():
    print("\nWelcome to the Password Manager!")
    print("1. Create new password entry")
    print("2. Retrieve stored password")
    print("3. Generate a random password")
    print("4. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            service = input("Enter the service name (e.g., GitHub, Gmail): ")
            username = input("Enter the username: ")
            password = getpass.getpass("Enter the password: ")
            save_password(service, username, password)
            print(f"Password for {service} saved successfully!")
        elif choice == "2":
            service = input("Enter the service name to retrieve password: ")
            username, password = retrieve_password(service)
            if username and password:
                print(f"Username: {username}")
                print(f"Password: {password}")
                pyperclip.copy(password)  # Copy password to clipboard
                print(f"Password copied to clipboard!")
            else:
                print(f"No entry found for {service}.")
        elif choice == "3":
            length = int(input("Enter the desired length of the password: "))
            random_password = generate_random_password(length)
            print(f"Generated password: {random_password}")
        elif choice == "4":
            print("Exiting Password Manager. Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
