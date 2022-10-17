"""		
New Features in version 2.0
	- Now supports multiple users.
	- Must login to your account to view your passwords.
	- Passwords are now encrypted before storage
"""
# Import modules
from database_manager import *
from secure import *
import os
DEBUG = False


def print_login_menu(option, error_msg = None):
	"""
	After user selects one of their options display the respective interface.
	
	Parameters :
	option (string) : The selection made by the user in the log in screen.
	error_msg (string) : If neccessary, display an error message to indicate that invalid input was used.
	
	Returns : 
	None
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



def print_user_menu(options, error_msg = None, current_user = None):
	"""
	Displays Login Menu

	Parameters:

	options (list of strings) : The options listed in the main menu.
	error_msg (string): To display at the bottom of the main menu
	current_user (string): username

	Returns:
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




def login_menu_selection(options):
	"""
	User selects an integer from 1-n. For example, selecting '2' allows you to register a new account.

	Parameters: 
	options (list of strings) : The options listed in the main menu.


	Returns
	(string) user_Input : The option selected by the user. 
	"""
	while True: # Keep asking for input until a valid one is entered

		user_Input = input("\nYour Input: ") # TODO: Safe input function with exception handling. To cover erroneous inputs. Ex. no input 

		if user_Input == "q" or user_Input == "Q":
			return user_Input # to exit program
		if not user_Input.isdigit() or user_Input == '':
			error_msg = " Invalid input formatting, try again. "
			print_user_menu(options, error_msg)
			continue # try again
		# Input is a digit
		if int(user_Input) not in list(range(1, len(options)+1)):
			# try again. Input is not in the range of 1-n where n is the number of options
			error_msg = " Invalid input formatting, try again. "
			print_user_menu(options, error_msg)
			continue 

		return user_Input # valid input



def process_login_selection(option):
	"""
	Proccessing user input in the Login screen. 

	Parameters:

	option (string) : The selection made by the user in the Login screen.

	Returns:
	None
	"""
	while True:

		user_Input = input('Your Input: ')
		if user_Input == "": # Invalid input for any operation.
			error_msg = " Error: Must have an input!"
			print_login_menu(option, error_msg)
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
				print_login_menu(option, error_msg)
				continue
		elif option == "Register User":
			if len(inp) == 2:
				if is_valid_user(inp[0]):
					error_msg = " This user already exists. Try another username!"
					print_login_menu(option, error_msg)
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
						print_login_menu(option, error_msg)
						continue
				else:
					error_msg = " There are no users with name: \'" + inp[0] + " \'to delete"
					print_login_menu(option, error_msg)
					continue
			
		if DEBUG:
			if option == "See all users":
				if user_Input == '1':
					get_all_users()
					print_success()
					return


		error_msg = " Invalid input formatting, try again."
		print_login_menu(option, error_msg) 			# loop again until a valid input is used
		continue											# readability




def display_user_options(option, error_msg = None):
	"""
	After a user has logged in to their account, display what they can do. For example, add/delete password.
	
	Includes example usage, how to exit the program, and instructions on how to use the program.

	Parameters:

	option (string) : The selection made by the user in the log in screen.
	error_msg (string): To display at the bottom of the main menu in case invalid input was used previously.

	Returns:
	None
	"""

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



def process_user_options(option, user, encryption_key): 
	"""
	After a user has logged in and selected their option, for example add a new password, this function will ask a user to input their data
	and will proccess their information if the correct formatting is found.

	Parameters:

	option (string) : The selection made by the user in the log in screen.
	user (string) : The username used to log into the password manager
	encryption_key (string): Key used to encrypt/decrypt passwords.

	Returns:
	user_Input (string) : Returns the user input when a valid input has been entered.
	"""
	while True: # never ending loop until input is a valid entry
	
		user_Input = input("\nYour Input: ") 

		if user_Input == "": # Invalid input for any operation.
			error_msg = "Invalid input formatting, try again."
			display_user_options(option, error_msg)
			continue # try again

		if user_Input == 'q' or user_Input == 'Q':
			return user_Input


		if option == "Add Password":
			if len(user_Input.split()) == 3: # valid formatting : (Username Password Website)
				inp = user_Input.split()
				if is_Valid_Website(user, inp[2]):
					error_msg = "Information for this website already exists.\n"
					error_msg += " Use the \'Replace Information\' option instead."
					display_user_options(option, error_msg)
					continue
				else:
					encrypted_pass = encrypt_password(inp[1], encryption_key)
					add_Password(user, inp[0], encrypted_pass, inp[2]) # : (user, username, encrypted pass, website)
					return user_Input
		elif option == "Delete Password":
			if len(user_Input.split()) == 1: # websites must have no blank spaces in its name. 
				if is_Valid_Website(user, user_Input): 
					delete_Password(user, user_Input) # information for the website exists in database
				else:
					error_msg = "There is no information associated with this website"
					display_user_options(option, error_msg)
					continue
				return user_Input
		elif option == "Show password from a Site": 
			if len(user_Input.split()) == 1: # websites must have no blank spaces in its name. 
				if is_Valid_Website(user, user_Input):
					item = show_website(user, user_Input)
					print((item[0]), decrypt_password(item[1], encryption_key), item[2])
				else:
					error_msg = "There is no information associated with this website"
					display_user_options(option, error_msg)
					continue
				return user_Input
		elif option == "View All":
			if user_Input == '1':
				if count_all(user) == 0:
					print('You have no passwords saved!')
				else:
					items = show_all(user) # list of lists
					for item in items:
						print((item[0], decrypt_password(item[1], encryption_key), item[2])) # (Username Password Website)
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
				encrypted_pass = encrypt_password(inp[1], encryption_key)
				add_Password(user, inp[0], encrypted_pass, inp[2]) # Add the information regardless if information already existed for that particular website
				return user_Input

		error_msg = "Invalid input formatting, try again."
		display_user_options(option, error_msg) # loop again until a valid input is used
		continue 				  # readability



def print_success():
	"""
	Displays a message indicating that the password manager has successfully processed the user input.
	User can start again after inputting "y" or "Y".
	
	Parameters:
	None

	Returns:
	None
	"""
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
		print_user_menu(login_options)
		user_Input = login_menu_selection(login_options)

		if user_Input == "q" or user_Input == "Q":
			return 

		option = login_options[int(user_Input) - 1]
		print_login_menu(option)


		if DEBUG:
			user_Entry = None

		user_Entry = process_login_selection(option) # returns q to quit, or a valid username if password matches

		if user_Entry == "q" or user_Entry == "Q":
			continue # return to login screen

		if user_Entry != None:
			user = user_Entry
			encryption_key = retrieve_key(user)
			logged_in = True
			break



	# Login is successful. Can access passwords database for that particular user.
	while logged_in: 
		print_user_menu(options, current_user = user)
		user_Input = login_menu_selection(options)

		if user_Input == "q" or user_Input == "Q": 
			exit()
		
		option = options[int(user_Input) - 1]
		display_user_options(option) # Valid option is selected, display the corresponding interface
		user_Entry = process_user_options(option, user, encryption_key) # also processes the tasks if the entry is valid
		if user_Entry == "q" or user_Entry == "Q":
			continue # return to main menu
		elif user_Entry == "n": # from option (delete all)
			continue # return to main menu

		print_success()
		

		


if __name__ == "__main__":
	main()


