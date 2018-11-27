import re



simsFileNameExp = "psy_exp_sort"
simsFileNameNov = "psy_nov_sort"


def printLatexRowMetricTable(word, freqE, freqN, simE, simN):
	print(word + " & " + freqE + " & & " + str(int(freqE)-int(freqN)) + " & " + simE + " & & " + simN +  " \\\\ \\hline")



#read read the similarity and insert into arrays
valuesDict = {}
def readSimilarityFiles():
	with open(simsFileNameExp, "r") as f:
		for cnt,line in enumerate(f):
			wordC = re.match(r'(.*?)[:](.*)', line)
			#the similarity
			word = wordC.group(1)
			#expSim.append(wordC.group(2))
			#add value to dict
			valuesDict[word] = [wordC.group(2)]
			#print(valuesDict[word])

	with open(simsFileNameNov, "r") as f:
		for cnt,line in enumerate(f):
			wordC = re.match(r'(.*?)[:](.*)', line)
			#print(wordC)
			#the similarity
			word = wordC.group(1)
			#novSim.append(wordC.group(2))
			#add values
			valuesDict[word].append(wordC.group(2))
			#print(valuesDict[word])
		

def getDiscreteChar(number):
	if number < 0.05:
		return "L"
	if 0.05 <= number <= 0.3:
		return "M"
	if number > 0.3:
		return "H" 
#laad the similarities into valuesDict
readSimilarityFiles()
for word in valuesDict:
	expDiscrete = (getDiscreteChar(float((valuesDict[word][0]))))
	nonDiscrete = (getDiscreteChar(float((valuesDict[word][1]))))
	print(word + " & " + expDiscrete + " & " + nonDiscrete + " \\\\ \\hline") 




'''
with open("wordcounts.txt", "r") as f:
	for cnt,line in enumerate(f):
		#print(cnt)
		wordC = re.match(r'(.*?)\: ([0-9]*) ([0-9]*)',line)
		if wordC:
			#print(wordC.group())
			# add the values to the dict
			word = wordC.group(1)
			expC = (wordC.group(2))
			expN = (wordC.group(3))
			try: 
				valuesDict[word].append(expC)
				valuesDict[word].append(expN)
				printLatexRowMetricTable(word, expC, expN, valuesDict[word][0],valuesDict[word][1])
			except KeyError:
				valuesDict[word] = []
				printLatexRowMetricTable(word, expC, expN, "-", "-")
	'''		



