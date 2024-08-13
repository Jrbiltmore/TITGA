
# encryption_handler.py

import logging
from cryptography.fernet import Fernet

# Configure logging
logging.basicConfig(filename='/mnt/data/TIGTA_Automation_Suite/CyberSecurity/Logs/encryption.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def generate_key():
    """Generates a new encryption key."""
    key = Fernet.generate_key()
    with open('/mnt/data/TIGTA_Automation_Suite/CyberSecurity/Keys/private_key.pem', 'wb') as key_file:
        key_file.write(key)
    logging.info("New encryption key generated and saved.")
    print("New encryption key generated and saved.")

def load_key():
    """Loads the encryption key from a file."""
    return open('/mnt/data/TIGTA_Automation_Suite/CyberSecurity/Keys/private_key.pem', 'rb').read()

def encrypt_message(message):
    """Encrypts a message using the loaded key."""
    try:
        key = load_key()
        fernet = Fernet(key)
        encrypted_message = fernet.encrypt(message.encode())
        logging.info("Message encrypted successfully.")
        print("Message encrypted successfully.")
        return encrypted_message
    except Exception as e:
        logging.error(f"Error in encrypting message: {e}")
        print(f"Error: {e}")
        return None

def decrypt_message(encrypted_message):
    """Decrypts an encrypted message using the loaded key."""
    try:
        key = load_key()
        fernet = Fernet(key)
        decrypted_message = fernet.decrypt(encrypted_message).decode()
        logging.info("Message decrypted successfully.")
        print("Message decrypted successfully.")
        return decrypted_message
    except Exception as e:
        logging.error(f"Error in decrypting message: {e}")
        print(f"Error: {e}")
        return None

# Example usage
if __name__ == "__main__":
    generate_key()
    secret_message = "This is a top secret message."
    encrypted = encrypt_message(secret_message)
    print(f"Encrypted: {encrypted}")
    decrypted = decrypt_message(encrypted)
    print(f"Decrypted: {decrypted}")
