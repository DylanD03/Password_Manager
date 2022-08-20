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

	cur.execute("CREATE TABLE passwords (username TEXT, password TEXT, website TEXT)")
	
	commit_to_Database(connection)



def delete_Database():
	"""
	Completely deletes the database containing all username/password/website information.
	i.e. deletes 'password_database.db'

	"""
	connection, cur = connect_to_Database()

	cur.execute("DROP TABLE passwords")

	commit_to_Database(connection)



def add_Password(username, password, website):
	"""
	Example usage:
		add_Password(myusername, mypassword, github)

	"""
	connection, cur = connect_to_Database()

	cur.execute("INSERT INTO passwords VALUES (?,?,?)", (username, password, website))

	commit_to_Database(connection)



def delete_Password(row_Number):
	"""
	Deletes the targetted password from the database
	"""

	connection, cur = connect_to_Database()

	cur.execute("DELETE FROM passwords WHERE rowid = (?)", row_Number)

	commit_to_Database(connection)



def show_all():
	"""
	Displays all username/passwords/website information
	"""
	connection, cur = connect_to_Database()

	cur.execute("SELECT rowid, * FROM passwords")
	items = cur.fetchall()
	for item in items:
		print(item)

	commit_to_Database(connection)

	


def show_website(queried_site):
	"""
	Displays username/password from a specific website:
	connection = sqlite3.connect('password_database.db')
	"""
	connection, cur = connect_to_Database()

	cur.execute("SELECT * FROM passwords WHERE website = (?)", (queried_site,))
	items = cur.fetchall()
	for item in items:
		print(item)

	commit_to_Database(connection)



