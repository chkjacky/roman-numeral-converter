import re

# THE DICTIONARY OF THE ARABIC NUMERALS WITH ROMAN NUMERALS
romanChar = {
	1: 'I',
	2: 'II',
	3: 'III',
	4: 'IV',
	5: 'V',
	6: 'VI',
	7: 'VII',
	8: 'VIII',
	9: 'IX',
	10: 'X',
	50: 'L',
	100: 'C',
	500: 'D',
	1000: 'M',
	5000: 'V',
}



# VALIDATE THE USER INPUT
def validateUserInput( userInput ): 
	# Check whether the userInput is an integer or a float using regular expression
    if( re.match("[+]?\d+$", userInput) ):
        # Convert the userInput to integer
    	userInput = int( userInput )
    else:
        # Display error message and restart the while loop
    	print("Invalid Input! Please enter an integer or a float. \n")
    	return False 

    return userInput



# CONVERT THE ARABIC NUMERALS TO THE ROMAN NUMERALS
def convertRomanNumeral( romanChar, tempNumber, romeString ):
	while ( tempNumber > 0 ):

		# Loop thru the romanChar dictionary
		for digit, numeral in romanChar.items():
			# Compare the tempNumber with the digit (romanChar's Key)
			if (tempNumber == digit):
				romeString= romanChar.get(digit) + romeString

				# TempNumber minus the digit for next while loop
				tempNumber -= digit

			elif (tempNumber < digit):
				# Get the index/position of the digit (romadnChar's Key)
				index = list(romanChar).index(digit)

				'''
				PATTERN AND SEQUENCE IN ROMAN NUMERALS
				The tricks here are dividing tempNumber by digit:
					if the result is 0.9 or more, means the tempNumber is near to the end (10, 100, 1000...),
						let say:
							if the arabic number is 9, the end is 10, hence we shall add "I" before "X"
							if the arabic number is 90, the end is 100, hence we shall add "X" before "C"
							if the arabic number is 900, the end is 1000, hence we shall add "C" before "M";

					else if the result is 0.8 or more, means the tempNumber is near to the mid (50, 500...), 
						let say:
							if the arabic number is 4, the mid is 5, hence we shall add "I" before "V"
							if the arabic number is 40, the mid is 50, hence we shall add "X" before "L";
				
				Please refer to the documentation for more information
				'''
				if( tempNumber / digit >= 0.9 ):
					if(tempNumber >= 50):
						romeString = romanChar.get((list(romanChar.keys())[index])) + romeString
						romeString = romanChar.get((list(romanChar.keys())[index - 2])) + romeString
						tempNumber -= (list(romanChar.keys())[index])

					else: 
						romeString = romanChar.get((list(romanChar.keys())[index ])) + romeString
						romeString = romanChar.get((list(romanChar.keys())[index - 1])) + romeString
						tempNumber -= (list(romanChar.keys())[index])

				elif( tempNumber / digit >= 0.8 and tempNumber / digit < 1 ):
					if(tempNumber >= 50 and tempNumber < 100):
						romeString = romanChar.get((list(romanChar.keys())[index - 2])) + romeString
						tempNumber -= (list(romanChar.keys())[index - 2])

					else:
						romeString = romanChar.get((list(romanChar.keys())[index])) + romeString
						romeString = romanChar.get((list(romanChar.keys())[index - 1])) + romeString
						tempNumber -= (list(romanChar.keys())[index])

				else: 
					if(tempNumber >= 50 and tempNumber < 100 ):
						romeString = romanChar.get((list(romanChar.keys())[index - 2])) + romeString
						tempNumber -= (list(romanChar.keys())[index - 2])

					else:
						romeString = romanChar.get((list(romanChar.keys())[index - 1])) + romeString
						tempNumber -= (list(romanChar.keys())[index - 1])
			else:
				continue

			break

	return romeString



# MAIN FUNCTION
def main():
	# Default counter for while loop
	x = 0

	while( x != -1 ):
		# Get user input
		userInput = input("\nInput an integer:\t")

		# Validate user input
		userInput = validateUserInput( userInput )

		# Verify user input return from the function
		if userInput is False:
			continue

		# Check the userInput size
		if( userInput == 0 or userInput >= 1501 ):
			print("Out of range! Enter integer number less than 1501 and more than 0. \n")
			continue

		# Assign value to the number variable 
		number = userInput

		# Counter for forloop below
		i = 0

		# Temporary number to breakdown and store the user input
		tempNumber = 0

		# Roman String with empty value
		romeString = ''

		# Break down the number into a list where we can identify its place value
		arrNumber = [int(i) for i in str(number)]

		# Inverse the array at this point, so that the unit will be at the 1st place, ten at 2nd place, ...
		arrNumber =  list(reversed(arrNumber))

		# CONVERSION BEGINS HERE
		for placeValue in arrNumber:

			# Since the user input has been broken down and saved into an array
			# Each numbers has their place value, unit, ten, hundred, etc
			# This is to make sure the number is multiplied by its places before conversion
			powerOfTen = pow(10, i)

			if (placeValue == 0):
				i += 1
				continue
			else : 
				tempNumber += (placeValue * powerOfTen)

			# Pass the variables in as arguments
			romeString = convertRomanNumeral(romanChar, tempNumber, romeString)

			# Increase the loop by 1 after each loop
			i += 1

			# Reset the tempNumber as we read from the arrNumber
			tempNumber = 0

		# Rome string has been concatenated properly in the function 
		# Display the result
		print("Roman Numeral:\t\t" + romeString)


# FUNCTION CALLING
main()