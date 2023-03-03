Console application for encrypting and decrypting text messages using AES algorithm

This program is a console application written in Python that allows you to encrypt and decrypt text messages using the AES algorithm.

When the program is launched, the user should enter the text of the message that needs to be encrypted. Then the program automatically generates a random encryption key and uses it to encrypt the message in CBC mode. The encrypted message is displayed on the screen as a byte string, and the encryption key is also displayed.

To decrypt the message, the user should enter the encrypted message and the encryption key. The program extracts the initialization vector from the encrypted message, creates an AES decryption object, and uses it to decrypt the message in CBC mode. The decrypted message is displayed on the screen.

pip install pycrypto
