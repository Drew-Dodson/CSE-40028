# Assignment 03
# CSE-40028, 145020, Winter 2020
# Robert Dodson

# Get the input of a numberical value from user
def getUserInput():

	usersChoice = input("Let me help you choose a movie or show. Type in a number 1-10: ")
	return usersChoice


def printOutMovie(usersChoice) :
	print("You should watch:")
	if usersChoice == "1":
		print("Finding Nemo")
	elif usersChoice == "2":
		print("Breaking Bad")
	elif usersChoice == "3":
		print("Black Mirror")
	elif usersChoice == "4":
		print("The Devil Next Door")
	elif usersChoice == "5":
		print("Night on Earth")
	elif usersChoice == "6":
		print("Arrested Development")
	elif usersChoice == "7":
		print("Pandemic")
	elif usersChoice == "8":
		print("Street Food")
	elif usersChoice == "9":
		print("Tremors")
	else:
		print("Narcos")


usersChoice = getUserInput()
printOutMovie(usersChoice)