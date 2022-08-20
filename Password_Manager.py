import sqlite3

"""
VERY SIMPLE password manager.
Usage:
	You can manually type in your usernames/passwords into the database 
	Can retrieve all usernames/passwords, or from specific sites.

Passwords in the database stored as
[username, password, website]

TODO:
Security
	- Implement a master username/password to 'login' to password manager
	- Encrpt passwords, maybe using SSH hashing?

Extension
	-Turn this password manager into a google extension.
"""


def initialize_Database():
	"""
	Creates the database file, 'password_database.db'
	Creates the table named 'passwords' inside that database file.
	"""
	connection = sqlite3.connect('password_database.db')
	cur = connection.cursor()

	cur.execute("CREATE TABLE passwords (username TEXT, password TEXT, website TEXT)")
	
	connection.commit()
	connection.close()



def delete_Database():
	"""
	Completely deletes the database containing all username/password/website information.
	i.e. deletes 'password_database.db'

	"""
	connection = sqlite3.connect('password_database.db')
	cur = connection.cursor()

	cur.execute("DROP TABLE passwords")

	connection.commit()
	connection.close()



def add_Password(username, password, website):
	"""
	Example usage:
		add_Password(myusername, mypassword, github)

	"""
	connection = sqlite3.connect('password_database.db')
	cur = connection.cursor()

	cur.execute("INSERT INTO passwords VALUES (?,?,?)", (username, password, website))

	connection.commit()
	connection.close()


def show_all():
	"""
	Displays all username/passwords/website information
	"""
	connection = sqlite3.connect('password_database.db')
	cur = connection.cursor()

	cur.execute("SELECT rowid, * FROM passwords")
	items = cur.fetchall()
	for item in items:
		print(item)

	connection.commit()
	connection.close()
	
def show_website(queried_site):
	"""
	Displays username/password from a specific website:
	connection = sqlite3.connect('password_database.db')
	"""
	connection = sqlite3.connect('password_database.db')
	cur = connection.cursor()	

	cur.execute("SELECT * FROM passwords WHERE website = (?)", (queried_site,))
	items = cur.fetchall()
	for item in items:
		print(item)

	connection.commit()
	connection.close()



	