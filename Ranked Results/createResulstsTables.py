import re
from prettytable import PrettyTable




def removeNotLetter(word):
	return re.sub('\W','', word)


dataCounts = dict()
#get the word frequncies from file
with open("wordCounts.txt", "r") as f:
	for cnt, line in enumerate(f):
		wordC = re.match(r'(.*?)\: ([0-9]*) ([0-9]*)',line)
		if wordC:
			#print(wordC.group())
			word = wordC.group(1)
			word = removeNotLetter(word)
			expC = (wordC.group(2))
			expN = (wordC.group(3))
			dataCounts[word] = [expC,expN]
			

table = PrettyTable()

with open("Ranked Results - Shooter.txt", "r") as fp:

	for cnt, line in enumerate(fp):
		#if encounter new descriptive word
		matchNewWord = re.match(r'(.*) word (.*?) .*',line)
		matchCompareWordSame = re.match(r'Word (.*?) found at position ([0-9]*) in both lists',line)
		matchCompareWordDiff = re.match(r'Word (.*?) found at position ([0-9]*) and ([0-9]*)',line)
		matchCompareWordNotPresentExp = re.match(r'(.*?) at position ([0-9]*) is not present in Expert list',line)
		if matchNewWord:
			print(table)
			print("\n")
			descWord = matchNewWord.group(2)
			descWord = removeNotLetter(descWord)
			print("Similar words to " + descWord)
			c = dataCounts.get(descWord)
			if c:
				#print()
				print("expert count: " + c[0] + " | Novice has " + c[1] + " less")
			else:
				print(descWord + " has no count")
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
		elif matchCompareWordNotPresentExp:
			compareWordNot = matchCompareWordNotPresentExp.group(1)
			compareWordNot = removeNotLetter(compareWordNot)
			position1 = matchCompareWordNotPresentExp.group(2)
			position2 = "-"
			difference = "-"
			table.add_row([compareWordNot,position1,position2,difference])
print(table)
