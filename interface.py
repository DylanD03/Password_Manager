import Password_Manager


def print_Default_Header():
	"""
	Prints the header of the interface. 

	"Password Manger v.x.y"

	"""
	print("--------------------------------------")
	print("\t" + "Password Manager v.1.0\n")


def print_Default_Footer():
	"""
	Prints the Footer of the interface 


	"""
	print()
	print("--------------------------------------")



def display_Option(options, option_Number):
	"""
	After user selects one of their options, display the respective interface.

	"""
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

	print_Default_Footer()



	
def display_Main_Menu(options, cFlag = 1):
	"""
	prints the Main Menu of the interface, displaying the options for the user 
	"""
	print_Default_Header()
	print(" Here are your options:\n")

	# Displaying each option and it's coresponding reference number.
	for i, option in enumerate(options):
		# Example, "1 : Add Password"
		print(" " + str(i+1) + " : " + option)

	if not cFlag:
		print("  Incorrect Input:")
		print("  Example Usage: \"1\"")

	print_Default_Footer()



def safe_Input(options):

	user_Input = input("Your Input: ") # TODO: Safe input function with exception handling. To cover erroneous inputs. Ex. no input 
	
	if user_Input == '':
		return '', 0 # Incorrect usage

	user_Input = int(user_Input)

	if user_Input not in list(range(1, len(options)+1)):
		return '', 0
	else:
		return user_Input, 1




def main():
	cFlag = 1
	options = ["Add Password", "Delete Password", "Show password from a Site", "View All", "Delete All"]

	while True:
		
		display_Main_Menu(options, cFlag)
		user_Input, cFlag = safe_Input(options)

		if not cFlag:
			continue # Restart main menu but with example usage

		display_Option(options, user_Input)
		user_Input, cFlag = safe_Input(options)






		# # Correct Input usage from user
		# while cFlag:
		# 	display_Option(options, user_Input)
		# 	user_Input, cFlag = safe_Input(options)

		# 	if user_Input == 'q' or 'Q':
		# 		break












		break





if __name__ == "__main__":
	main()
