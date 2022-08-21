import Password_Manager


def print_Default_Header():
	"""
	Prints the Header of the interface. 

	"""
	print("--------------------------------------")
	print("\t" + "Password Manager v.1.0\n")


def print_Default_Footer():
	"""
	Prints the Footer of the interface 

	"""
	print()
	print("--------------------------------------")



def display_Option(options, option_Number, try_again = 0):
	"""
	After user selects one of their options, display the respective interface.

	"""
	while True:
		option = options[option_Number-1]
		print_Default_Header()
		print(" Enter \'Q\' on keyboard to go back to Main Menu")
		print(" Selected Option #" + str(option_Number) + ": " + option)
		print()
		print(" to " + option + " Enter: ")

		if option_Number == 1: # Add Password
			print(" Username Password Website")
			print()
			print(" Example Usage: ")
			print(" myusername mypassword github")

		elif option_Number == 2: # Delete password
			Password_Manager.show_all()
			print()
			print("Enter the row number of the password to be deleted")


		elif option_Number == 3: # Show password from a site
			print(" Website")
			print()
			print(" Example Usage: ")
			print(" github")

		elif option_Number == 4:
			print(" \'1\'")

		elif option_Number == 5:
			print(" (y/n)\n")
			print(" Example Usage: 'y'")
			print(" note: ALL passwords will be deleted, and cannot be recovered")
			print(" Input 'n' or 'q' if you change your mind")

		if try_again == 1:
			print("\n Previous input is invalid, try again")

		print_Default_Footer()

		cFlag = 0
		user_Entry, cFlag = safe_Input_Options(options, option_Number)

		if cFlag: # proper input is used, can exit the 'option' screen
			break
		if not cFlag:
			try_again == 1 
			continue

	return user_Entry # later perform operation based on this user entry.


	
def display_Main_Menu(options, cFlag = 1):
	"""
	prints the Main Menu of the interface, displaying the options for the user 
	"""
	while True:

		print_Default_Header()
		print(" Here are your options:\n")


		# Displaying each option and it's coresponding reference number.
		for i, option in enumerate(options):
			# Example, "1 : Add Password"
			print(" " + str(i+1) + " : " + option)

		if not cFlag:
			print("  Incorrect Input:")
			print("  Example Usage: \"1\"")
		print("\n Or enter 'q' to exit the program")
		print_Default_Footer()


		user_Input, cFlag = safe_Input_Main(options)
		if not cFlag:
			continue  # Restart main menu but with example usage
		if cFlag: break

	return user_Input




def safe_Input_Main(options):

	user_Input = input("Your Input: ") # TODO: Safe input function with exception handling. To cover erroneous inputs. Ex. no input 
	
	if user_Input == "Q" or user_Input == "q":
		return user_Input, 1 # to exit program

	if user_Input == '' or not user_Input.isdigit():
		return '', 0 # Incorrect usage
	user_Input = int(user_Input) # Valid input in the main menu is an integer from 1 to the amount of options available.
	if user_Input not in list(range(1, len(options)+1)):
		return '', 0 # The integer is not listed as one of the options
	else:
		return user_Input, 1 


def safe_Input_Options(options, option_Number): # maybe change var name to option_Choice?
	
	user_Input = input("Your Input: ") 


	return option_Number, 1 
	




def main():
	cFlag = 1
	options = ["Add Password", "Delete Password", "Show password from a Site", "View All", "Delete All"]

	user_Input = display_Main_Menu(options, cFlag) # Exits the main menu once a valid entry has been used.

	if user_Input == "q" or user_Input == "Q":
		return 0  

	user_Entry = display_Option(options, user_Input) # Valid option is selected, display the corresponding interface















if __name__ == "__main__":
	bb = main()
