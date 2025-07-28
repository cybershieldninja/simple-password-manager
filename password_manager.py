from cryptography.fernet import Fernet
import json
import os
import base64
import pyperclip
# Generate a random password
import random
import string

# Generate a key for encryption (Only run once to save the key securely)
def generate_key():
    """
    Generates a 256-bit key for AES encryption and saves it to a file 'secret.key'.
    This should only be run once to create the key.
    """
    # Generate a 256-bit random key
    key = base64.urlsafe_b64encode(os.urandom(32))  # 32 bytes = 256 bits
    
    # Save the key to 'secret.key'
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    
    print("Key generated and saved to 'secret.key'.")

# Store and retrieve the key securely (For simplicity, we'll store it in a file)
def load_key():
    """
    Loads the encryption key from the 'secret.key' file. If the file does not exist,
    it generates a new key and saves it to 'secret.key'.
    """
    if not os.path.exists("secret.key"):
        print("Key not found. Generating a new key...")
        generate_key()  # Generate and save a new key
    
    # Load and return the encryption key from 'secret.key'    
    return open("secret.key", "rb").read()

# Encrypt the password
def encrypt_password(password, key):
    f = Fernet(key)
    encrypted_password = f.encrypt(password.encode())
    return encrypted_password

# Decrypt the password
def decrypt_password(encrypted_password, key):
    f = Fernet(key)
    decrypted_password = f.decrypt(encrypted_password).decode()
    return decrypted_password

# Save password to file
def save_password(service, username, password):
    key = load_key()
    encrypted_password = encrypt_password(password, key)

    # Store the encrypted password in a dictionary
    if not os.path.exists("passwords.json"):
        with open("passwords.json", "w") as f:
            json.dump({}, f)

    with open("passwords.json", "r") as f:
        data = json.load(f)

    data[service] = {"username": username, "password": encrypted_password.decode()}

    with open("passwords.json", "w") as f:
        json.dump(data, f, indent=4)

# Retrieve a stored password
def retrieve_password(service):
    key = load_key()
    with open("passwords.json", "r") as f:
        data = json.load(f)

    if service in data:
        username = data[service]["username"]
        encrypted_password = data[service]["password"].encode()
        decrypted_password = decrypt_password(encrypted_password, key)
        return username, decrypted_password
    else:
        return None, None

def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    random_password = ''.join(random.choice(characters) for i in range(length))
    return random_password
