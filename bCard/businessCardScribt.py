
# Business Card Class
class Card:
	lastName = ""
	fullName = ""
	email = ""
	address = ""
	phoneNumber = ""
	nameOrPos = ["",""]
	position = ""
		
# open file and read lines
file = open("businessCard.txt", "r")

allLines = file.readlines()


# instantiate boolean to check if the line 
# is the second line of the address as false
secondLineAdd = False

# line counter
lineInd = 0

# get last line
last = allLines[-1]

# array of card objects
cards = []

# counter for number of cards
numCard = 0

# initial card
cards.append(Card())

# iterate through lines, newline determines new card
for line in allLines:
	i = 0
	y = 0
	x = 0
	j = 3
	
	isEmail = False
	isNumeric = False
	
	firstThreeChars = line[i:i+3]

# checking if the line being read is the second line of address
	if(secondLineAdd == False):
		# if newline separating cards 
		if line == '\n':
			# determining whether string is Name or Position Title by checking 
			# if it contains the last name found in the email
			if cards[numCard].lastName.lower() in cards[numCard].nameOrPos[0].lower():

				cards[numCard].fullName = cards[numCard].nameOrPos[0]
				cards[numCard].position = cards[numCard].nameOrPos[1]
				
			else:
				cards[numCard].fullName = cards[numCard].nameOrPos[1]
				cards[numCard].position = cards[numCard].nameOrPos[0]
			
			# add new card
			cards.append(Card())
			numCard+=1
			# idk why I have to do this
			cards[numCard].nameOrPos = ["", ""]
				
#line is not new line or last line
		else:
		
			# differentiates address and phone number
			if (firstThreeChars.isnumeric()) or (line[i+1:i+4].isnumeric()):

			#check if numeric groups of three
				while(j <= 6):
					if (line[j:j+3].isnumeric()):
						isNumeric = True
					j += 1

				if(isNumeric == True):
					cards[numCard].phoneNumber += line
				else:
					cards[numCard].address += line
					# adding next line of address
					cards[numCard].address += "	" + allLines[lineInd+1]
					secondLineAdd = True
		
			else:
				#checks for email and finds last name
				for i in range(len(line)):
					if(line[i] == '@'):

						for x in range(1,i):
							cards[numCard].lastName += line[x]

						cards[numCard].email += line
						isEmail = True

				if (isEmail == False) and (secondLineAdd == False):
					if(cards[numCard].nameOrPos[0] == ""):
						
						cards[numCard].nameOrPos[0] = line
					
					else:
						cards[numCard].nameOrPos[1] = line
		lineInd += 1

	# if the line is the second line of the address
	else:
		lineInd += 1
		secondLineAdd = False

	# check if its the last line of the file rather than newline
	if (line == last):

		# determining whether string is Name or Position Title
		if cards[numCard].lastName.lower() in cards[numCard].nameOrPos[0].lower():

			cards[numCard].fullName = cards[numCard].nameOrPos[0]
			cards[numCard].position = cards[numCard].nameOrPos[1]
			
		else:
			cards[numCard].fullName = cards[numCard].nameOrPos[1]
			cards[numCard].position = cards[numCard].nameOrPos[0]
			
# print all data
for f in range(2):
	print("Card: " + str(f+1) + "\n")
	print("	Full name: \n 	" + cards[f].fullName)
	print("	Position: \n 	" + cards[f].position)
	print("	Phone Number: \n 	" + cards[f].phoneNumber)
	print("	Address: \n 	" + cards[f].address)
	print("	Email: \n 	" + cards[f].email)

