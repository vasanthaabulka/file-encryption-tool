from cryptography.fernet import Fernet # type: ignore

import os

def generate_key():
    """Generates a new encryption key and saves it to secret.key file"""
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("[+] New encryption key generated and saved to secret.key.")

def load_key():
    """Loads the encryption key from secret.key file"""
    if not os.path.exists("secret.key"):
        print("[-] Key file not found. Please generate a key first.")
        return None
    return open("secret.key", "rb").read()

def encrypt_file(filename, key):
    """Encrypts the contents of the file using the key"""
    fernet = Fernet(key)
    try:
        with open(filename, "rb") as file:
            data = file.read()
        encrypted = fernet.encrypt(data)
        with open(filename, "wb") as file:
            file.write(encrypted)
        print(f"[+] File '{filename}' encrypted successfully.")
    except FileNotFoundError:
        print(f"[-] File '{filename}' not found.")

def decrypt_file(filename, key):
    """Decrypts the contents of the file using the key"""
    fernet = Fernet(key)
    try:
        with open(filename, "rb") as file:
            data = file.read()
        decrypted = fernet.decrypt(data)
        with open(filename, "wb") as file:
            file.write(decrypted)
        print(f"[+] File '{filename}' decrypted successfully.")
    except Exception as e:
        print("[-] Error decrypting file:", str(e))

if __name__ == "__main__":
    print("\n====== File Encryption/Decryption Tool ======\n")
    print("1. Generate Key")
    print("2. Encrypt File")
    print("3. Decrypt File")
    choice = input("\nEnter your choice (1/2/3): ")

    if choice == "1":
        generate_key()

    elif choice == "2":
        key = load_key()
        if key:
            filename = input("Enter filename to encrypt (e.g., sample.txt): ")
            encrypt_file(filename, key)

    elif choice == "3":
        key = load_key()
        if key:
            filename = input("Enter filename to decrypt (e.g., sample.txt): ")
            decrypt_file(filename, key)

    else:
        print("[-] Invalid choice. Exiting.")
