import csv

filename = 'results.csv'

def showStats():
	highestMark = -1
	numberOfWrongAnswers = 0
	numberOfCorrectAnswers = 0
	numberOfAllCorrectSubmissions = 0
	highestMarkUser = ""

	with open(filename) as file:
		reader = csv.reader(file,delimiter=",")
		for row in reader:
			score = calculateScore(row[2:])
			wrongs = calculateWrongs(row[2:])
			corrects = caculateCorrects(row[2:])

			userID = row[0]
			testID = row[1]

			if score > highestMark:
				highestMark = score
				highestMarkUser = userID

			numberOfWrongAnswers += wrongs
			numberOfCorrectAnswers += corrects
			
			if wrongs == 0:
				numberOfAllCorrectSubmissions += 1


	print("Highest mark ever scored in a test: " + str(highestMark))
	print("User ID with the highest mark: " + highestMarkUser)
	print("Number of wrong answers recorded: " + str(numberOfWrongAnswers))
	print("Number of correct answers recorded: " + str(numberOfCorrectAnswers))
	print("Number of perfect scores recorded: " + str(numberOfAllCorrectSubmissions))





def calculateScore(row):
	score = 0
	for each in row:
		if each == "1":
			score += 1
	return score


def calculateWrongs(row):
	wrongs = 0
	for each in row:
		if each == "0":
			wrongs += 1
	return wrongs

def caculateCorrects(row):
	corrects = 0
	for each in row:
		if each == "1":
			corrects += 1
	return corrects




showStats()