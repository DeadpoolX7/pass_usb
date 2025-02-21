import os
import sqlite3
from cryptography.fernet import Fernet
import getpass
import hashlib
import base64

# Function to generate a key from the master password (SHA-256)
def generate_key(master_password):
    # Hash the master password using SHA-256
    hashed_password = hashlib.sha256(master_password.encode()).digest()
    # Encode the hashed password to base64 to create the Fernet key
    return base64.urlsafe_b64encode(hashed_password)

# Function to encrypt and decrypt passwords and emails
def encrypt_data(fernet, data):
    return fernet.encrypt(data.encode()).decode()

def decrypt_data(fernet, encrypted_data):
    return fernet.decrypt(encrypted_data.encode()).decode()

# Initialize SQLite Database
def init_db():
    conn = sqlite3.connect('passwords.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS credentials
                 (website TEXT, username TEXT, password TEXT, email TEXT)''')
    conn.commit()
    conn.close()

# Save new password/email to DB
def save_credentials(fernet, website, username, password, email):
    conn = sqlite3.connect('passwords.db')
    c = conn.cursor()
    encrypted_password = encrypt_data(fernet, password)
    encrypted_email = encrypt_data(fernet, email)
    c.execute("INSERT INTO credentials (website, username, password, email) VALUES (?, ?, ?, ?)",
              (website, username, encrypted_password, encrypted_email))
    conn.commit()
    conn.close()

# Retrieve credentials from DB
def get_credentials(fernet, website):
    conn = sqlite3.connect('passwords.db')
    c = conn.cursor()
    c.execute("SELECT username, password, email FROM credentials WHERE website=?", (website,))
    result = c.fetchone()
    conn.close()
    if result:
        username, encrypted_password, encrypted_email = result
        decrypted_password = decrypt_data(fernet, encrypted_password)
        decrypted_email = decrypt_data(fernet, encrypted_email)
        return username, decrypted_password, decrypted_email
    return None, None, None

# Update password/email for an entry
def update_credentials(fernet, website, new_password, new_email):
    conn = sqlite3.connect('passwords.db')
    c = conn.cursor()
    encrypted_password = encrypt_data(fernet, new_password)
    encrypted_email = encrypt_data(fernet, new_email)
    c.execute("UPDATE credentials SET password=?, email=? WHERE website=?",
              (encrypted_password, encrypted_email, website))
    conn.commit()
    conn.close()

# Delete an entry by website
def delete_credentials(website):
    conn = sqlite3.connect('passwords.db')
    c = conn.cursor()
    c.execute("DELETE FROM credentials WHERE website=?", (website,))
    conn.commit()
    conn.close()

# View all stored credentials
def view_all_credentials(fernet):
    conn = sqlite3.connect('passwords.db')
    c = conn.cursor()
    c.execute("SELECT website, username, password, email FROM credentials")
    entries = c.fetchall()
    conn.close()
    for entry in entries:
        website, username, encrypted_password, encrypted_email = entry
        decrypted_password = decrypt_data(fernet, encrypted_password)
        decrypted_email = decrypt_data(fernet, encrypted_email)
        print(f"Website: {website}\nUsername: {username}\nPassword: {decrypted_password}\nEmail: {decrypted_email}\n")

# Main function to interact with the user via terminal
def main():
    if not os.path.exists("passwords.db"):
        init_db()

    print("Welcome to the Portable Password & Email Manager!")

    # Ask for the master password
    master_password = getpass.getpass("Enter your master password: ")
    if not master_password:
        print("Master password is required. Exiting.")
        return

    # Generate a key from the master password
    key = generate_key(master_password)

    # Initialize the Fernet object using the generated key
    fernet = Fernet(key)

    while True:
        print("\nSelect an option:")
        print("1. Add new credential (website, username, password, email)")
        print("2. Retrieve credential by website")
        print("3. Update credential (website, new password, new email)")
        print("4. Delete credential by website")
        print("5. View all stored credentials")
        print("6. Exit")
        
        choice = input("Enter choice (1-6): ")

        if choice == '1':
            website = input("Enter website name: ")
            username = input("Enter username: ")
            password = getpass.getpass("Enter password: ")
            email = input("Enter email address: ")
            save_credentials(fernet, website, username, password, email)
            print(f"Credentials for {website} saved successfully!")

        elif choice == '2':
            website = input("Enter website name to retrieve: ")
            username, password, email = get_credentials(fernet, website)
            if username:
                print(f"\nWebsite: {website}\nUsername: {username}\nPassword: {password}\nEmail: {email}")
            else:
                print("No credentials found for this website.")

        elif choice == '3':
            website = input("Enter website name to update: ")
            new_password = getpass.getpass("Enter new password: ")
            new_email = input("Enter new email address: ")
            update_credentials(fernet, website, new_password, new_email)
            print(f"Credentials for {website} updated successfully!")

        elif choice == '4':
            website = input("Enter website name to delete: ")
            delete_credentials(website)
            print(f"Credentials for {website} deleted successfully!")

        elif choice == '5':
            view_all_credentials(fernet)

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
