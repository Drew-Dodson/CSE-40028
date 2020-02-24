# Assignment 06
# CSE-40028, 145020, Winter 2020
# Robert Dodson
# Jukebox

# Refactor options: This could be done better with a dictionary or something like a Class or Struct (Do these exist in Python vs Swift?).

# Available Genres
genreChoices = {
	1: "Country",
	2: "Oldies",
	3:  "Pop",
	4:  "Rock",
	5:  "Rap"
}

# Available Artists
countryChoices = {
	1: "Luke Bryan",
	2: "Blake Shelton",
	3: "Tim McGraw"
}

oldiesChoices = {
	1: "Loius Armstrong",
	2: "Frank Sinatra"
}

popChoices = {
	1: "Arianna Grande",
	2: "Katy Perry"
}

rockChoices = {
	1: "Fall Out Boy",
	2: "Blink-182",
	3: "Sum 41"
}

rapChoices = {
	1: "Lil Nas X",
	2: "Lupe Fiasco",
	3: "Kendrick Lamar"
}

# Country Arist Songs
lukeBryanChoices = {
	1: "Country Girl",
	2: "Kiss Tomorrow Goodbye",
	3: "I Know You're Gonna Be There"
}

blakeSheltonChoices = {
	1: "God's Country",
	2: "Neon Light",
	3: "Sangria"
}

timMcGrawChoices = {
	1: "Humble and Kind",
	2: "Shotgun Rider",
	3: "Live Like You Were Dying"
}

# Oldies Arist Songs
louisArmstrongChoices = {
	1: "What a Wonderful World",
	2: "Cool Yule",
	3: "La Vie En Rose"
}

franSinatraChoices = {
	1: "Fly Me To The Moon",
	2: "My Way",
	3: "That's Life"
}

# Pop Arist Songs
arianaGrandeChoices = {
	1: "7 Rings",
	2: "Break Up With Your Girlfriend, I am Bored",
	3: "Thank U, Next"
}

katyPerryChoices = {
	1: "Dark Horse",
	2: "Roar",
	3: "Firework"
}

# Rock Arist Songs
fallOutBoyChoices = {
	1: "Centuries",
	2: "My Songs Know What You Did In The Dark",
	3: "Uma Thurman"
}

blink182Choices = {
	1: "I Miss You",
	2: "The Rock Show",
	3: "First Date"
}

sum41Choices = {
	1: "Fat Lip",
	2: "In Too Deep",
	3: "Still Waiting"
}

# Rap Arist Songs
lilNasXChoices = {
	1: "Panini",
	2: "Old Town Rold",
	3: "Rodeo"
}

lupeFiascoChoices = {
	1: "The Show Goes On",
	2: "Superstar",
	3: "Kick, Push"
}

kendrickLamarChoices = {
	1: "Humble.",
	2: "DNA.",
	3: "Love."
}



# Get the Genre the user would like to use and return it to be stored as a global var
def getGenreChoice():
	print("What genre of music would you like to listen to?")
	for key, value in genreChoices.items():
		print(key, ": ", value)
	usersChoice = input("Please enter a number: ")
	print("\n")
	return usersChoice



# Use the global var 'genreChoice' to display artist choices based off of current value. Enumerate over all of the artists of the selected genre. Store artist choice as global var
def getArtistChoice(genreChoice):
	if genreChoice == "1":
		print("Country Arists:")
		for key, value in countryChoices.items():
			print(key, ": ", value)
	elif genreChoice == "2":
		print("Oldies Arists:")
		for key, value in oldiesChoices.items():
			print(key, ": ", value)
	elif genreChoice == "3":
		print("Pop Artists: ")
		for key, value in popChoices.items():
			print(key, ": ", value)
	elif genreChoice == "4":
		print("Rock Artists: ")
		for key, value in rockChoices.items():
			print(key, ": ", value)
	elif genreChoice == "5":
		print("Rap Artists:")
		for key, value in rapChoices.items():
			print(key, ": ", value)
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
			for key, value in lukeBryanChoices.items():
				print(key, ": ", value)
		elif artistChoice == "2":
			print("Blake Shelton Songs: ")
			for key, value in blakeSheltonChoices.items():
				print(key, ": ", value)
		elif artistChoice == "3":
			print("Tim McGraw Songs: ")
			for key, value in timMcGrawChoices.items():
				print(key, ": ", value)


	elif genreChoice == "2":
		if artistChoice == "1":
			print("Louis Armstrong Songs: ")
			for key, value in louisArmstrongChoices.items():
				print(key, ": ", value)
		elif artistChoice == "2":
			print("Frank Sinatra Songs: ")
			for key, value in franSinatraChoices.items():
				print(key, ": ", value)


	elif genreChoice == "3":
		if artistChoice == "1":
			print("Ariana Grande Songs: ")
			for key, value in arianaGrandeChoices.items():
				print(key, ": ", value)
		elif artistChoice == "2":
			print("Katy Perry Songs: ")
			for key, value in katyPerryChoices.items():
				print(key, ": ", value)


	elif genreChoice == "4":
		if artistChoice == "1":
			print("Fall Out Boy Songs: ")
			for key, value in fallOutBoyChoices.items():
				print(key, ": ", value)
		elif artistChoice == "2":
			print("Blink-182 Songs: ")
			for key, value in blink182Choices.items():
				print(key, ": ", value)
		elif artistChoice == "3":
			print("Sum 41 Songs: ")
			for key, value in sum41Choices.items():
				print(key, ": ", value)


	elif genreChoice == "5":
		if artistChoice == "1":
			print("Lil Nas X Songs: ")
			for key, value in lilNasXChoices.items():
				print(key, ": ", value)
		elif artistChoice == "2":
			print("Lupe Fiasco Songs: ")
			for key, value in lupeFiascoChoices.items():
				print(key, ": ", value)
		elif artistChoice == "3":
			print("Kendrick Lamar Songs: ")
			for key, value in kendrickLamarChoices.items():
				print(key, ": ", value)
	else:
		print("Error")

	print("What song would you like to listen to?")
	usersChoice = input("Please enter a number: ")
	print("\n")
	print("Starting jukebox!")
	return usersChoice




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
