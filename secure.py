# https://www.geeksforgeeks.org/how-to-encrypt-and-decrypt-strings-in-python/
# Cryptography
from cryptography.fernet import Fernet
import hashlib

def hash_password(password):

	encoded_password = password.encode()
	hashed_password = hashlib.sha256(encoded_password)

	return hashed_password


def generate_key():

	key = Fernet.generate_key()
	return key

def encrypt_message(message, key):

	fernet = Fernet(key)
	encoded_message = message.encode()
	encrypted_message = fernet.encrypt(encoded_message)

	return encrypted_message

def decrypt_mesage(encrypted_message, key):

	fernet = Fernet(key)
	encoded_message = fernet.decrypt(encrypted_message)
	message = encoded_message.decode()

	return message