import os
from Crypto.Cipher import AES

# Set encryption mode
mode = AES.MODE_CBC

# Define block size for AES encryption
block_size = 16

# Function for generating encryption key
def generate_key():
    # Generate key from random bytes
    key = os.urandom(block_size)
    return key

# Function for padding message
def pad_message(message):
    # Calculate padding size
    padding_size = block_size - len(message) % block_size

    # Pad message with filler characters
    padded_message = message + padding_size * chr(padding_size)

    return padded_message

# Function for encrypting message
def encrypt_message(message, key):
    # Pad message
    padded_message = pad_message(message)

    # Generate random initialization vector
    iv = os.urandom(block_size)

    # Create AES encryption object
    cipher = AES.new(key, mode, iv)

    # Encrypt message using AES encryption in CBC mode
    encrypted_message = iv + cipher.encrypt(padded_message.encode())

    return encrypted_message

# Function for decrypting message
def decrypt_message(encrypted_message, key):
    # Extract initialization vector from encrypted message
    iv = encrypted_message[:block_size]

    # Create AES decryption object
    cipher = AES.new(key, mode, iv)

    # Decrypt message using AES encryption in CBC mode
    decrypted_message = cipher.decrypt(encrypted_message[block_size:]).decode()

    # Remove filler characters from decrypted message
    unpadded_message = decrypted_message[:-ord(decrypted_message[-1])]

    return unpadded_message

# Generate encryption key
key = generate_key()

# Get text input from user
text = input("Enter text to encrypt: ")

# Encrypt message
encrypted_message = encrypt_message(text, key)

# Display encrypted message and key
print("Encrypted message: ", encrypted_message)
print("Encryption key: ", key)

# Decrypt message
decrypted_message = decrypt_message(encrypted_message, key)

# Display decrypted message
print("Decrypted message: ", decrypted_message)