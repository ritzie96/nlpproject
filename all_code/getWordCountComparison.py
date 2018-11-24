from subprocess import check_output
import re




def removeNotLetter(word):
	return re.sub('\W','', word)


def getWordCountNovice(word):
	try:
		x = check_output(["grep", " "+word+"$","removed_all_freq.txt"])
		x = str(x)
		#print(type(x))
		#print(x)
		count = re.findall(r'\d+',x)
		#print(word + " " + count[0])
		return count[0]
	except:
		return "0"

def getWordCountExpert(word):
	try:
		x = check_output(["grep", " "+word+"$","new_expert_freq.txt"])
		x = str(x)
		#print(type(x))
		#print(x)
		count = re.findall(r'\d+',x)
		#print(word + " " + count[0])
		return count[0]
	except:
		return "0"

with open("Metric/final_describe_words_clean.txt", "r") as f:
	for line in f:
		word = removeNotLetter(line)
		noviceFreq = getWordCountNovice(word)
		expertFreq = getWordCountExpert(word)
		print(word + ": " + expertFreq + " " + noviceFreq)




