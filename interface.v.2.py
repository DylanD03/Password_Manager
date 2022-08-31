"""		
Password Manager v.2.0

New Feature(s in v.2.0 :
Security:
	- Implement a master username/password to 'login' to password manager
	- Encrypted Passwords, need to log in to be able to see them.
	- Passwords in the database are encrypted before storage.

TODO:
Extension
	-Turn this password manager into a google extension. - v.3.0
"""
from password_ManagerV2 import (
	initialize_Database, add_Password, delete_Password, show_all, show_website, 
	is_Valid_Website, count_all, add_user, delete_user, is_valid_user, 
	get_user_hashed_password, get_all_users, retrieve_key, delete_Database_User,
)
from secure import hash_password, generate_key, encrypt_message, decrypt_message
import os
DEBUG = True


def display_Main_Menu(options, error_msg = None, current_user = None):
	"""
	Displays the main menu for the user login and what options a user has after they log in.

	Input:

	options (list of strings) : The options listed in the main menu.
	error_msg (string): To display at the bottom of the main menu
	current_user (string): username

	returns:
	None
	"""

	print("--------------------------------------")
	print("\t" + "Password Manager v.2.0\n")
	if current_user is not None:
		print(" Welcome, " + current_user)
	print(" Here are your options:\n")

	# Displaying each option and it's coresponding reference number.
	for i, option in enumerate(options):
		print(" " + str(i+1) + " : " + option) # Example, " 1 : Add Password"

	print("\n Or enter 'q' to exit the program")

	if error_msg is not None:
		print('\n' + error_msg)
	print("--------------------------------------")




def safe_Input_Main(options):
	"""
	Ensures the input for the main menu is a valid input.
	The input should be an integer from 1-n where n is the number of options.

	Input: 
	options (list of strings) : The options listed in the main menu.


	returns
	(string) user_Input : The option selected by the user. 

	"""
	while True: # Keep asking for input until a valid one is entered

		user_Input = input("\nYour Input: ") # TODO: Safe input function with exception handling. To cover erroneous inputs. Ex. no input 
		
		if user_Input == "q" or user_Input == "Q":
			return user_Input # to exit program
		if not user_Input.isdigit() or user_Input == '':
			error_msg = " Invalid input formatting, try again. "
			display_Main_Menu(options, error_msg)
			continue # try again
		# Input is a digit
		if int(user_Input) not in list(range(1, len(options)+1)):
			# try again. Input is not in the range of 1-n where n is the number of options
			error_msg = " Invalid input formatting, try again. "
			display_Main_Menu(options, error_msg)
			continue 

		return user_Input # valid input




def display_login_option(option, error_msg = None):
	"""
	After user selects one of their options, display the respective interface.

	"""
	print("--------------------------------------")
	print("\t" + "Password Manager v.2.0\n")
	print(" Enter \'q\' on keyboard to go back to the Main Menu")
	print(" Selected Option : " + option)
	print()
	print(" to " + option + " Enter: ")

	if option == "User Login":
		print(" Username Password")
		print()
		print(" Example Usage:\n userLogin userPassword") 
	elif option == "Register User": 
		print(" Username Password")
		print()
		print(" Example Usage:\n userLogin userPassword")
	elif option == "Delete User":
		print(" Username Password")
		print()
		print(" Example Usage:\n userLogin userPassword")

	if DEBUG:
		if option == "See all users":
			print(" \'1\'\n")

	if error_msg is not None:
		print('\n' + error_msg)
	print("--------------------------------------")



def display_Option(option, error_msg = None):
	print("--------------------------------------")
	print("\t" + "Password Manager v.2.0\n")
	print(" Enter \'q\' on keyboard to go back to Main Menu")
	print(" Selected Option : " + option)
	print()
	print(" to " + option + " Enter: ")

	if option == "Add Password":
		print(" Username Password Website")
		print()
		print(" Example Usage:\n myusername mypassword github")
	elif option == "Delete Password": 
		print()
		print(" The website of the password to be deleted")
		print(" Example Usage:\n Github")
	elif option == "Show password from a Site": 
		print(" Website")
		print()
		print(" Example Usage:\n Github")
	elif option == "View All":
		print(" \'1\'")
	elif option == "Delete All":
		print(" (y/n)\n")
		print(" Example Usage: 'y'")
		print(" note: ALL passwords will be deleted, and cannot be recovered")
		print(" Input 'n' if you change your mind")
	elif option == "Replace Information":
		print(" New Username, New Password, and the website you want to replace")
		print()
		print(" Example Usage:\n NEWuser NEWpass github")
	if error_msg is not None:
		print('\n ' + error_msg)
	print("--------------------------------------")



def safe_Input_Options(option, user, encryption_key): 
	while True: # never ending loop until input is a valid entry
	
		user_Input = input("\nYour Input: ") 

		if user_Input == "": # Invalid input for any operation.
			error_msg = "Invalid input formatting, try again."
			display_Option(option, error_msg)
			continue # try again

		if user_Input == 'q' or user_Input == 'Q':
			return user_Input


		if option == "Add Password":
			if len(user_Input.split()) == 3: # valid formatting : (Username Password Website)
				inp = user_Input.split()
				if is_Valid_Website(user, inp[2]):
					error_msg = "Information for this website already exists.\n"
					error_msg += " Use the \'Replace Information\' option instead."
					display_Option(option, error_msg)
					continue
				else:
					encrypted_pass = encrypt_message(inp[1], encryption_key)
					add_Password(user, inp[0], encrypted_pass, inp[2]) # : (user, username, encrypted pass, website)
					return user_Input
		elif option == "Delete Password":
			if len(user_Input.split()) == 1: # websites must have no blank spaces in its name. 
				if is_Valid_Website(user, user_Input): 
					delete_Password(user, user_Input) # information for the website exists in database
				else:
					error_msg = "There is no information associated with this website"
					display_Option(option, error_msg)
					continue
				return user_Input
		elif option == "Show password from a Site": 
			if len(user_Input.split()) == 1: # websites must have no blank spaces in its name. 
				if is_Valid_Website(user, user_Input):
					item = show_website(user, user_Input)
					print((item[0]), decrypt_message(item[1], encryption_key), item[2])
				else:
					error_msg = "There is no information associated with this website"
					display_Option(option, error_msg)
					continue
				return user_Input
		elif option == "View All":
			if user_Input == '1':
				if count_all(user) == 0:
					print('You have no passwords saved!')
				else:
					items = show_all(user) # list of lists
					for item in items:
						print((item[0], decrypt_message(item[1], encryption_key), item[2])) # (Username Password Website)
				return user_Input
		elif option == "Delete All":
			if user_Input == 'y':
				delete_Database_User(user)
				return user_Input
			elif user_Input == 'n':
				return user_Input
		elif option == "Replace Information":
			if len(user_Input.split()) == 3:
				inp = user_Input.split()
				if is_Valid_Website(user, inp[2]):
					delete_Password(user, inp[2])
				else:
					print("\nNo pre-existing information was available to replace.\nPassword will be added to the database.\n")
				encrypted_pass = encrypt_message(inp[1], encryption_key)
				add_Password(user, inp[0], encrypted_pass, inp[2]) # Add the information regardless if information already existed for that particular website
				return user_Input

		error_msg = "Invalid input formatting, try again."
		display_Option(option, error_msg) # loop again until a valid input is used
		continue 				  # readability




def safe_input_login_options(option):
	while True:

		user_Input = input('Your Input: ')
		if user_Input == "": # Invalid input for any operation.
			error_msg = " Error: Must have an input!"
			display_login_option(option, error_msg)
			continue # try again

		if user_Input == 'q' or user_Input == 'Q':
			return user_Input

		inp = user_Input.split() # [username, password]

		if option == "User Login":
			if len(inp) == 2:
				if is_valid_user(inp[0]):
					if hash_password(inp[1]) == get_user_hashed_password(inp[0]):
						return inp[0] # Successful login, can proceed to interact with password database				
				error_msg = " Invalid username/password. Try again."
				display_login_option(option, error_msg)
				continue
		elif option == "Register User":
			if len(inp) == 2:
				if is_valid_user(inp[0]):
					error_msg = " This user already exists. Try another username!"
					display_login_option(option, error_msg)
					continue
				else:	
					add_user(inp[0], hash_password(inp[1]), generate_key()) 
					print_success()
					return # restart to login screen

		elif option == "Delete User":
			if len(inp) == 2:
				if is_valid_user(inp[0]):
					if hash_password(inp[1]) == get_user_hashed_password(inp[0]):
						delete_user(inp[0])
						print_success()
						return # restart to login screen
					else:
						error_msg = " Entered Incorrect password. Cannot Delete user."
						display_login_option(option, error_msg)
						continue
				else:
					error_msg = " There are no users with name: \'" + inp[0] + " \'to delete"
					display_login_option(option, error_msg)
					continue
			
		if DEBUG:
			if option == "See all users":
				if user_Input == '1':
					get_all_users()
					print_success()
					return


		error_msg = " Invalid input formatting, try again."
		display_login_option(option, error_msg) 			# loop again until a valid input is used
		continue											# readability


def print_success():
	while True:
		print("--------------------------------------")
		print("\t" + "Password Manager v.2.0\n")
		print('Success!\nInput \'y\' to start again!')
		print("--------------------------------------")
		
		start_again = input('Your Input: ')
		if start_again == "y" or start_again == "Y":
			break
	return


		
def main():
	login_options = ["User Login", "Register User", "Delete User"]
	if DEBUG:
		login_options.append("See all users")
	options = ["Add Password", "Delete Password", "Show password from a Site", "View All", "Delete All", "Replace Information"]

	if not os.path.exists('./password_database.v.2.db'): # version 2 
		initialize_Database() # Only creates database if it doesn't already exist.


	user = None
	encryption_key = None
	logged_in = False
	while True: # Log in menu
		display_Main_Menu(login_options)
		user_Input = safe_Input_Main(login_options)

		if user_Input == "q" or user_Input == "Q":
			return 

		option = login_options[int(user_Input) - 1]
		display_login_option(option)


		if DEBUG:
			user_Entry = None

		user_Entry = safe_input_login_options(option) # returns q to quit, or a valid username if password matches

		if user_Entry == "q" or user_Entry == "Q":
			continue # return to login screen

		if user_Entry != None:
			user = user_Entry
			encryption_key = retrieve_key(user)
			logged_in = True
			break



	# Login is successful. Can access passwords database for that particular user.
	while logged_in: 
		display_Main_Menu(options, current_user = user)
		user_Input = safe_Input_Main(options)

		if user_Input == "q" or user_Input == "Q": 
			exit()
		
		option = options[int(user_Input) - 1]
		display_Option(option) # Valid option is selected, display the corresponding interface
		user_Entry = safe_Input_Options(option, user, encryption_key) # also processes the tasks if the entry is valid
		if user_Entry == "q" or user_Entry == "Q":
			continue # return to main menu
		elif user_Entry == "n": # from option (delete all)
			continue # return to main menu

		print_success()
		

		


if __name__ == "__main__":
	main()


