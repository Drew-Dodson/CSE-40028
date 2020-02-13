# Assignment 04
# CSE-40028, 145020, Winter 2020
# Robert Dodson

# Starting variables to control flow
currentNumber = 10000
removalNumber = 100


# Starting the count from 10000 down to 0
while (currentNumber > 0):
	# This will reset the removalNumber to match the output file as well as prevents an infinate loop if we did not.
	# The output shows we are removing by (removalNumber) and then (removalNumber - 1) next iteration until we get to less than 10 then it resets to 100
	if removalNumber < 10: removalNumber = 100

	# Print the current number we are on based off of the currentNumber variable
	print(currentNumber)
	currentNumber = currentNumber - removalNumber
	removalNumber = removalNumber - 1

# Print final 0 to end the output
print(0)