# Assignment 05
# CSE-40028, 145020, Winter 2020
# Robert Dodson
# Jukebox

# Refactor options: This could be done better with a dictionary or something like a Class or Struct (Do these exist in Python vs Swift?).

# Available Genres
genreChoices = ["Country", "Oldies", "Pop", "Rock", "Rap"]

# Available Artists
countryChoices = ["Luke Bryan", "Blake Shelton", "Tim McGraw"]
oldiesChoices = ["Loius Armstrong", "Frank Sinatra"]
popChoices = ["Arianna Grande", "Katy Perry"]
rockChoices = ["Fall Out Boy", "Blink-182", "Sum 41"]
rapChoices = ["Lil Nas X", "Lupe Fiasco", "Kendrick Lamar"]

# Country Arist Songs
lukeBryanChoices = ["Country Girl", "Kiss Tomorrow Goodbye", "I Know You're Gonna Be There"]
blakeSheltonChoices = ["God's Country", "Neon Light", "Sangria"]
timMcGrawChoices = ["Humble and Kind", "Shotgun Rider", "Live Like You Were Dying"]

# Oldies Arist Songs
louisArmstrongChoices = ["What a Wonderful World", "Cool Yule", "La Vie En Rose"]
franSinatraChoices = ["Fly Me To The Moon", "My Way", "That's Life"]

# Pop Arist Songs
arianaGrandeChoices = ["7 Rings", "Break Up With Your Girlfriend, I am Bored", "Thank U, Next"]
katyPerryChoices = ["Dark Horse", "Roar", "Firework"]

# Rock Arist Songs
fallOutBoyChoices = ["Centuries", "My Songs Know What You Did In The Dark", "Uma Thurman"]
blink182Choices = ["I Miss You", "The Rock Show", "First Date"]
sum41Choices = ["Fat Lip", "In Too Deep", "Still Waiting"]

# Rap Arist Songs
lilNasXChoices = ["Panini", "Old Town Rold", "Rodeo"]
lupeFiascoChoices = ["The Show Goes On", "Superstar", "Kick, Push"]
kendrickLamarChoices = ["Humble.", "DNA.", "Love."]


# Get the Genre the user would like to use and return it to be stored as a global var
def getGenreChoice():
	print("What genre of music would you like to listen to?")
	for position, value in enumerate(genreChoices):
			print((position + 1), ':', value)
	usersChoice = input("Please enter a number: ")
	print("\n")
	return usersChoice

# Use the global var 'genreChoice' to display artist choices based off of current value. Enumerate over all of the artists of the selected genre. Store artist choice as global var
def getArtistChoice(genreChoice):

	if genreChoice == "1":
		print("Country Arists:")
		for position, value in enumerate(countryChoices):
			print((position + 1), ':', value)
	elif genreChoice == "2":
		print("Oldies Arists:")
		for position, value in enumerate(oldiesChoices):
			print((position + 1), ':', value)
	elif genreChoice == "3":
		print("Pop Artists: ")
		for position, value in enumerate(popChoices):
			print((position + 1), ':', value)
	elif genreChoice == "4":
		print("Rock Artists: ")
		for position, value in enumerate(rockChoices):
			print((position + 1), ':', value)
	elif genreChoice == "5":
		print("Rap Artists:")
		for position, value in enumerate(rapChoices):
			print((position + 1), ':', value)
	else:
		print("Error with Genre selection")

	print("What Artist would you like to listen to?")
	usersChoice = input("Please enter a number: ")
	print("\n")
	return usersChoice


# Use the global var 'genreChoice' && 'aristChoice' to display song choices based off of current value. Enumerate over all of the songs of the selected artisst. Store song choice as global var
def getSongChoice(genreChoice, artistChoice):
	if genreChoice == "1":
		if artistChoice == "1":
			print("Luke Bryan Songs: ")
			for position, value in enumerate(lukeBryanChoices):
				print((position + 1), ':', value)
		elif artistChoice == "2":
			print("Blake Shelton Songs: ")
			for position, value in enumerate(blakeSheltonChoices):
				print((position + 1), ':', value)
		elif artistChoice == "3":
			print("Tim McGraw Songs: ")
			for position, value in enumerate(timMcGrawChoices):
				print((position + 1), ':', value)


	elif genreChoice == "2":
		if artistChoice == "1":
			print("Louis Armstrong Songs: ")
			for position, value in enumerate(louisArmstrongChoices):
				print((position + 1), ':', value)
		elif artistChoice == "2":
			print("Frank Sinatra Songs: ")
			for position, value in enumerate(franSinatraChoices):
				print((position + 1), ':', value)


	elif genreChoice == "3":
		if artistChoice == "1":
			print("Ariana Grande Songs: ")
			for position, value in enumerate(arianaGrandeChoices):
				print((position + 1), ':', value)
		elif artistChoice == "2":
			print("Katy Perry Songs: ")
			for position, value in enumerate(katyPerryChoices):
				print((position + 1), ':', value)


	elif genreChoice == "4":
		if artistChoice == "1":
			print("Fall Out Boy Songs: ")
			for position, value in enumerate(fallOutBoyChoices):
				print((position + 1), ':', value)
		elif artistChoice == "2":
			print("Blink-182 Songs: ")
			for position, value in enumerate(blink182Choices):
				print((position + 1), ':', value)
		elif artistChoice == "3":
			print("Sum 41 Songs: ")
			for position, value in enumerate(sum41Choices):
				print((position + 1), ':', value)


	elif genreChoice == "5":
		if artistChoice == "1":
			print("Lil Nas X Songs: ")
			for position, value in enumerate(lilNasXChoices):
				print((position + 1), ':', value)
		elif artistChoice == "2":
			print("Lupe Fiasco Songs: ")
			for position, value in enumerate(lupeFiascoChoices):
				print((position + 1), ':', value)
		elif artistChoice == "3":
			print("Kendrick Lamar Songs: ")
			for position, value in enumerate(kendrickLamarChoices):
				print((position + 1), ':', value)
	else:
		print("Error")

	print("What song would you like to listen to?")
	usersChoice = input("Please enter a number: ")
	print("\n")
	print("Starting jukebox!")
	return usersChoice


# Utilizing this allows my faux main() function to only call startJukeBox() to begin the program
def startJukeBox():
	genreChoice = getGenreChoice()
	artistChoice = getArtistChoice(genreChoice)
	songChoice = getSongChoice(genreChoice, artistChoice)
	restartJukeBox()


# Loop to see if we want to play another song.
def restartJukeBox():
	print("Would you like to select another song?")
	usersChoice = input("y | n: ")
	if usersChoice == "y" or usersChoice == "Y":
		print("\n")
		startJukeBox()
	else:
		print("\n")
		print("Good bye!")


# Start this baby up and jam out
startJukeBox()
