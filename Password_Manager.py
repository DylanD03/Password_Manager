import sqlite3

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

	cur.execute("CREATE TABLE IF NOT EXISTS passwords (username TEXT, password TEXT, website TEXT)")
	
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



def delete_Password(queried_site):
	"""
	Deletes the targetted password from the database
	"""

	connection, cur = connect_to_Database()

	cur.execute("DELETE FROM passwords WHERE website = (?)", (queried_site,))

	commit_to_Database(connection)



def show_all():
	"""
	Displays all username/passwords/website information
	"""
	connection, cur = connect_to_Database()

	cur.execute("SELECT * FROM passwords")
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
	if len(items) == 0:
		print('None Available')
	else: 
		for item in items:
			print(item)

	commit_to_Database(connection)


def is_Valid_Website(queried_site):

	connection, cur = connect_to_Database()	
	cur.execute("SELECT * FROM passwords WHERE website = (?)", (queried_site,))
	items = cur.fetchall()
	for item in items:
		if item[2] == queried_site:
			return True

	commit_to_Database(connection)
	return False


def count_all():
	"""
	returns number of user/pass/web entries are in the database.
	"""
	connection, cur = connect_to_Database()

	cur.execute("SELECT rowid, * FROM passwords")
	items = cur.fetchall()
	commit_to_Database(connection)

	return len(items)


