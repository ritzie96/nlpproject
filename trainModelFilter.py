import os
import nltk
import json
import gensim


def getSentences(directory):
		data = []
		ll = ""
		print("hello")
		for subdir, dirs, files in os.walk(self.filename):
			for fil in files:
				print(os.path.join(subdir,fil))
				f = open(os.path.join(subdir,fil),'r')
				for line in f:
					data = json.loads(line)
					print(data)
					ll = ll + [i for i in unicode(data, 'utf-8').lower().split()]
			
			print (ll)
		yield ll


get = getSentences("extracted")
get.next()
