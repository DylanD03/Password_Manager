import Password_Manager
import os
DEBUG = True

"""		
Password Manager v.2.0

New Feature(s):
Security  
	- Implement a master username/password to 'login' to password manager
	- Encrypted Passwords, need to log in to be able to see them.

	Using ssh hashing you need your master password to use the key stored in the users database.
	then with your key you can unencrypt information in the passwords database for that particular user.

TODO:
Extension
	-Turn this password manager into a google extension. - v.3.0
"""

	
def display_Main_Menu(options, current_user = None, try_again = 0):
	"""
	prints the Main Menu of the interface, displaying the options for the user 
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

	if try_again:
		print("\n Previous input is invalid, try again.")
		print(" Example Usage: \"1\"")
	print("--------------------------------------")





def safe_Input_Main(options):
	"""
	Ensures the input for the main menu is a valid input.
	The input should be an integer from 1-n where n is the number of options.

	Input: 
	(list of strings) : The options listed in the main menu.


	returns
	(string) user_Input : The option selected by the user. 

	"""
	while True: # Keep asking for input until a valid one is entered

		user_Input = input("\nYour Input: ") # TODO: Safe input function with exception handling. To cover erroneous inputs. Ex. no input 
		
		if user_Input == "q" or user_Input == "Q":
			return user_Input # to exit program
		if not user_Input.isdigit() or user_Input == '':
			display_Main_Menu(options, try_again = True)
			continue # try again
		# Input is a digit
		if int(user_Input) not in list(range(1, len(options)+1)):
			# try again. Input is not in the range of 1-n where n is the number of options
			display_Main_Menu(options, try_again = True)
			continue 

		return user_Input # valid input



def display_login_option(option, try_again = 0):
	"""
	After user selects one of their options, display the respective interface.

	"""
	print("--------------------------------------")
	print("\t" + "Password Manager v.2.0\n")
	print(" Enter \'q\' on keyboard to go back to Login Menu")
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


	if try_again:
		print("\n Previous input had invalid formatting, try again")
	print("--------------------------------------")

def safe_input_login_options(option):
	pass


def display_Option(options, try_again = 0):
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
	if try_again:
		print("\n Previous input is invalid, try again")
	print("--------------------------------------")






def safe_Input_Options(option): 
	while True: # never ending loop until input is a valid entry
	
		user_Input = input("\nYour Input: ") 

		if user_Input == "": # Invalid input for any operation.
			display_Option(option, 1)
			continue # try again

		if user_Input == 'q' or user_Input == 'Q':
			return user_Input


		if option == "Add Password":
			if len(user_Input.split()) == 3: # valid formatting (Username Password Website)
				inp = user_Input.split()
				if Password_Manager.is_Valid_Website(inp[2]):
					print("There already exists information for this website")
					print("Use \'Replace Information\' instead")
					print("Enter \'q\' on keyboard to go back to the Main Menu")
					continue
				else:
					Password_Manager.add_Password(inp[0], inp[1], inp[2])
					return user_Input
		elif option == "Delete Password":
			if len(user_Input.split()) == 1: # websites must have no blank spaces in its name. 
				if Password_Manager.is_Valid_Website(user_Input): 
					Password_Manager.delete_Password(user_Input) # information for the website exists in database
				else:
					print("\nThere is no information associated with this website")
					print("Enter \'q\' on keyboard to go back to the Main Menu")
					continue
				return user_Input
		elif option == "Show password from a Site": 
			if len(user_Input.split()) == 1: # websites must have no blank spaces in its name. 
				if Password_Manager.is_Valid_Website(user_Input):
					Password_Manager.show_website(user_Input)
				else:
					print("\nThere is no information associated with this website")
					print("Enter \'q\' on keyboard to go back to the Main Menu")
					continue
				return user_Input
		elif option == "View All":
			if user_Input == '1':
				if Password_Manager.count_all() == 0:
					print('You have no passwords saved!')
				else:
					Password_Manager.show_all()
				return user_Input
		elif option == "Delete All":
			if user_Input == 'y':
				Password_Manager.delete_Database()
				Password_Manager.initialize_Database()
				return user_Input
			elif user_Input == 'n':
				return user_Input
		elif option == "Replace Information":
			if len(user_Input.split()) == 3:
				inp = user_Input.split()
				if Password_Manager.is_Valid_Website(inp[2]):
					Password_Manager.delete_Password(inp[2])
				else:
					print("No pre-existing information was available to replace. Password will be added like normal")
				Password_Manager.add_Password(inp[2],inp[1],inp[2]) # Add the information regardless if information already existed for that particular website
				return user_Input

		display_Option(option, 1) # loop again until a valid input is used
		continue 				  # readability

	
		
def main():
	login_options = ["User Login", "Register User", "Delete User"]
	if DEBUG:
		login_options.append("See all users")
	options = ["Add Password", "Delete Password", "Show password from a Site", "View All", "Delete All", "Replace Information"]

	if not os.path.exists('./password_database.v.2.db'): # version 2 
		Password_Manager.initialize_Database() # Only creates database if it doesn't already exist.


	user = None
	while True:
		display_Main_Menu(login_options)
		user_Input = safe_Input_Main(login_options)

		if user_Input == "q" or user_Input == "Q":
			return 

		option = login_options[int(user_Input) - 1]
		display_login_option(option)


		if DEBUG:
			user_Entry = None

		user_Entry = safe_input_login_options(option)

		if user_Entry == "q" or user_Entry == "Q":
			continue # return to login screen

		return


	# Login is successful. Can access passwords database for that particular user.
	while True: 
		display_Main_Menu(options, current_user = user)
		user_Input = safe_Input_Main(options)

		if user_Input == "q" or user_Input == "Q":
			exit()
		
		option = options[int(user_Input) - 1]
		display_Option(option) # Valid option is selected, display the corresponding interface
		user_Entry = safe_Input_Options(option) # also processes the tasks if the entry is valid
		if user_Entry == "q" or user_Entry == "Q":
			continue # return to main menu
		elif user_Entry == "n": # from option (delete all)
			continue # return to main menu


		while True:
			print("--------------------------------------")
			print("\t" + "Password Manager v.1.1\n")
			print('Success!\nInput \'y\' to start again!')
			print("--------------------------------------")
			
			start_again = input('Your Input: ')
			if start_again == "y" or start_again == "Y":
				break

		


if __name__ == "__main__":
	main()


