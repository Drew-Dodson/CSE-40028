# Assignment 07
# CSE-40028, 145020, Winter 2020
# Robert Dodson
# Note to self: Us proper Python naming scheme for vars like variable_name
# Read-only mode for files
# demofile1.txt
# demofile2.txt



# Grab the file the user wishes to read from
def getFileName():
	print("What is the name of the file to read from?")
	file_name = input("Please enter a file name: ")
	return file_name


# Parse that file and show statistics
def readFile(file_name):
	line_index = 0
	character_index = 0
	try:
		print("\n")
		print("Reading from file name:", file_name)
		text = open(file_name, "r")
		for line in text:
			print(line_index + 1, "-" , line.strip())
			line_index = line_index + 1
			for character in line:
				character_index = character_index + 1
		print("\n")
		print("File Stats:")
		print("Total number of lines:", line_index)
		print("total number of characters:", character_index)
		print("\n")
		text.close()
	except:
		print("Error loading file:", file_name)
		print("\n")


# Restart challenge to user
def restart():
	print("Would you like to select another file?")
	usersChoice = input("y | n: ")
	if usersChoice == "y" or usersChoice == "Y":
		print("\n")
		startFileReader()
	else:
		print("\n")
		print("Good bye!")


# Allows the program to run multiple times
def startFileReader():
	file_name = getFileName()
	readFile(file_name)
	restart()


# Start the program
startFileReader()