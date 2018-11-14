import re
from prettytable import PrettyTable




def removeNotLetter(word):
	return re.sub('\W','', word)


table = PrettyTable()

with open("Ranked Results - Dance.txt", "r") as fp:

	for cnt, line in enumerate(fp):
		#if encounter new descriptive word
		matchNewWord = re.match(r'(.*) word (.*?) .*',line)
		matchCompareWordSame = re.match(r'Word (.*?) found at position ([0-9]*) in both lists',line)
		matchCompareWordDiff = re.match(r'Word (.*?) found at position ([0-9]*) and ([0-9]*)',line)
		if matchNewWord:
			
			print(table)
			print("\n")
			descWord = matchNewWord.group(2)
			descWord = removeNotLetter(descWord)
			print("Similar words to " + descWord)
			table = PrettyTable()
			table.field_names = ["Word", "Novice Pos", "Expert Pos", "Difference"]
		#then comes novicelist of words
		#and the expertlist
		#we dont need to display
		#then comes the words we want to display
		elif matchCompareWordSame:
			#print(matchCompareWordSame.group())
			compareWord = matchCompareWordSame.group(1)
			compareWord = removeNotLetter(compareWord)
			position = matchCompareWordSame.group(2)
			table.add_row([compareWord,position,position,'0'])
			#print("same positions")
			#print(compareWord)
			#print(position)
		elif matchCompareWordDiff:
			#print(matchCompareWordDiff.group())
			compareWordDiff = matchCompareWordDiff.group(1)
			compareWordDiff = removeNotLetter(compareWordDiff)
			position1 = matchCompareWordDiff.group(2)
			position2 = matchCompareWordDiff.group(3)
			difference = (int(position1)-int(position2))
			table.add_row([compareWordDiff,position1,position2,difference])
			#print("Different positions")
			#print(compareWordDiff)
			#print(position1)
			#print(position2)
print(table)
