# Password Manager

## Description
The **Password Manager** is a simple and secure application designed to store and manage your passwords. This application uses **AES encryption** to protect your passwords and ensures that only you have access to them. It allows you to store multiple passwords for various services with ease while ensuring **strong encryption** for security.

### Features
- **Secure Password Storage**: Store your passwords encrypted using AES-256 encryption.
- **Password Generation**: Generate strong and random passwords for your accounts.
- **Master Password Protection**: The application uses a **master password** for access to the stored passwords.
- **Cross-platform Compatibility**: Works on **Windows**, **macOS**, and **Linux**.

---

## Prerequisites

Before running this application, make sure you have the following installed:

- **Python** (version 3.10 or higher)
- **pip** (Python package manager)

---

## Installation

### 1. Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/cybershieldninja/simple-password-manager.git
cd password-manager
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
    or 
pip install cryptography getpass pyperclip

```

### Usage
1. Run the Application

To start the application, run the following command:
```bash
python main.py
```

# Dependencies

The following libraries are required for this project:

    cryptography: For encryption and decryption of passwords.

    getpass: For securely capturing user input (especially passwords).

    pyperclip: For copying passwords to clipboard.

# License

This project is licensed under the MIT License - see the LICENSE file for details.

# Contributing

Feel free to fork the repository and submit pull requests. Contributions are welcome!    