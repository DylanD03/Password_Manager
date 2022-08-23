import Password_Manager
import os

"""		
Password Manager v.1.2
Usage:
	You can manually type in your usernames/passwords into the database 
	Can retrieve all usernames/passwords, or from specific sites.

Passwords in the database stored as
[username, password, website]

TODO:
Implement Feature(s):
	- Overriding a row of information in database.
Security
	- Implement a master username/password to 'login' to password manager
	- Encrpt passwords, maybe using SSH hashing?

Extension
	-Turn this password manager into a google extension.
"""


	
def display_Main_Menu(options, try_again = 0):
	"""
	prints the Main Menu of the interface, displaying the options for the user 
"""

	print("--------------------------------------")
	print("\t" + "Password Manager v.1.2\n")
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
		
		if user_Input == "Q" or user_Input == "q":
			return user_Input # to exit program
		if not user_Input.isdigit() or user_Input == '':
			display_Main_Menu(options, True)
			continue # try again
		# Input is a digit
		if int(user_Input) not in list(range(1, len(options)+1)):
			# try again. Input is not in the range of 1-n where n is the number of options
			display_Main_Menu(options, True)
			continue 

		return user_Input # valid input




def display_Option(option, try_again = 0):
	"""
	After user selects one of their options, display the respective interface.

	"""
	# while True: # Keep displying that option screen until a valid input has been entered.

	print("--------------------------------------")
	print("\t" + "Password Manager v.1.1\n")
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
	if try_again:
		print("\n Previous input is invalid, try again")
	print("--------------------------------------")




def safe_Input_Options(option): 
	while True: # never ending loop until input is a valid entry
	
		user_Input = input("\nYour Input: ") 

		if user_Input == "": # Invalid input for any operation.
			return user_Input

		if user_Input == 'q' or user_Input == 'Q':
			return user_Input


		if option == "Add Password":
			if len(user_Input.split()) == 3: # valid formatting (Username Password Website)
				inp = user_Input.split()
				Password_Manager.add_Password(inp[0], inp[1], inp[2])
				return user_Input
		elif option == "Delete Password": 
			if Password_Manager.is_Valid_Website(user_Input): # information for the website exists in database
				Password_Manager.delete_Password(user_Input)
				return user_Input
		elif option == "Show password from a Site": 
			if len(user_Input.split()) == 1: # websites must have no blank spaces in its name. 
				if not Password_Manager.is_Valid_Website():
					print(" There is no information associated with this website")
				else:
					Password_Manager.show_website(user_Input)
				return user_Input
		elif option == "View All":
			if user_Input == '1':
				Password_Manager.show_all()
				return user_Input
		elif option == "Delete All":
			if user_Input == 'y':
				Password_Manager.delete_Database()
				Password_Manager.initialize_Database()
				return user_Input
			elif user_Input == 'n':
				return user_Input
		else:
			display_Option(option, 1) # loop again until a valid input is used
			continue 				  # readability

	
		
def main():
	options = ["Add Password", "Delete Password", "Show password from a Site", "View All", "Delete All"]
	if not os.path.exists('./password_database.db'):
		Password_Manager.initialize_Database() # Only creates database if it doesn't already exist.

	while True:
		display_Main_Menu(options)
		user_Input = safe_Input_Main(options)
		if user_Input == "q" or user_Input == "Q":
			return # exits the program
		
		option = options[int(user_Input)-1]
		display_Option(option) # Valid option is selected, display the corresponding interface
		user_Entry = safe_Input_Options(option) # also processes the tasks if the entry is valid
		if user_Entry == "q" or user_Entry == "Q":
			continue # return to main menu
		elif user_Entry == "n":
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


