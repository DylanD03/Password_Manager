import sqlite3
from cryptography.fernet import Fernet
import hashlib


# passwords database

def connect_to_Database():
	"""
	returns a cursor to the database named password_database.db
	"""
	connection = sqlite3.connect('password_database.db')
	cur = connection.cursor()

	return connection, cur



def commit_to_Database(connection):
	connection.commit()
	connection.close()



def initialize_Database():
	"""
	Creates the database file, 'password_database.db'
	Creates the table named 'passwords' inside that database file.
	"""
	connection, cur = connect_to_Database()

	cur.execute("CREATE TABLE IF NOT EXISTS users (user TEXT, hashed_password TEXT, encryption_key TEXT)")
	cur.execute("CREATE TABLE IF NOT EXISTS passwords (user TEXT, username TEXT, encrypted_password TEXT, website TEXT)")
	
	commit_to_Database(connection)



def delete_Database():
	"""
	Completely deletes the database containing all username/password/website information.
	i.e. deletes 'password_database.db'

	"""
	connection, cur = connect_to_Database()

	cur.execute("DROP TABLE passwords")
	cur.execute("DROP TABLE users")

	commit_to_Database(connection)



def add_Password(current_user, username, encrypted_password, website):
	"""
	Example usage:
		add_Password(myuser, myusername, mypassword, github)

	"""
	connection, cur = connect_to_Database()

	cur.execute("INSERT INTO passwords VALUES (?,?,?,?)", (current_user, username, encrypted_password, website))
	# password should be encrypted
	commit_to_Database(connection)



def delete_Password(current_user, queried_site):
	"""
	Deletes the targetted password from the database
	"""

	connection, cur = connect_to_Database()

	cur.execute("DELETE FROM passwords WHERE user = (?) AND website = (?)", (current_user, queried_site)) 

	commit_to_Database(connection)



def show_all(current_user):
	"""
	returns all username/passwords/website information
	list of lists.
	"""
	connection, cur = connect_to_Database()

	cur.execute("SELECT username, encrypted_password, website FROM passwords WHERE user = (?)", (current_user,))
	items = cur.fetchall()
	for item in items:     #####
		print(item)

	commit_to_Database(connection)
	return items



def show_website(current_user, queried_site):
	"""
	Returns username/password from a specific website:
	connection = sqlite3.connect('password_database.db')
	"""
	connection, cur = connect_to_Database()

	cur.execute("SELECT username, encrypted_password, website FROM passwords WHERE user = (?) AND website = (?)", (current_user, queried_site))
	item = cur.fetchone()
	commit_to_Database(connection)
	print(item)     #######

	return item


def is_Valid_Website(current_user, queried_site):

	connection, cur = connect_to_Database()	
	cur.execute("SELECT username, encrypted_password, website FROM passwords WHERE user = (?) AND website = (?)", (current_user, queried_site))
	items = cur.fetchall()
	for item in items:
		if item[2] == queried_site:
			commit_to_Database(connection)
			return True

	commit_to_Database(connection)
	return False


def count_all(current_user):
	"""
	returns number of user/pass/web entries are in the database for a particular user.
	"""
	connection, cur = connect_to_Database()

	cur.execute("SELECT * FROM passwords WHERE user = (?)", (current_user,))
	items = cur.fetchall()
	commit_to_Database(connection)
	print(items)
	return len(items)

def replace_instance(current_user, website):
	"""
	for a particular user,
	replaces information for a website by deleting the old entry and replacing it with the new one.

	"""
	pass # future implementation


# users database
# https://www.geeksforgeeks.org/how-to-encrypt-and-decrypt-strings-in-python/
# Cryptography
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


